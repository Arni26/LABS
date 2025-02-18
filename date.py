from datetime import datetime, timedelta

#Write a Python program to subtract five days from current date.
def five():
    date = datetime.now()
    new_date = date - timedelta(days=5)
    return new_date.strftime("%Y-%m-%d")

print("Five days ago:", five())

print()

#Write a Python program to print yesterday, today, tomorrow.
def dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
    print("Today:", today.strftime("%Y-%m-%d"))
    print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

dates()
print()

#Write a Python program to drop microseconds from datetime.
def micro():
    date0 = datetime.now()
    return date0.strftime("%Y-%m-%d %H:%M:%S")

print(micro())
print()

#Write a Python program to calculate two date difference in seconds.
def date_diff(date1, date2):
    dif = date2 - date1
    return dif.total_seconds()

date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 6, 14, 30, 0)

print("Difference in seconds:", date_diff(date1, date2))
