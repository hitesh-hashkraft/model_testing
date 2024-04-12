import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
load_dotenv()

prompt_file_path = "./model_testing/inputs/prompts/intent_matching_prompt_gemini.txt"
api_key = os.environ.get("GOOGLE_API_KEY")

with open(prompt_file_path, "r") as file:
    prompt = file.read()

genai.configure(api_key=api_key)


def get_gemini_intent(prompt, user_query, model):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt + "\n" + user_query)
    response_json = json.loads(response.text) 
    return response_json.get("intent")


if __name__ == "__main__":
    print(get_gemini_intent(prompt, "Show me all the flats in mumbai", "gemini-pro"))