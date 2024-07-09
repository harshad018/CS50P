def main():
    #take user input
    time = input("What time it is? ")
    mealtime(convert(time))


def convert(time):
    hour,nothing,minute = time.rpartition(":")
    hour = float(hour)
    minute = float( float(minute)/60)
    time = float(hour + minute)
    return time


def mealtime(time):
    if 7.00 <= time <=8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


if __name__ == "__main__":
    main()

