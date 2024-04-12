import os
import pandas as pd

def create_mismatches_csv(output_file_path, model_name, output_dir):
    # Read the LLM intent output CSV file
    data = pd.read_csv(output_file_path)
    
    # Get the column names for the model intent
    model_intent_column = f"{model_name}_intent"
    
    # Filter rows where actual intent does not match model intent
    mismatches = data[data['Intent'] != data[model_intent_column]]
    
    # Create DataFrame for mismatches
    mismatches_df = mismatches[['Question', 'Intent', model_intent_column]]
    
    # Create CSV file name
    csv_file_name = f"{model_name}_mismatches_1.csv"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Write mismatches DataFrame to CSV in the output directory
    csv_file_path = os.path.join(output_dir, csv_file_name)
    mismatches_df.to_csv(csv_file_path, index=False)
    
    print(f"CSV file '{csv_file_name}' created with mismatched intents for model '{model_name}'.")

if __name__ == "__main__":
    output_file_path = "./model_testing/outputs/llm_intent_output.csv"
    output_dir = "./model_testing/mismatch_csvs"
    
    models = ['gpt-3.5-turbo-0125', 'gpt-4-0125-preview', 'gpt-3.5-turbo-1106', 'gpt-4-1106-preview', 'claude-3-opus-20240229']  # Add more models as needed
    
    for model_name in models:
        create_mismatches_csv(output_file_path, model_name, output_dir)
