#  define variables hour, minutes and seconds attached to user input
hour_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
# combine the 3 time variables into one big time variable and apply appropriate numbers
time_1 = (hour_1 * 3600) + (minutes_1 * 60) + (seconds_1 * 1)
hour_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
# rinse and repeat
time_2 = (hour_2 * 3600) + (minutes_2 * 60) + (seconds_2 * 1)
results = time_2 - time_1
# print results
print(results)
