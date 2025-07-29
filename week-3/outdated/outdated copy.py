months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May":"05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    while True:
        d = input("Date: ").strip()
        if "/" in d:
            month, day, year = d.split("/")
            if int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        elif "," in d:
            month, day, year = d.split()
            day = day.replace(",","")  
            if int(day) <= 31:
                print(f"{year}-{months[month]}-{int(day):02}")
                break 
            
main()