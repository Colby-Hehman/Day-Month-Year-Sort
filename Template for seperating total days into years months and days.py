# Data to enter
total_days = 368
start_phrase = "It will take you "
end_phrase = "to finish writing this program!"
# Sorts total days into years, months, and days
years_count_int = int(total_days / 365.25)
months_count_int = int((total_days - years_count_int * 365.25) / 30.416666666)
days_count_int = int(total_days - years_count_int * 365.25 - months_count_int *  30.416666666)
# This converts the final numbers into strings for printing
years_count = str(years_count_int)
months_count = str(months_count_int)
days_count = str(days_count_int)
# Prints the amount of years, months, and days it would take to fill container
if years_count_int > 1:
    if months_count_int > 1:
        if days_count_int > 1:
            print(start_phrase + years_count + " years, " + months_count + " months, and "
                  + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + years_count + " years, " + months_count + " months, and "
                  + days_count + " day " + end_phrase)
        else:
            print(start_phrase + years_count + " years and " + months_count + " months " + end_phrase)
    elif months_count_int > 0:
        if days_count_int > 1:
            print(start_phrase + years_count + " years, " + months_count + " month, and "
                  + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + years_count + " years, " + months_count + " month, and "
                  + days_count + " day " + end_phrase)
        else:
            print(start_phrase + years_count + " years and " + months_count + " month " + end_phrase)
    else:
        if days_count_int > 1:
            print(start_phrase + years_count + " years and " + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + years_count + " years and " + days_count + " day " + end_phrase)
        else:
            print(start_phrase + years_count + " years " + end_phrase)
elif years_count_int > 0:
    if months_count_int > 1:
        if days_count_int > 1:
            print(start_phrase + years_count + " year, " + months_count + " months, and "
                  + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + years_count + " year, " + months_count + " months, and "
                  + days_count + " day " + end_phrase)
        else:
            print(start_phrase + years_count + " year and " + months_count + " months " + end_phrase)
    elif months_count_int > 0:
        if days_count_int > 1:
            print(start_phrase + years_count + " year, " + months_count + " month, and "
                  + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + years_count + " year, " + months_count + " month, and "
                  + days_count + " day " + end_phrase)
        else:
            print(start_phrase + years_count + " year and " + months_count + " month " + end_phrase)
    else:
        if days_count_int > 1:
            print(start_phrase + years_count + " year and " + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + years_count + " year and " + days_count + " day " + end_phrase)
        else:
            print(start_phrase + years_count + " year " + end_phrase)
else:
    if months_count_int > 1:
        if days_count_int > 1:
            print(start_phrase + months_count + " months and " + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + months_count + " months and " + days_count + " day " + end_phrase)
        else:
            print(start_phrase + months_count + " months " + end_phrase)
    elif months_count_int > 0:
        if days_count_int > 1:
            print(start_phrase + months_count + " month and " + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + months_count + " month and " + days_count + " day " + end_phrase)
        else:
            print(start_phrase + months_count + " month " + end_phrase)
    else:
        if days_count_int > 1:
            print(start_phrase + days_count + " days " + end_phrase)
        elif days_count_int > 0:
            print(start_phrase + days_count + " day " + end_phrase)
        else:
            print(start_phrase + " 0 days " + end_phrase)