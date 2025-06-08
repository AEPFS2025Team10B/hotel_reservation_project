from datetime import datetime, date

def calculate_age(birthday: date) -> int:
    today = datetime.now().date() # Get only the date part for comparison
    age = today.year - birthday.year
    # Adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age 