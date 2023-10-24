import re
from datetime import datetime

def normalize_dates(text):
    date_patterns = [
        r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY
        r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
        r'\b(\d{1,2})(?:st|nd|rd|th)? (?:January|February|March|April|May|June|July|August|September|October|November|December)[a-z]* (\d{4})\b'  # 25th February 2023
    ]

    for pattern in date_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            original_date = match.group()
            try:
                if "/" in original_date:
                    date_obj = datetime.strptime(original_date, '%m/%d/%Y')
                elif "-" in original_date:
                    date_obj = datetime.strptime(original_date, '%Y-%m-%d')
                else:
                    date_obj = datetime.strptime(original_date, '%d %B %Y')
                normalized_date = date_obj.strftime('%Y-%m-%d')
                text = text.replace(original_date, normalized_date)
            except ValueError:
                # Handle invalid dates here
                pass

    return text

# Example text with date variations
text_with_dates = "On 02/25/2023, the event took place. It was also mentioned on 25th February 2023 and 2023-02-25."

# Normalize the dates in the text
normalized_text = normalize_dates(text_with_dates)

print(normalized_text)
