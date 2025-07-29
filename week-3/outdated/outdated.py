months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def main():
    while True:
        d = input("Date: ").strip()
        for month in months.keys():
            if month in d:
                month, day, year = d.split()
                if "," in day:
                    day = day.replace(",", "")
                    print(f"{year}-{months[month]}-{int(day):02}")
                    return True
                else:
                    continue
        else:
            d = d.split("/")
            print(f"{d[2]}-{int(d[0]):02}-{int(d[1]):02}")
            break


main()
