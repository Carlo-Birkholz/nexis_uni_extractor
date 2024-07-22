from pipeline import convert_files_to_csv
import os

#input_folder = 'C:\\Users\\CMB\\PycharmProjects\\nexis_uni_extractor\\test\\more_data'
#output_folder = 'C:\\Users\\CMB\\PycharmProjects\\nexis_uni_extractor\\test\\more_data'

input_folder = ('C:\\Users\\CMB\\Dropbox\\PC\\Documents\\Projects\\17_ECB\\1_Data\\Newspapers\\'
                '_countries\\Germany\\BILD Bund\\')
output_folder = ('C:\\Users\\CMB\\Dropbox\\PC\\Documents\\Projects\\17_ECB\\1_Data\\Newspapers\\'
                '_countries\\Germany\\BILD Bund\\')

convert_files_to_csv(input_folder, output_folder, language='german')

