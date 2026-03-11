# import libraries
import numpy as np
import matplotlib.pyplot as plt

# FULLSTOP UNPROCESSED / PROCESSED ANALYSIS
def analyze_add_fullstops_pubcasual(processed_fs_ds, fs_count_unprocessed, fs_count_processed):

  # line chart showing subset pubmed size - (left)
  x_1 = np.arange(processed_fs_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='red', label=f"Rows {processed_fs_ds:,}")
  plt.title(f"Processed - PubMed Subset Size")
  plt.legend()

  # bar chart showing fullstops missing unprocessed - (right)
  plt.subplot(1, 2, 2) 
  labels = [f'Missing ({fs_count_unprocessed:,})']
  values = [fs_count_unprocessed]
  mycolors = ["red"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Unprocessed Output Missing Full Stops')
  plt.ylim(0)
  plt.tight_layout()
  plt.show()

  # bar chart showing fullstops missing processed - (bottom)
  plt.figure(figsize=(10.5, 4))
  labels = [f'Missing ({fs_count_processed:,})']
  values = [fs_count_processed]
  mycolors = ["purple"]
  plt.title('Processed Output Missing Full Stops')
  plt.bar(labels, values, color=mycolors)
  plt.ylim(0)
  plt.show()
