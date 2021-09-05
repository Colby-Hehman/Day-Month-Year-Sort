'''
This is a very simple program. Just use the function on the amount of total_days you want sorted, and the day_sorter function will sort them into a gramatically accurate string. 
This was my first ever programming project and I did not even know how to use functions at the time, I have since reworked it to be easier for use
'''

def day_sorter(total_days):
    # Sorts total days into years, months, and days
    years_count_int = int(total_days / 365.25)
    months_count_int = int((total_days - years_count_int * 365.25) / 30.416666666)
    days_count_int = int(total_days - years_count_int * 365.25 - months_count_int * 30.416666666)
    # This converts the final numbers into strings for return ing
    years_count = str(years_count_int)
    months_count = str(months_count_int)
    days_count = str(days_count_int)
    # Prints the amount of years, months, and days it would take to fill container
    if years_count_int > 1:
        if months_count_int > 1:
            if days_count_int > 1:
                return (years_count + " years, " + months_count + " months, and "
                        + days_count + " days")
            elif days_count_int > 0:
                return (years_count + " years, " + months_count + " months, and "
                        + days_count + " day")
            else:
                return years_count + " years and " + months_count + " months"
        elif months_count_int > 0:
            if days_count_int > 1:
                return (years_count + " years, " + months_count + " month, and "
                        + days_count + " days")
            elif days_count_int > 0:
                return (years_count + " years, " + months_count + " month, and "
                        + days_count + " day")
            else:
                return years_count + " years and " + months_count + " month"
        else:
            if days_count_int > 1:
                return years_count + " years and " + days_count + " days"
            elif days_count_int > 0:
                return years_count + " years and " + days_count + " day"
            else:
                return years_count + " years "
    elif years_count_int > 0:
        if months_count_int > 1:
            if days_count_int > 1:
                return (years_count + " year, " + months_count + " months, and "
                        + days_count + " days")
            elif days_count_int > 0:
                return (years_count + " year, " + months_count + " months, and "
                        + days_count + " day")
            else:
                return years_count + " year and " + months_count + " months"
        elif months_count_int > 0:
            if days_count_int > 1:
                return (years_count + " year, " + months_count + " month, and "
                        + days_count + " days")
            elif days_count_int > 0:
                return (years_count + " year, " + months_count + " month, and "
                        + days_count + " day")
            else:
                return years_count + " year and " + months_count + " month"
        else:
            if days_count_int > 1:
                return years_count + " year and " + days_count + " days"
            elif days_count_int > 0:
                return years_count + " year and " + days_count + " day"
            else:
                return years_count + " year"
    else:
        if months_count_int > 1:
            if days_count_int > 1:
                return months_count + " months and " + days_count + " days"
            elif days_count_int > 0:
                return months_count + " months and " + days_count + " day"
            else:
                return months_count + " months"
        elif months_count_int > 0:
            if days_count_int > 1:
                return months_count + " month and " + days_count + " days"
            elif days_count_int > 0:
                return months_count + " month and " + days_count + " day"
            else:
                return months_count + " month"
        else:
            if days_count_int > 1:
                return days_count + " days"
            elif days_count_int > 0:
                return days_count + " day"
            else:
                return "0 days"

