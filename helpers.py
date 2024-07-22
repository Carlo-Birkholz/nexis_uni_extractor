from datetime import datetime
from dateutil import parser

def format_date(date_string, language):
    # Define month mappings for each language
    month_mappings = {
        'french': {
            'janvier': 'January',
            'février': 'February',
            'mars': 'March',
            'avril': 'April',
            'mai': 'May',
            'juin': 'June',
            'juillet': 'July',
            'août': 'August',
            'septembre': 'September',
            'octobre': 'October',
            'novembre': 'November',
            'décembre': 'December'
        },
        'italian': {
            'gennaio': 'January',
            'febbraio': 'February',
            'marzo': 'March',
            'aprile': 'April',
            'maggio': 'May',
            'giugno': 'June',
            'luglio': 'July',
            'agosto': 'August',
            'settembre': 'September',
            'ottobre': 'October',
            'novembre': 'November',
            'dicembre': 'December'
        },
        'german': {
            'januar': 'January',
            'februar': 'February',
            'märz': 'March',
            'maerz': 'March',
            'april': 'April',
            'mai': 'May',
            'juni': 'June',
            'juli': 'July',
            'august': 'August',
            'september': 'September',
            'oktober': 'October',
            'november': 'November',
            'dezember': 'December'
        },
        'spanish': {
            'enero': 'January',
            'febrero': 'February',
            'marzo': 'March',
            'abril': 'April',
            'mayo': 'May',
            'junio': 'June',
            'julio': 'July',
            'agosto': 'August',
            'septiembre': 'September',
            'octubre': 'October',
            'noviembre': 'November',
            'diciembre': 'December'
        }
    }

    # Get the month mapping based on the language
    month_mapping = month_mappings.get(language)

    if not month_mapping:
        return "Unsupported language"

    for month, month_translation in month_mapping.items():
        date_string = date_string.lower().replace(month, month_translation)

    try:
        # Parse the date using dateutil.parser.parse
        date = parser.parse(date_string, fuzzy=True).date()

        # Convert the date to the desired format "yyyy/mm/dd"
        formatted_date = date.strftime('%Y/%m/%d')
        return formatted_date
    except ValueError:
        return "Invalid date format"

def process_string(input_string):
    if input_string is None:
        return 0, None
        
    # Find the index of "[]" in the input string
    index_brackets = input_string.find("[]")

    # Find the index of "Graphic" in the input string
    index_graphic = input_string.find("Graphic")
    
    # Assign the index with a non-negative value to the variable 'index'
    if index_brackets != -1:
        index = index_brackets
    elif index_graphic != -1:
        index = index_graphic
    else:
        index = -1  # No match found

    if index != -1:
        # Discard all characters starting from "Graphic"
        input_string = input_string[:index].strip()
        return 1, input_string
    else:
        return 0, input_string
