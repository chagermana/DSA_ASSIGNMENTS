
class DateCalculator:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month.strip().lower()
        self.year = year

        # Adjust months and year for Zeller's formula
        if self.month == "january":
            self.month_number = 13
            self.year -= 1
        elif self.month == "february":
            self.month_number = 14
            self.year -= 1
        else:
            # Mapping other months to numbers
            month_map = {
                "march": 3, "april": 4, "may": 5, "june": 6,
                "july": 7, "august": 8, "september": 9,
                "october": 10, "november": 11, "december": 12
            }
            self.month_number = month_map.get(self.month, 0)

    def calculate_day(self):
        q = self.day
        m = self.month_number
        Y = self.year
        K = Y % 100
        J = Y // 100

        # Zeller's Congruence formula
        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

# Example usage:
day = int(input("Enter the day: "))
month = input("Enter the month: ")
year = int(input("Enter the year: "))

calc = DateCalculator(day, month, year)
print("The day of the week is:", calc.calculate_day())
