import json
import os

text = ("Compozent_Task/1st_Task/1.4_Data_Structures/student.txt")


# Function to load student data from the file
def load_std():
    if os.path.exists(text):  
        try:
            with open(text, "r") as file:
                return json.load(file)  
        except json.JSONDecodeError:
            return {}  
    else:
        return {}  #

# Function to save student data to the file
def save_std(student):
    with open(text, "w") as file:
        json.dump(student, file, indent=2)  

# Function to add a new student
def std_add():
    student = load_std()  
    std_id = input("Enter the student id: ")
    if std_id in student:
        print("This ID already exists.")
        return
    name = input("Enter the Name of the student: ")
    age = int(input("Enter the age of the student: "))
    grades = list(map(float, input("Enter the grades of the student (separated by comma): ").split(',')))  
    student[std_id] = {"name": name, "age": age, "grades": grades}  
    save_std(student)  
    print("Student added successfully!")

# Function to display all students
def show_std():
    student = load_std()  
    if not student:
        print("No student records found.")
        return
    for std_id, details in student.items():
        print(f"ID: {std_id}, Name: {details['name']}, Age: {details['age']}, Grades: {details['grades']}")

def std_delete():
    student = load_std()
    std_id = input("Enter the student id to delete:")
    if std_id in student:
        del student[std_id]
        save_std(student)
        print("Id deleted sucessfully")

def std_update():
    student = load_std()
    std_id = input("Enter the id tha you want to update:")  
    if std_id not in student:
        print("Id not found, pls enter valid Id")
        return
    print("Student id found")
    name= input(f"enter the new name for the student ,Current: {student[std_id]['name']}:")
    age = int(input(f"enter the new age for the student,Current:{student[std_id]['age']}:"))
    grades = list(map(float, input(f"Enter new grades for the student (current: {student[std_id]['grades']}): ").split(',')))  # Convert grades to float
    
    student[std_id]= {"name":name,"age":age,"grades":grades}
    save_std(student)
    print("Student details are updated")





# Main menu 
def main():
    while True:
        print("\n--- Student Records System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Delete")
        print("4. Update")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            std_add()
        elif choice == '2':
            show_std()
        elif choice == '3':
            std_delete()   
        elif choice == '4':
            std_update()     
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
