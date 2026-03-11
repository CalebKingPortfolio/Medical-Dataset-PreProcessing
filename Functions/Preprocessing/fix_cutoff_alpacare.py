import re

def fix_cutoff_alpacare(processed_filtered_df):
    # 1. CRITICAL: Reset the index to prevent Pandas from dropping the wrong rows 
    df = processed_filtered_df.copy().reset_index(drop=True)

    # 2. Get the subset mask
    alpac_mask = df['subset_source'] == 'AlpaCare-52k'

    unprocessed_cutoff_ds = len(df)
    unprocessed_alpa_ds = alpac_mask.sum()

    # 3. Safely strip whitespace only from text columns 
    text_cols = ['instruction', 'input', 'output']
    for col in text_cols:
        if col in df.columns:
            df.loc[alpac_mask, col] = df.loc[alpac_mask, col].astype(str).str.strip()

    # 4. Helper function to check for missing punctuation
    def is_missing_punctuation(text):
        # Returns True if NO punctuation is found at the very end
        return len(re.findall(r'([.?\"\'\]!\)]\s*$)', str(text))) == 0

    # 5. Apply the check and find rows to drop
    is_cut_off = df.loc[alpac_mask, 'output'].apply(is_missing_punctuation)
    unprocessed_cut_off_count = is_cut_off.sum()

    indices_to_drop = is_cut_off[is_cut_off].index

    # 6. Drop the bad rows using our newly cleaned, unique index
    processed_df = df.drop(index=indices_to_drop)

    # 7. Recalculate stats for the processed dataframe
    processed_alpa_ds = (processed_df['subset_source'] == 'AlpaCare-52k').sum()
    processed_cutoff_ds = len(processed_df)

    # 8. Final verification count
    is_cut_off_final = processed_df.loc[processed_df['subset_source'] == 'AlpaCare-52k', 'output'].apply(is_missing_punctuation)
    processed_cut_off_count = is_cut_off_final.sum()

    # Return without the duplicate variable
    return (unprocessed_cutoff_ds, unprocessed_alpa_ds, processed_alpa_ds, 
            unprocessed_cut_off_count, processed_cutoff_ds, 
            processed_cut_off_count, processed_df)
