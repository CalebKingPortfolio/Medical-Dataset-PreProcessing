import re

def remove_squished_commas(processed_spaces_df):

  # gives the dataframe another name
  unprocessed_commas_df = processed_spaces_df.copy()

  # regex pattern: comma not followed by a space or a digit
  pattern = r',(?![ \d])'

  # count total number of squished commas (using pandas .str.count is much faster than .apply(lambda))
  instruction_squished_commas_unprocessed = unprocessed_commas_df['instruction'].astype(str).str.count(pattern).sum()
  input_squished_commas_unprocessed = unprocessed_commas_df['input'].astype(str).str.count(pattern).sum()
  output_squished_commas_unprocessed = unprocessed_commas_df['output'].astype(str).str.count(pattern).sum()

  # remove squished commas
  processed_commas_df = unprocessed_commas_df.copy()
  for col in ['instruction', 'input', 'output']:
      # .fillna("") prevents nulls from becoming the string "nan"
      processed_commas_df[col] = processed_commas_df[col].fillna("").astype(str).str.replace(pattern, ', ', regex=True)

  # count total number of squished commas 
  instruction_squished_commas_processed = processed_commas_df['instruction'].str.count(pattern).sum()
  input_squished_commas_processed = processed_commas_df['input'].str.count(pattern).sum()
  output_squished_commas_processed = processed_commas_df['output'].str.count(pattern).sum()

  # gets size of the dataset
  processed_commas_ds = len(processed_commas_df)

  # returns variables used within the function
  return (
      instruction_squished_commas_unprocessed, 
      input_squished_commas_unprocessed, 
      output_squished_commas_unprocessed, 
      instruction_squished_commas_processed, 
      input_squished_commas_processed, 
      output_squished_commas_processed, 
      processed_commas_ds, 
      processed_commas_df
  )
