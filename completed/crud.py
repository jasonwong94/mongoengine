from mongoengine import *
import students_schema
import engineering_schema
import lists
import datetime

def printStudentInfo(Students):
	print("----Student Record----")
	for student in Students:
		formattedOutput = '{:>22} {:>12} {:12}'.format(
		student.name, student.discipline, student.year)
		print formattedOutput 
	print("----End Record----")
	return

def addStudent():
	name_ = raw_input("> Enter a student name: ")
	year_ = raw_input("> Enter graduation year: ")
	discipline_ = raw_input("> Enter student discipline: ")

	academicInfo_ = students_schema.AcademicInfoSchema(
		registered = datetime.datetime.now(),
		graduationYear = year_,
		status = 'registered',
	)

	registrationInfo_ = students_schema.RegistrationInfoSchema(
		international = False
	)

	contactInfo_ = students_schema.ContactInfoSchema(
	)


	student = students_schema.StudentSchema(
		name = name_,
		discipline = discipline_,
		year = 1,
		registrationInfo = registrationInfo_,
		academicInfo = academicInfo_,
		contactInfo = contactInfo_
	)
	student.save()

	#find engineering disciplin
	disciplineSchema = engineering_schema.DisciplineSchema.objects(name = discipline_)
	disciplineSchema.update(
		add_to_set__students = [student]
	)

def removeStudent():
	studentName = raw_input("> Enter a student name: ")
	student = students_schema.StudentSchema.objects().find_student(studentName)

	student.delete()
	return

def addGPAToStudentProfile():
	studentName = raw_input("> Enter a student name: ")
	gpa = raw_input("> Enter GPA: ")

	student = students_schema.StudentSchema.objects().find_student(studentName).update(add_to_set__academicInfo__gpa = gpa)

	return

def displayGraduationInelligibleStudents():
	students = students_schema.StudentSchema.objects().is_graduation_elliglble()

	printStudentInfo(students)

	return

def getStudentInfo():
	studentName = raw_input("> Enter a student name: ")
	student = students_schema.StudentSchema.objects().find_student(studentName)

	printStudentInfo(student)
	return

def printAllStudents():
	students = students_schema.StudentSchema.objects()
	printStudentInfo(students)
	return

menuOptions = {
	"Add Student": addStudent,
	"Remove Student": removeStudent,
	"Get Student Info": getStudentInfo,
	"Add GPA to Student Profile": addGPAToStudentProfile,
	"Display Graduation Inelligible Students": displayGraduationInelligibleStudents,
	"Print All Students": printAllStudents
}

def printOptions():
	menuList = list(enumerate(menuOptions))

	for index, option in menuList:
		print(("%d - %s") % (index, option))

	userInput = input("Pick an option: ")

	if userInput >= len(menuList):
		print "Invalid option entered"
	else:
		#stores it as (index, title)
		title = menuList[userInput][1]
		menuOptions[title]()
