import re
import pandas as pd

def add_fullstops_pubcasual(processed_qm_output_df):

  # creates a copy so the original dataframe outside the function stays safe
  unprocessed_fs_output_df = processed_qm_output_df.copy() 

  # gets the original size of the dataset
  processed_fs_ds = len(unprocessed_fs_output_df)

  # gets the subset used
  pubmed_subset = unprocessed_fs_output_df['subset_source'] == 'medical_meadow_pubmed_causal'

  # strips the output
  unprocessed_fs_output_df.loc[pubmed_subset, 'output'] = unprocessed_fs_output_df.loc[pubmed_subset, 'output'].astype(str).str.strip()

  # regex pattern: looks for the end of the string NOT preceded by . or ?
  fs_regex = r'(?<![\.\?])$'

  # counts how many rows have no full stop at the end
  fs_count_unprocessed = unprocessed_fs_output_df.loc[pubmed_subset, 'output'].str.contains(fs_regex, regex=True).sum()

  # creates another copy so we have a distinct 'processed' object
  processed_fs_output_df = unprocessed_fs_output_df.copy()

  # replaces the no full stop with a full stop
  processed_fs_output_df.loc[pubmed_subset, 'output'] = processed_fs_output_df.loc[pubmed_subset, 'output'].replace(fs_regex, '.', regex=True)

  # counts how many rows have no full stop at the end after processing
  fs_count_processed = processed_fs_output_df.loc[pubmed_subset, 'output'].str.contains(fs_regex, regex=True).sum()

  # return the variables that are used inside this function
  return(processed_fs_ds, fs_count_unprocessed, fs_count_processed, processed_fs_output_df)
