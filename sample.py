from mongoengine import *
import students_schema
import datetime

def main():
	connect('importedDB')

	students = students_schema.StudentSchema.objects()
	for student in students:
		students_schema.printStudentInfo(student)

if __name__ == "__main__":
	main()