import datetime


class CheckDate:
    """This class checks users input dates."""
    def __init__(self, d1, d2):
        """This method initializes."""
        self.day1 = d1.split('/')[0]
        self.day2 = d2.split('/')[0]
        self.month1 = d1.split('/')[1]
        self.month2 = d2.split('/')[1]
        self.year1 = d1.split('/')[2]
        self.year2 = d2.split('/')[2]

    def check_date(self):
        """This method checks is user input is date or in correct format
        dd/mm/yy"."""
        correct = True
        try:
            datetime.datetime(int(self.year1), int(self.month1), int(self.day1))
            datetime.datetime(int(self.year2), int(self.month2), int(self.day2))
        except ValueError:
            correct = False
        if correct:
            return True
        else:
            return False

    def check_two(self):
        """This method checks if two date are relevant and not too long
        or too short period between them."""
        if not self.check_date():
            return "Incorrect date format. Please, try again."
        curr_year = str(datetime.date.today()).split()[0].replace("-", "/")[2:4]
        curr_month = str(datetime.date.today()).split()[0].\
        replace("-", "/")[5:7]
        curr_date = str(datetime.date.today()).split()[0].\
        replace("-", "/")[8:10]
        if self.year1 != curr_year or self.year2 != curr_year:
            return "You can plan your trip by the end of this year. \
Aviaticket for next year will be avaible later"
        time1 = datetime.date(year = int("20" + self.year1), \
        month = int(self.month1), day = int(self.day1))
        time2 = datetime.date(year = int("20" + self.year2), \
        month = int(self.month2), day = int(self.day2))
        if time1 <= datetime.date.today() or time2 <= datetime.date.today():
            return "Your date Incorrect. Please, try again."
        final_time = time2 - time1
        total_days = int(str(final_time).split()[0])
        if 0 < total_days < 3:
            return "Interval between date too short."
        if total_days <= 0:
            return "Incorrect date. Please, try again."
        elif total_days > 21:
            return "Interval between your date too large."
        else:
            return True
