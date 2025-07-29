import re
import sys  # noqa: F401


def main():
    try:
        print(convert(input("Hours: ")))
    except AttributeError:
        raise ValueError


def convert(s):
    time_dict = {}

    time = re.search(
        r"(?P<t1>\d+):?(?P<t2>[0-5][0-9])? (?P<f1>\w+) to (?P<t3>\d+):?(?P<t4>[0-5][0-9])? (?P<f2>\w+)",
        s,
    )
    if time.group("f1") == "PM":  # type: ignore
        if time.group("t2"):  # type: ignore
            hour_1 = int(time.group("t1")) + 12  # type: ignore
            min_1 = int(time.group("t2"))  # type: ignore
            time_1 = f"{hour_1:02}:{min_1:02}"
            time_dict["time_1"] = time_1

        elif not time.group("t2"):  # type: ignore
            hour_1 = int(time.group("t1")) + 12  # type: ignore
            time_1 = f"{hour_1:02}:00"
            time_dict["time_1"] = time_1

    elif time.group("f1") == "AM":  # type: ignore
        hour_1 = int(time.group("t1"))  # type: ignore
        if hour_1 == 12:
            hour_1 = 0
            if time.group("t2"):  # type: ignore
                min_1 = int(time.group("t2"))  # type: ignore
                time_1 = f"{hour_1:02}:{min_1:02}"
                time_dict["time_1"] = time_1

            elif not time.group("t2"):  # type: ignore
                time_1 = f"{hour_1:02}:00"
                time_dict["time_1"] = time_1

        else:
            if time.group("t2"):  # type: ignore
                min_1 = int(time.group("t2"))  # type: ignore
                time_1 = f"{hour_1:02}:{min_1:02}"
                time_dict["time_1"] = time_1

            elif not time.group("t2"):  # type: ignore
                time_1 = f"{hour_1:02}:00"
                time_dict["time_1"] = time_1

    if time.group("f2") == "PM":  # type: ignore
        if time.group("t3") == "12":  # type: ignore
            if time.group("t4"):  # type: ignore
                hour_2 = int(time.group("t3"))  # type: ignore
                min_2 = int(time.group("t4"))  # type: ignore
                time_2 = f"{hour_2:02}:{min_2:02}"
                time_dict["time_2"] = time_2
            elif not time.group("t2"):  # type: ignore
                hour_2 = int(time.group("t3"))  # type: ignore
                time_2 = f"{hour_2:02}:00"
                time_dict["time_2"] = time_2
        else:
            if time.group("t4"):  # type: ignore
                hour_2 = int(time.group("t3")) + 12  # type: ignore
                min_2 = int(time.group("t4"))  # type: ignore
                time_2 = f"{hour_2:02}:{min_2:02}"
                time_dict["time_2"] = time_2
            elif not time.group("t2"):  # type: ignore
                hour_2 = int(time.group("t3")) + 12  # type: ignore
                time_2 = f"{hour_2:02}:00"
                time_dict["time_2"] = time_2

    elif time.group("f2") == "AM":  # type: ignore
        hour_2 = int(time.group("t3"))  # type: ignore
        if hour_2 == 12:
            hour_2 = 0
            if time.group("t4"):  # type: ignore
                min_2 = int(time.group("t4"))  # type: ignore
                if min_2 <= 59:
                    time_2 = f"{hour_2:02}:{min_2:02}"
                    time_dict["time_2"] = time_2
                else:
                    raise ValueError
            elif not time.group("t4"):  # type: ignore
                time_2 = f"{hour_2:02}:00"
                time_dict["time_2"] = time_2

        else:
            if time.group("t4"):  # type: ignore
                min_2 = int(time.group("t4"))  # type: ignore
                if min_2 <= 59:
                    time_2 = f"{hour_2:02}:{min_2:02}"
                    time_dict["time_2"] = time_2
                else:
                    raise ValueError
            elif not time.group("t4"):  # type: ignore
                time_2 = f"{hour_2:02}:00"
                time_dict["time_2"] = time_2

    return f"{time_dict['time_1']} to {time_dict['time_2']}"


if __name__ == "__main__":
    main()
