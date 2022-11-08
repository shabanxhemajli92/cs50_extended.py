import pdb

pdb.set_trace()


def main():
    student = get_Person()
    print(f"{student['name']} {student['Last Name']} was born on {student['birth date']} in {student['where were you born']} and lives in {student['Where do you live']}")


def get_Person():

    name = input("Name: ")
    last_name = input("Last Name: ")
    Birth_date = input("Date of birth: ")
    Birth_place = input("What is your birth place: ")
    house = input("Where do you live: ")
    return {"name": name, "Last Name": last_name, "birth date": Birth_date, "where were you born": Birth_place, "Where do you live": house}


if __name__ == "__main__":
    main()
