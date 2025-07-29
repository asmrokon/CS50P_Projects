def main():
    time = input("What time is it? ").strip()
    if "a.m." not in time and "p.m." not in time:
        twentyfor_format(time)
    
    elif "a.m." in time:
        time = time.replace("a.m.", "")
        time = convert(time)
        if 7 <= time <= 8:
            print("breakfast time")
            
    elif "p.m." in time:
        time = time.replace("p.m.", "")
        time = pmconvert(time)
        if 12 <= time <= 13:
            print("lunch time")
        if 18 <= time <= 19:
            print("dinner time")
    

#24 format
def twentyfor_format(t1):
    t1 = convert(t1)
    if 7 <= t1 <= 8:
        print("breakfast time")
    elif 12 <= t1 <= 13:
        print("lunch time")
    elif 18 <= t1 <= 19:
        print("dinner time")

#time converter
def convert(t2):
    t2 = t2.strip().split(":")
    hours = float(t2[0])
    mins = float(t2[1])
    mins = mins / 60
    t2 = hours + mins
    return t2 

#pm time converter
def pmconvert(t3):
    t3 = t3.strip().split(":")
    hours = float(t3[0])
    mins = float(t3[1])
    mins = mins / 60
    t2 = hours + mins
    return t2 

main()
