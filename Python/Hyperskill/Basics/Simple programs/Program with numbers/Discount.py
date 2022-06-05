age = int(input())  # age variable attached to user input
discount = (age < 21) or (age >= 65)  # if not age less than 21 or at least 65 years and older
if not discount:  # if age less than 21 or at least 65 years and older then give discount, otherwise do not give discount
    print(False)
else:
    print(True or False)
