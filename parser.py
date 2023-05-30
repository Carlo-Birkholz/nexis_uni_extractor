import re
import json
import pandas as pd
from dateutil import parser
from helpers import process_string, format_date

def parser(input_path, output_path, language='germany'):
  # define features of the article
  titles = []
  publishers = []
  publish_dates = []
  editions = []
  sections = []
  lengths = []
  bylines = []
  bodys = []
  graphics = []

  # Read the contents of the file
  with open(input_path, 'r', encoding='utf-8') as file:
      content = file.read()

  # Define the pattern of one article
  pattern = r"(?s)(.*?)End of Document"

  # Find all articles
  matches = re.findall(pattern, content)

  for article in matches:
    article = article.replace('[]', '', 1).strip()

    # get title,publisher
    title = article.split('\n\n', 1)[0].replace('\n', ' ')
    publisher = article.split('\n\n', 1)[1].split('\n\n',1)[0]
    # get publish date
    date_str = article.split('\n\n', 1)[1].split('\n\n',1)[1].split('\n\n',1)[0]
    publish_date = format_date(date_str, language)
    # get edition
    edition_str = article.split('\n\n',4)[3]
    if "edition" in edition_str.lower():
        pass  # No changes needed, edition_str remains the same
    else:
        edition_str = "NaN"
    
    # match section
    pattern_section = r"Section:(.*?)\n"
    section_matches = re.findall(pattern_section, article, re.DOTALL)
    section = section_matches[0] if section_matches else "NaN"
    
    # match length
    pattern_length = r"Length:(.*?)\n"
    matches_lengths = re.findall(pattern_length, article, re.DOTALL)[0]
    length = int(matches_lengths.split()[0])
    
    # match byline
    pattern_byline = r"Byline:(.*?)\n"
    byline_matches = re.findall(pattern_byline, article, re.DOTALL)
    byline = byline_matches[0] if byline_matches else "NaN"
    
    # match body
    pattern_body = r'Body(.*?)Load-Date'
    match = re.findall(pattern_body, article, re.DOTALL)[0].strip()
    body = match.replace("[image]", '').replace("\n", " ").strip()
    # match graph
    graphic, body = process_string(body)
    
    titles.append(title)
    publishers.append(publisher)
    publish_dates.append(publish_date)
    editions.append(edition_str)
    sections.append(section)
    lengths.append(length)
    bylines.append(byline)
    bodys.append(body)
    graphics.append(graphic)

  data = {'title': titles, 'publisher': publishers, 'publish_date':publish_dates, 'edition':editions, 'section':sections, 'length':lengths, 'byline':bylines, 'body':bodys, 'graphic':graphics}

  df = pd.DataFrame(data)

  df.to_csv(output_path, index=False, encoding='utf-8')
