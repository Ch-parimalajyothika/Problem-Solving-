def day_name(day):
    days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",
            5:"Friday", 6:"Saturday", 7:"Sunday"}
    return days.get(day, "Invalid day number")

day = int(input("Enter day number (1-7): "))
print(day_name(day))
