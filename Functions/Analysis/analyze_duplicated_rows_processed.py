# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# DUPLICATED ROWS PROCESSED ANALYSIS
def analyze_duplicated_rows_processed(processed_duplicates_ds, duplicates_processed):

  # line chart showing dataset size - (left)
  x_1 = np.arange(processed_duplicates_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='blue', label=f"Rows {processed_duplicates_ds:,}")
  plt.title("Unprocessed - Dataset Size")
  plt.legend()

  # bar chart showing duplicate rows - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Duplicates ({duplicates_processed:,})']
  values = [duplicates_processed]
  mycolors = ["green"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Unprocessed - Duplicates Found')
  plt.tight_layout()
  plt.show()
