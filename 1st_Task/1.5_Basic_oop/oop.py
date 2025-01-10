class Student:
    def __init__ (self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# Example usage
if __name__ == "__main__":
    name= input("Enter the name of the student:")
    age = int(input("Enter the age of the student:"))
    grades = list(map(float,input("Enter the grades of the student (comma ',' seprated):").split(',')))
    # Create a Student object
    student = Student(name, age,grades)

    # Display student details
    student.display()

    # Calculate and display average grade
    average_grade = student.average_grade()
    print(f"Average Grade: {average_grade:}")
