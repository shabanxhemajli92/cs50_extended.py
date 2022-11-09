class Student:

    def __init__(self, name, house,patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Grifyndor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "#" 
            case "Otter":
                return "?"
            case "Jack"          

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus=input("Patronus: ")
    return Student(name, house,patronus)


if __name__ == "__main__":
    main()
