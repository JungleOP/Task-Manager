from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return date_string
    except ValueError:
       raise ValueError("Date provided is not valid ")
