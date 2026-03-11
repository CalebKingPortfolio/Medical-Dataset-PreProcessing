# import libraries
import numpy as np
import matplotlib.pyplot as plt

# CUT OFF ALPACARE UNPROCESSED 
def analyze_cutoff_alpa_unprocessed(unprocessed_alpa_ds, unprocessed_cut_off_count, unprocessed_cutoff_ds):

  # line chart showing unprocessed subset alpacare size - (left)
  x_1 = np.arange(unprocessed_alpa_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='red', label=f"Rows {unprocessed_alpa_ds:,}")
  plt.title(f"Unprocessed - AlpaCare-52k Subset Size")
  plt.legend()

  # bar chart showing unprocessed cut off rows - (right)
  plt.subplot(1, 2, 2) 
  labels = [f'Cut Off ({unprocessed_cut_off_count:,})']
  values = [unprocessed_cut_off_count]
  mycolors = ["blue"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Unprocessed AlpaCare-52k Cut Off Rows')
  plt.ylim(0)
  plt.tight_layout()
  plt.show()

  #  bar chart showing unprocessed dataset size - (bottom)
  x_2 = np.arange(unprocessed_cutoff_ds)
  plt.figure(figsize=(23, 4))
  plt.subplot(1, 2, 1)
  plt.plot(x_2, x_2, color='green', label=f"Rows {unprocessed_cutoff_ds:,}")
  plt.title("Unprocessed - Dataset Size")
  plt.legend()
  plt.ylim(0)
  plt.show()
