from datetime import date

def calendar_week(d):
  
    year, month, day = map(int, d.split("-"))
    dt = date(year, month, day)
    return dt.isocalendar().week

print(calendar_week("2023-01-01"))
print(calendar_week("2023-01-02"))
print(calendar_week("2024-02-14"))
print(calendar_week("2025-01-01"))