class Student:
  def __init__(self,name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade
  def display_info(self):
    print("Name of the student is :",self.name)
    print("Age of the student is :",self.age)
    print("Grade of the student is :",self.grade)
  
# student = Student('Aditya',21,'C')

# n = input("Enter your name")
# a= int(input("Enter your age"))
# g = input("enter your grade")
# student = Student(n,a,g)

students = []
while True:
  print("1. Add Student")
  print("2. View All Students")
  print("3. Exit")
  choose = input("Enter your choice: ")
  if choose == '1':
    n = input("Enter your name: ")
    a= int(input("Enter your age: "))
    g = input("enter your grade: ")
    student = Student(n,a,g)
    students.append(student)
    student.display_info()
  elif choose == '2':
    if students:
      print("students info: ")
      for i,student in enumerate(students):
        print(f"{i+1}.{student.__dict__}")
    else:
      print("No students added yet.")
  

    
  elif choose =='3':
    print("Thanks!")
    break
  else:
    print("Please select either 1,2 or 3")
    

    
