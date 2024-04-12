from openai import OpenAI
import os
from dotenv import load_dotenv
import json
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_KEY")
ORGANISATION_ID = os.environ.get("ORGANISATION_ID")

client = OpenAI(api_key=OPENAI_API_KEY,organization='org-3PpaVHeZveq1yiJkfuSwvQqi')


def get_gpt_intent(prompt, user_query, model):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_query}
        ],
        response_format={ "type": "json_object" }
    )
    response = completion.choices[0].message.content
    response_json = json.loads(response)
    gpt_intent = response_json['intent']
    return gpt_intent
