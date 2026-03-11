# import libraries
import numpy as np
import matplotlib.pyplot as plt

# EXRA SPACES PROCESSED ANALYSIS
def analyze_extra_spaces_processed(extra_spaces_ds, leading_trailing_spaces_processed, extra_spaces_instruction_processed, extra_spaces_input_processed, extra_spaces_output_processed):

  # line chart showing dataset size - (left)
  x_1 = np.arange(extra_spaces_ds)
  plt.figure(figsize=(9, 4))  # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='blue', label=f"Rows {extra_spaces_ds:,}")
  plt.title("Unprocessed - Dataset Size")
  plt.legend()

  # bar chart showing leading / trailing spaces peer cell - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Cells ({leading_trailing_spaces_processed:,})']
  values = [leading_trailing_spaces_processed]
  mycolors = ["red"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Cells with Leading or Trailing Spaces')
  plt.tight_layout()
  plt.ylim(0)
  plt.show()

  #  bar chart showing extra spaces per column - (bottom)
  plt.figure(figsize=(10.5, 4))
  labels = [f'Instruction ({extra_spaces_instruction_processed:,})', f'Input ({extra_spaces_input_processed:,})', f'Output ({extra_spaces_output_processed:,})' ]
  values = [extra_spaces_instruction_processed, extra_spaces_input_processed, extra_spaces_output_processed]
  mycolors = ["purple", "red", "green"]
  plt.title('Extra Spaces per Column')
  plt.bar(labels, values, color=mycolors)
  plt.ylim(0)
  plt.show()
