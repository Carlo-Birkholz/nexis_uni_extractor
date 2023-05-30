from parser import parser
from transformer import convert_files_to_plain_text
import os

def convert_files_to_csv(input_folder, output_folder, language):
  
  convert_files_to_plain_text(input_folder, input_folder)

  # Create the output folder if it doesn't exist
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # Iterate over the files in the input folder
  for file_name in os.listdir(input_folder):
      # Build the input and output file paths
      input_file = os.path.join(input_folder, file_name)
      output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.csv')

      # Determine the file extension
      _, file_extension = os.path.splitext(file_name)
      file_extension = file_extension.lower()

      if file_extension == '.txt':
          # Convert txt to csv
          parser(input_file, output_file, language)
          
          print(f"Converted {file_name} to csv")
  print("Conversion completed")


