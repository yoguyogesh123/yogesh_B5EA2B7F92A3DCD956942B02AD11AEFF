class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def   sort_students(student_list):
#sort the list of students in descending order of cgpa
  sorted_students = sorted(student_list,
      key = lambda student: student.cgpa,
      reverse = True)
  return sorted_students
#example usage:
students = [
     student("akash","22BCE1230",7.8),
     student("kesav","22BCE1235",8.9),
     student("vijay","22BCE1241",9.1),
     student("yogesh","22BCE1243",8.5)]
sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, roll number: {},cgpa: {}".format (student.name, student.roll_number,student.cgpa))