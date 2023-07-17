import re



def main():
    print(convert(input("Hours: ")))


def convert(s):

    m = re.search("(([\d][\d]*):*([\d][\d])* (AM|PM) to ([\d][\d]*):*([\d][\d])* (AM|PM))",s)
    if m:
        start_hour = int(m.group(2))
        finish_hour = int(m.group(5))
        if m.group(4) == "PM":
            start_hour = start_hour + 12
            if start_hour > 23:
                raise ValueError
        if m.group(7) == "PM":
            finish_hour = finish_hour + 12
            if finish_hour > 23:
                raise ValueError

        #if threr are minutes on input
        if m.group(3) and m.group(6):
            start_minute = int(m.group(3))
            finish_minute = int(m.group(6))
            if start_minute >59:
                raise ValueError
            if finish_minute > 59:
                raise ValueError
            return (f"{start_hour:02}:{start_minute:02} to {finish_hour:02}:{finish_minute:02}")

            #if there are no minutes in input
        return (f"{start_hour:02}:00 to {finish_hour:02}:00")


    else:
        raise ValueError








if __name__ == "__main__":
    main()