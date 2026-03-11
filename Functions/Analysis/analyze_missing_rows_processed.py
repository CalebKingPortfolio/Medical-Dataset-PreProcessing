# import libraries
import numpy as np
import matplotlib.pyplot as plt

# MISSING ROWS PROCESSED ANALYSIS
def analyze_missing_rows_processed(processed_missing_ds, missing_row_count_processed, empty_instruction_rows_processed, empty_input_rows_processed, empty_output_rows_processed):
  
  # line chart showing dataset size - (left)
  x_1 = np.arange(processed_missing_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='blue', label=f"Rows {processed_missing_ds:,}")
  plt.title(f"Processed - Dataset Size")
  plt.legend()

  # bar chart showing missing rows - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Empty Rows ({missing_row_count_processed:,})']
  values = [missing_row_count_processed]
  mycolors = ["green"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Processed - Missing Rows')
  plt.ylim(0)
  plt.tight_layout()
  plt.show()

  #  bar chart showing empty rows per column - (bottom)
  plt.figure(figsize=(10.5, 4))
  labels = [f'Instruction ({empty_instruction_rows_processed:,})', f'Input ({empty_input_rows_processed:,})', f'Output ({empty_output_rows_processed:,})' ]
  values = [empty_instruction_rows_processed, empty_input_rows_processed, empty_output_rows_processed]
  mycolors = ["green", "blue", "orange"]
  plt.title('Processed - Missing Values per Column')
  plt.bar(labels, values, color=mycolors)
  plt.ylim(0)
  plt.show()
