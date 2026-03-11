def fix_cutoff_alpacare(processed_filtered_df):

  # creates a copy so the original dataframe outside the function stays safe
  unprocessed_alpa_df = processed_filtered_df.copy()

  # gets the subset used
  alpac_subset = unprocessed_alpa_df['subset_source'] == 'AlpaCare-52k'

  # gets the length of the unprocessed dataframe
  unprocessed_cutoff_ds = len(unprocessed_alpa_df)

  # get the length of rows from the 'AlpaCare-52k' subset
  unprocessed_alpa_ds = len(unprocessed_alpa_df[alpac_subset])

  # strips the rows
  unprocessed_alpa_df.loc[alpac_subset] = (unprocessed_alpa_df.loc[alpac_subset].astype(str).apply(lambda x: x.str.strip()))

  # find rows which are cut off and over 1300 characters
  is_cut_off = unprocessed_alpa_df.loc[alpac_subset, 'output'].apply(
      lambda x: (len(re.findall(r'(?i)([.?\"\]!\)]\s*$)', str(x))) == 0) and (len(str(x)) > 1200)
  )

  # sum of rows found
  cut_off_unprocessed_count = is_cut_off.sum()

  # gets the index of the rows
  indices_to_drop = is_cut_off.index[is_cut_off]

  # drops the rows which are cut off and over 1300 characters
  processed_alpa_df = unprocessed_alpa_df.drop(index=indices_to_drop)

  # gets the subset used
  alpac_subset = processed_alpa_df['subset_source'] == 'AlpaCare-52k'

  # get the length of rows from the 'AlpaCare-52k' subset processed
  processed_alpa_ds = len(processed_alpa_df[alpac_subset])

  # gets the length of the unprocessed dataframe processed
  processed_cutoff_ds = len(processed_alpa_df)

 # find rows which are cut off and over 1300 characters
  is_cut_off_final = unprocessed_alpa_df.loc[alpac_subset, 'output'].apply(
      lambda x: (len(re.findall(r'(?i)([.?\"\]!\)]\s*$)', str(x))) == 0) and (len(str(x)) > 1200)
  )
  cut_off_processed_count = is_cut_off_final.sum()

  # return the variables that are used inside this function
  return(unprocessed_cutoff_ds, unprocessed_alpa_ds, processed_alpa_ds, cut_off_unprocessed_count, processed_cutoff_ds, cut_off_processed_count, processed_alpa_df)
