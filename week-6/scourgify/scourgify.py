import csv
import sys

students = []


def main():
    try:
        if len(sys.argv) == 3:
            if ".csv" in sys.argv[1]:
                try:
                    with open(f"{sys.argv[1]}", "r") as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            last_name, first_name = row["name"].split(",")
                            student = {
                                "first": first_name.strip(),
                                "last": last_name.strip(),
                                "house": row["house"].strip(),
                            }
                            students.append(student)
                    make_file(sys.argv[2])
                except FileNotFoundError:
                    sys.exit(f"Could not read {sys.argv[1]}")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            raise IndexError
    except IndexError:
        sys.exit("Too few command-line arguments")


def make_file(file):
    with open(f"{file}", "w", newline="") as f:
        fields = ["first", "last", "house"]
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()
        for row in students:
            writer.writerow(row)
    f.close()


main()
