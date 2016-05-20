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

	#TODO: initial the AcademicInfoSchema, RegistrationInfoSchema, ContactInfoSchema
	academicInfo_ = students_schema.AcademicInfoSchema(
		registered = datetime.datetime.now(),
		status = 'registered',

		#pass in missing graduation year parameter!
	)

	registrationInfo_ = students_schema.RegistrationInfoSchema(
		international = False
	)

	contactInfo_ = students_schema.ContactInfoSchema(
	)


	student = students_schema.StudentSchema(
		#TODO: pass in missing name and discipline parameter!
		
		discipline = discipline_,
		year = 1,
		
		#TODO: add missing embedded documents
	)
	student.save()

	#find engineering disciplin
	disciplineSchema = engineering_schema.DisciplineSchema.objects(name = discipline_)
	
	#TODO: update students field in the document

def removeStudent():
	studentName = raw_input("> Enter a student name: ")
	student = students_schema.StudentSchema.objects().find_student(studentName)

	#TODO: call function to remove student
	return

def addGPAToStudentProfile():
	studentName = raw_input("> Enter a student name: ")
	gpa = raw_input("> Enter GPA: ")


	#TODO: update student result
	return

def displayGraduationInelligibleStudents():
	#prints out students that cannot graduate
	#TODO: call missing query function & print function

	return

def getStudentInfo():
	studentName = raw_input("> Enter a student name: ")
	#TODO: call query that extracts student info
	return

def printAllStudents():
	#TODO: complete me
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
