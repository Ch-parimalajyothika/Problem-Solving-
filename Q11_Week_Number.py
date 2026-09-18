def week_day(week):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[week - 1] if 1 <= week <= 7 else "Invalid week number"

week = int(input("Enter week number (1-7): "))
print(week_day(week))
