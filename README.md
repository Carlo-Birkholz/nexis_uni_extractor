# Function

Convert doc or rtf files from nexis into formatted csv.

## Usage

1. the transformer module contains convert_files_to_plain_text function,
parameters: input and output file path
do: convert rtf/docx to plain text

2. helpers module contains 1> format_date(which format time from english, french, german, italian and spanish to yyyy/mm/dd)
2> process_string(determine if the article contains images, return 1/0 and return body part of the article)

3. parser module contains parser, takes input_path and output_path as parameter, input path should be a txt file that you wanna parse, output file should be a csv file

4. pipeline module contains convert_files_to_csv, a pipeline function, it takes input_folder and output_folder as parameters, it convert a folder of docx files to a folder of csv files. The converted csv file conatins features of article title, publisher, publish_date, edition, section, length, byline, body and graphic.

5. To use the pipeline:
import convert_files_to_csv from pipeline, set input_folder and output_folder parameters, the input folder conatins docx or rtf files.
in E:\github\nexis_uni_extractor\test\more_data before:
1.DOCX
2.DOCX. 
In E:\github\nexis_uni_extractor\test\more_data after:
1.csv
2.csv
1.txt
2.txt
1.DOCX
2.DOCX
(in total 4 new files are generated)


```python
from pipeline import convert_files_to_csv

input_folder = 'E:\\github\\nexis_uni_extractor\\test\\more_data'
output_folder = 'E:\\github\\nexis_uni_extractor\\test\\more_data'
convert_files_to_csv(input_folder, output_folder, language='french')
```


6. py or ipynb files with name starting with test are just for test purposes

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT License

Copyright (c) 2023 zhong3401

