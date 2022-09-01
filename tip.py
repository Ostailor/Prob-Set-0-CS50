def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(amount):
    return float(amount.replace("$", ""))


def percent_to_float(percentage):
    return float(percentage.replace("%", "")) / 100


main()
