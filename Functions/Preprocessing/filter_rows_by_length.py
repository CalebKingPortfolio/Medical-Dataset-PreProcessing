def filter_rows_by_length(processed_spaces_df):

  # minumin and maximum row size
  min_total_chars = 25
  max_output_chars = 2000
  min_output_chars = 5 

  # copy of the dataframe
  unprocessed_filtered_df = processed_spaces_df.copy()

  # gets the original size of the dataset
  unprocessed_filtered_ds = len(unprocessed_filtered_df)

  # count length per row
  unprocessed_filtered_df['total_len'] = (
      unprocessed_filtered_df['instruction'].astype(str).str.len() +
      unprocessed_filtered_df['input'].astype(str).str.len() +
      unprocessed_filtered_df['output'].astype(str).str.len()
  )

  # keep rows with total_len >= min, output length <= max, and output length > min
  unprocessed_filtered_df = unprocessed_filtered_df[
      (unprocessed_filtered_df['total_len'] >= min_total_chars) &
      (unprocessed_filtered_df['output'].astype(str).str.len() <= max_output_chars) &
      (unprocessed_filtered_df['output'].astype(str).str.len() > min_output_chars)
  ]

  # drops the column total_len
  processed_filtered_df = unprocessed_filtered_df.drop(columns=['total_len'])

  # gets the original size of the dataset
  processed_filtered_ds = len(processed_filtered_df)

  # total number of rows droped
  total_droped = unprocessed_filtered_ds - processed_filtered_ds
  
  return(unprocessed_filtered_ds, processed_filtered_ds, total_droped, processed_filtered_df)
