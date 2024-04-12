import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("./model_testing/llm_intent_output.csv")
output_file_path = "./model_testing/llm_intent_output.csv"

# Specify the columns you want to delete
columns_to_delete = [ 'gpt-3_intent']

# Drop the specified columns
df.drop(columns=columns_to_delete, inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv(output_file_path, index=False)

print("Columns deleted and modified CSV file saved successfully.")
