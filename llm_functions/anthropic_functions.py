import anthropic
import os
import json

from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)



def get_claude_intent(prompt, user_query, model):
    message = client.messages.create(
        model=model,
        max_tokens=2048,
        messages=[
            {"role": "user", "content": prompt + "\n" + user_query}
        ]
    )
    content_blocks = message.content
    print(content_blocks)
    try:
        content = content_blocks[0].text
        print(content)  # Extracting the text from the content blocks
        json_content = extract_json_from_text(content)
        print(json_content)
        intent_data = json.loads(json_content)  # Parsing JSON string to Python dictionary
        intent = intent_data.get('intent')  # Extracting the 'intent' field
        return intent
    except:
        return "None" 
    

def extract_json_from_text(text):
    # Find the starting index of the JSON content
    start_idx = text.find('{')
    # Find the ending index of the JSON content
    end_idx = text.rfind('}')
    # If either the start or end index couldn't be found, return None
    if start_idx == -1 or end_idx == -1:
        return None
    # Extract the substring from the start index to the end index, inclusive
    json_content = text[start_idx:end_idx+1]
    return json_content