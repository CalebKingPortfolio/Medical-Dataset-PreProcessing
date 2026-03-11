# import libraries
import numpy as np
import matplotlib.pyplot as plt

# UNPROCESSED AND PROCESSED FILTERED LARGE AND SMALL VALUES
def analyze_filtered_rows(unprocessed_filtered_ds, total_droped, processed_filtered_ds):

  # line chart showing unprocessed dataset size - (left)
  x_1 = np.arange(unprocessed_filtered_ds)
  plt.figure(figsize=(9, 4))
  plt.subplot(1, 2, 1)
  plt.plot(x_1, x_1, color='blue', label=f"Rows {unprocessed_filtered_ds:,}")
  plt.title("Unprocessed - Dataset Size")
  plt.legend()

  # bar chart  showing dropped rows from threshold - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Rows ({total_droped:,})']
  values = [total_droped]
  mycolors = ["blue"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Dropped by Threshold (Min & Max)')
  plt.ylim(0)
  plt.tight_layout()
  plt.show()

  #  bar chart showing processed dataset size
  x_2 = np.arange(processed_filtered_ds)
  plt.figure(figsize=(23, 4))
  plt.subplot(1, 2, 1)
  plt.plot(x_2, x_2, color='red', label=f"Rows {processed_filtered_ds:,}")
  plt.title("Processed - Dataset Size")
  plt.legend()
  plt.ylim(0)
  plt.show()
