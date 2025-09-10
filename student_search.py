def load_students(filename):
    students = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    student_id = parts[0]
                    last_name = parts[1]
                    first_name = parts[2]
                    major = parts[3]
                    gpa = parts[4]
                    students[student_id] = [last_name, first_name, major, gpa]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    return students


def search_by_last_name(students, last_name):
    found = False
    for student_id, info in students.items():
        if info[0].lower() == last_name.lower():
            print(f"{student_id},{info[0]},{info[1]},{info[2]},{info[3]}")
            found = True
    if not found:
        print(f"No students found with last name: {last_name}")


def search_by_major(students, major):
    found = False
    for student_id, info in students.items():
        if info[2].lower() == major.lower():
            print(f"{student_id},{info[0]},{info[1]},{info[2]},{info[3]}")
            found = True
    if not found:
        print(f"No students found in major: {major}")


def main():
    filename = "students.txt"
    students = load_students(filename)

    while True:
        print("\nChoose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            last_name = input("Enter last name to search for: ")
            search_by_last_name(students, last_name)
        elif choice == '2':
            major = input("Enter major to search for: ")
            search_by_major(students, major)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
