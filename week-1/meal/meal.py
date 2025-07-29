def main():
    t = input("What time is it? ")
    t = convert(t)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    time = time.strip().split(":")
    hours = float(time[0])
    mins = float(time[1])
    mins = mins / 60
    time = hours + mins
    return time 

if __name__ == "__main__":
    main()
