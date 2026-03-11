# import libraries
import numpy as np
import matplotlib.pyplot as plt

# CUT OFF ALPACARE PROCESSED
def analyze_cutoff_alpa_processed(processed_alpa_ds, processed_cut_off_count, processed_cutoff_ds):

  # line chart showing processed subset alpacare size - (left)
  x_1 = np.arange(processed_alpa_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='red', label=f"Rows {processed_alpa_ds:,}")
  plt.title(f"Processed - AlpaCare-52k Subset Size")
  plt.legend()

  # bar chart showing processed cut off rows - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Cut Off ({processed_cut_off_count:,})']
  values = [processed_cut_off_count]
  mycolors = ["blue"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Processed AlpaCare-52k Cut Off Rows')
  plt.ylim(0)
  plt.tight_layout()
  plt.show()

  #  bar chart showing processed dataset size - (bottom)
  x_2 = np.arange(processed_cutoff_ds)
  plt.figure(figsize=(23, 4))
  plt.subplot(1, 2, 1)
  plt.plot(x_2, x_2, color='green', label=f"Rows {processed_cutoff_ds:,}")
  plt.title("Processed - Dataset Size")
  plt.legend()
  plt.ylim(0)
  plt.show()
