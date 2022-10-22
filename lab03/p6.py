def next_day(y, m, d):

# cases:
    # odd month and date is 30 (add month, date 1)
    # even month not 2 and date is 31 (add month, date 1)
    # month is 12 and date 31 (add year, date 1, month 1)
    # month 2 and date is 28 and is a leap year (date 29, month 2)
    # month 2 and date is 29 (date 1, month 3)
    # month 2 and date is 28 and is not a leap year (date 1, month 3)
