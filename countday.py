from datetime import date

def count_days(d):
    today = date.today()
    
    if d < today:
        return "The day is in the past!"
    elif d==today:
        return"today is the day!"
    else:
        diff = (d - today).days
        return f"{diff} days"
    
print(count_days(date(2025,12,31)))
print(count_days(date.today()))
print(count_days(date(2020,1,1)))