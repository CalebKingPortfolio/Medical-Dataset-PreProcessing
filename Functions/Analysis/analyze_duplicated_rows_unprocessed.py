# import libraries
import numpy as np
import matplotlib.pyplot as plt

# DUPLICATED ROWS UNPROCESSED ANALYSIS
def analyze_duplicated_rows_unprocessed(unprocessed_duplicates_ds, duplicates_unprocessed):

  # line chart showing dataset size - (left)
  x_1 = np.arange(unprocessed_duplicates_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='blue', label=f"Rows {unprocessed_duplicates_ds:,}")
  plt.title("Unprocessed - Dataset Size")
  plt.legend()

  # bar chart showing duplicate rows - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Duplicates ({duplicates_unprocessed:,})']
  values = [duplicates_unprocessed]
  mycolors = ["green"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Unprocessed - Duplicates Found')
  plt.tight_layout()
  plt.show()
