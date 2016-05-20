from mongoengine import *
import students_schema
import engineering_schema
import lists
import datetime
import crud


def main():
	connect('importedDB')

	students = students_schema.StudentSchema.objects()
	crud.printStudentInfo(students)

	while True:
		crud.printOptions()

if __name__ == "__main__":
	main()