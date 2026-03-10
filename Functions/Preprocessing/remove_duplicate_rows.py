def remove_duplicate_rows(processed_missing_df):

  # creates another copy of the dataframe
  unprocessed_duplicates_df = processed_missing_df.copy() 

  # gets the length of the unprocessed dataframe
  unprocessed_duplicates_ds = len(unprocessed_duplicates_df)

  # finds duplicate rows and gets there index (row number)
  duplicated_rows_uprocessed = unprocessed_duplicates_df.index[unprocessed_duplicates_df.duplicated()].tolist()

  # gets the length of the duplicate rows
  duplicates_unprocessed = len(duplicated_rows_uprocessed)

  # drops the duplcated rows
  processed_duplicates_df = unprocessed_duplicates_df.drop_duplicates()

  # gets the length of the processed dataframe
  processed_duplicates_ds = len(processed_duplicates_df)

  # finds duplicate rows and gets there index (row number) after processing
  duplicated_rows_processed = processed_duplicates_df.index[processed_duplicates_df.duplicated()].tolist()

   # gets the length of the duplicate rows
  duplicates_processed = len(duplicated_rows_processed)

  # returns variables used within the function
  return(unprocessed_duplicates_ds, duplicates_unprocessed, processed_duplicates_ds, duplicates_processed, processed_duplicates_df)
