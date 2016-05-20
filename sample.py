from mongoengine import *
import students_schema
import engineering_schema
import lists
import datetime

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

def main():
	connect('importedDB')

	students = students_schema.StudentSchema.objects()
	for student in students:
		students_schema.printStudentInfo(student)

	#engineering_schema.createDisciplines()
	disciplines = engineering_schema.DisciplineSchema.objects()

	for discipline in disciplines:
		engineering_schema.printDisciplineInfo(discipline)

	addStudent()

if __name__ == "__main__":
	main()