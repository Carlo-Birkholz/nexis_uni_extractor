import os
import subprocess

def convert_files_to_plain_text(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the files in the input folder
    for file_name in os.listdir(input_folder):
        # Build the input and output file paths
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.txt')

        # Determine the file extension
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()

        if file_extension == '.rtf':
            # Run the pandoc command to convert RTF to plain text
            pandoc_cmd = ["pandoc", "--from=rtf", "--to=plain", "-s", input_file, "-o", output_file]
            subprocess.run(pandoc_cmd)
            print(f"Converted {file_name} to plain text")

        elif file_extension == '.docx':
            # Run the pandoc command to convert DOCX to plain text
            pandoc_cmd = ["pandoc", "--from=docx", "--to=plain", "-s", input_file, "-o", output_file]
            subprocess.run(pandoc_cmd)
            print(f"Converted {file_name} to plain text")

    print("Conversion completed")