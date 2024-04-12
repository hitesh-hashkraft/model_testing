from dotenv import load_dotenv
from llm_functions.gpt_functions import get_gpt_intent
from llm_functions.gemini_functions import get_gemini_intent
from llm_functions.anthropic_functions import get_claude_intent
import pandas as pd
from utils.calculate_accuracy import calculate_accuracy
import os
import time

load_dotenv()

prompt_file_path = "./model_testing/inputs/prompts/intent_matching_prompt.txt"
prompt_file_path_gemini = "./model_testing/inputs/prompts/intent_matching_prompt_gemini.txt"
csv_file_path = "./model_testing/inputs/csv_inputs/intent_match_data_set.csv"
output_file_path = "./model_testing/outputs/llm_intent_output.csv"
#accuracy_file_path = "./model_testing/llm_intent_accuracy.csv"


with open(prompt_file_path, "r") as file:
    prompt = file.read()


with open(prompt_file_path_gemini, "r") as file:
    prompt_gemini = file.read()
    
# Function to get intent based on provider and model
def get_intent(user_query, provider, model):
    if provider == 'gemini':
        intent = get_gemini_intent(prompt_gemini, user_query, model)
        return intent
    elif provider == 'claude':
        intent = get_claude_intent(prompt, user_query, model)
        return intent
    elif provider == 'gpt': 
        intent = get_gpt_intent(prompt, user_query, model)
        return intent
    else:
        return None

def main(llm_provider, model):
    # Read CSV file
    csv_data = pd.read_csv(csv_file_path)

    user_queries = csv_data['Question']
    actual_intents = csv_data['Intent']

    intent_list = []

    for i in range(len(user_queries)):
        print(i)
        user_query = user_queries[i]
        actual_intent = actual_intents[i]

        output_intent = get_intent(user_query, llm_provider, model)
            
        intent_list.append(output_intent)

        # time.sleep(20)
        

    # saving the output intent in a csv file
    intent_dataframe = pd.DataFrame(intent_list)
    csv_data[f'{model}_intent'] = intent_dataframe

    csv_data.to_csv(output_file_path, index=False)

    print("Output CSV file generated successfully.")


if __name__ == "__main__":
    llm_provider = input("Enter the LLM provider : ")
    model = input("Enter the model : ")
    main(llm_provider, model)
