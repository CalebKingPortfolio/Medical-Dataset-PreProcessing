# import libraries
import numpy as np
import matplotlib.pyplot as plt

# UNPROCESSED FLASHCARD OUTPUTS THAT END WITH QUESTION MARKS
def analyze_output_question_marks_unprocessed(unprocessed_qm_ds, qm_count_unprocessed,unprocessed_fs_ds):

  # line chart showing unprocessed flashcard subset size - (left)
  x_1 = np.arange(unprocessed_qm_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='blue', label=f"Rows {unprocessed_qm_ds:,}")
  plt.title("Unprocessed - Flashcard Subset Size")
  plt.legend()

  # bar chart showing question mark count in outputs - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Questions Marks ({qm_count_unprocessed:,})']
  values = [qm_count_unprocessed]
  mycolors = ["red"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Output Questions Marks Count')
  plt.tight_layout()
  plt.show()

  #  bar chart showing unprocessed dataset size - (bottom)
  x_2 = np.arange(unprocessed_fs_ds)
  plt.figure(figsize=(23, 4))
  plt.subplot(1, 2, 1)
  plt.plot(x_2, x_2, color='green', label=f"Rows {unprocessed_fs_ds:,}")
  plt.title("Unprocessed - Dataset Size")
  plt.legend()
  plt.ylim(0)
  plt.show()
