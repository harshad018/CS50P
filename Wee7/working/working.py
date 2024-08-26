import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matched = re.search(r"((?:[1-9]|1[0-2]):[0-5][0-9]\s(?:AM|PM))\sto\s((?:[1-9]|1[0-2]):[0-5][0-9]\s(?:AM|PM))", s)
    if matched:
        start_time = matched.group(1).split(" ")
        end_time = matched.group(2).split(" ")

        if "PM" in start_time[1]:
            hour, minute = start_time[0].split(":")
            hour = int(hour) + 12  # Calculate the hour
            hour = f"{hour:02}"  # Format the hour with leading zeros
            return (f"{hour}:{minute} to {end_time[0]}")
        else:
            hour, minute = end_time[0].split(":")
            hour = int(hour) + 12
            hour = f"{hour:02}"
            return (f"{start_time[0]} to {hour}:{minute}")
    else:
        return False

if __name__ == "__main__":
    main()
