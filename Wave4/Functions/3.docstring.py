def readable_timedelta(days):
    # insert your docstring here
    """Calculate the number of weeks equal to a certain nbet of days. 
    INPUT:
        days: int. The number of days to be checked. 
    OUTPUT:
        weeks: days // 7. The equivalent number of weeks without remainder
        remainder: days % 7. the remainder after dividing days by 7
        """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)