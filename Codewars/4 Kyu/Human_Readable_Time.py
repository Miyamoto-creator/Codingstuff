import timeit as t


def format_duration(seconds):
    sec, minute, hour, day, year = 0, 0, 0, 0, 0
    time = seconds

    while True:
        if time >= 365 * 24 * 60 * 60:
            year += 1
            time -= 365 * 24 * 60 * 60

        elif time >= 24 * 60 * 60:
            day += 1
            time -= 24 * 60 * 60

        elif time >= 60 * 60:
            hour += 1
            time -= 60 * 60

        elif time >= 60:
            minute += 1
            time -= 60

        elif time >= 1:
            sec += 1
            time -= 1

        elif time == 0:
            break

    time_lst = [year, day, hour, minute, sec]
    word_lst = ["year", "day", "hour", "minute", "second"]
    lst = []

    for i, n in enumerate(time_lst):
        if n > 1:
            lst.append(f"{str(n)} {word_lst[i]}s")

        elif n > 0:
            lst.append(f"{str(n)} " + word_lst[i])

    if len(lst) >= 3:
        half = [f"{lst[i]}, " for i in range(len(lst) - 2)]
        return "".join(half) + f"{lst[len(lst) - 2]} and {lst[len(lst) - 1]}"

    elif len(lst) == 2:
        return "".join(f"{lst[0]} and {lst[1]}")

    elif len(lst) == 1:
        return lst[0]

    elif len(lst) == 0:
        return 'now'


print("Run time:", t.timeit(lambda: format_duration(3662), number=10000))
# print("Actual output: ",format_duration(3662))
# print("Expected output: 1 hour, 1 minute and 2 seconds")
print("Actual output: ", format_duration(132030240))
print("Expected output: 4 years, 68 days, 3 hours and 4 minutes")
