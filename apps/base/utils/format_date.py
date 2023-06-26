from datetime import datetime

def format_date(date):
    date = datetime.strptime(date, "%d/%m/%Y")
    date = f"{date.year}-{date.month}-{date.day}"
    return date