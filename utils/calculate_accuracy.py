import pandas as pd
import os

def calculate_accuracy(output_file_path, accuracy_file_path, model_name):
    # Read the LLM intent output CSV file
    data = pd.read_csv(output_file_path)
    
    # Get the column names for the model intent
    model_intent_column = f"{model_name}_intent"
    
    # Calculate the number of correct predictions
    correct_predictions = sum(data['Intent'] == data[model_intent_column])
    
    # Calculate the total number of predictions
    total_predictions = len(data)
    
    # Calculate the accuracy percentage
    accuracy_percentage = (correct_predictions / total_predictions) * 100 if total_predictions > 0 else 0
    
    # Create DataFrame for accuracy results
    accuracy_df = pd.DataFrame({'Model Name': [model_name], 'Accuracy Percentage': [accuracy_percentage]})
    
    # Check if the accuracy file exists
    if os.path.exists(accuracy_file_path):
        # Append accuracy results to the accuracy CSV file without header
        accuracy_df.to_csv(accuracy_file_path, mode='a', index=False, header=False)
    else:
        # Write DataFrame with header
        accuracy_df.to_csv(accuracy_file_path, index=False)
    
    print(f"Accuracy for {model_name}: {accuracy_percentage:.2f}%")

if __name__ == "__main__":
    output_file_path = "./model_testing/outputs/llm_intent_output.csv"
    accuracy_file_path = "./model_testing/outputs/llm_intent_accuracy.csv"
    
    models = ['gpt-3.5-turbo-0125', 'gpt-4-0125-preview', 'gpt-3.5-turbo-1106', 'gpt-4-1106-preview', 'claude-3-opus-20240229']  # Add more models as needed
    
    for model_name in models:
        calculate_accuracy(output_file_path, accuracy_file_path, model_name)
