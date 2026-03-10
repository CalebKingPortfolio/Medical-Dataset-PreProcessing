# MISSING ROWS UNPROCESSED ANALYSIS
def analyze_missing_rows_unprocessed():

  # line chart showing dataset size - (left)
  x_1 = np.arange(unprocessed_missing_ds)
  plt.figure(figsize=(9, 4)) # sets size of line charts
  plt.subplot(1, 2, 1) # position of linechart
  plt.plot(x_1, x_1, color='blue', label=f"Rows {unprocessed_missing_ds:,}")
  plt.title(f"Unprocessed - Dataset Size")
  plt.legend()

  # bar chart showing missing rows - (right)
  plt.subplot(1, 2, 2)
  labels = [f'Empty Rows ({missing_row_count_unprocessed:,})']
  values = [missing_row_count_unprocessed]
  mycolors = ["green"]
  plt.bar(labels, values, color=mycolors)
  plt.title('Unprocessed - Missing Rows')
  plt.tight_layout()
  plt.show()

  #  bar chart showing empty rows per column - (bottom)
  plt.figure(figsize=(10.5, 4))
  labels = [f'Instruction ({empty_instruction_rows_unprocessed:,})', f'Input ({empty_input_rows_unprocessed:,})', f'Output ({empty_output_rows_unprocessed:,})' ]
  values = [empty_instruction_rows_unprocessed, empty_input_rows_unprocessed, empty_output_rows_unprocessed]
  mycolors = ["green", "blue", "orange"]
  plt.title('Unprocessed - Missing Values per Column')
  plt.bar(labels, values, color=mycolors)
  plt.show()
