from mongoengine import *
import datetime

DISCIPLINES = ('Chemical', 'Civil', 'Electrical', 'Industrial', 'Mechanical', 'Materials', 'TrackOne')
ACADEMIC_STATUS = ('registered', 'withdrawn', 'probation')

def printStudentInfo(Student):
	print ("%s %s %d" % (Student.name, Student.discipline, Student.year)) 
	return

class CustomQuerySet(QuerySet):
	def filter_by_year(self, year_):
		return self.filter(year= year_)

	def is_graduation_elliglble(self):
		return self.filter(
			Q(academicInfo__peyCompleted= True) | Q(academicInfo__hoursCompleted= True) 
		)

	def find_student(self, name_):
		return self.filter(name= name_)

class AcademicInfoSchema(EmbeddedDocument):
	registered = DateTimeField(required=True)
	status  = StringField( max_length=20, choices = ACADEMIC_STATUS, required=True )
	peyCompleted = BooleanField()
	hoursCompleted = BooleanField()
	graduationYear = IntField( min_value = 2016, max_value = 2019, required=True)
	gpa = ListField(
		DecimalField(min_value=0, max_value=4.0) )

class RegistrationInfoSchema(EmbeddedDocument):
	paid = BooleanField(default=False)
	international = BooleanField(required=True)

class ContactInfoSchema(EmbeddedDocument):
	email = EmailField(max_length = 50)
	phone = StringField(max_lenght = 9)


class StudentSchema(Document):
	name = StringField(max_length=50, required=True )
	year = IntField(min_value = 1, max_value = 4)
	discipline = StringField( max_length=20, choices= DISCIPLINES)

	#EmbeddedDocuments 
	registrationInfo = EmbeddedDocumentField(RegistrationInfoSchema)
	contactInfo = EmbeddedDocumentField(ContactInfoSchema)
	academicInfo = EmbeddedDocumentField(AcademicInfoSchema)

	meta = {
		'collection': 'students',
		'queryset_class': CustomQuerySet
	}

#for now we'll just pass in the required params..
def addStudent():
	name_ = raw_input("> Enter a student name: ")
	year_ = raw_input("> Enter graduation year: ")
	discipline_ = raw_input("> Enter student discipline: ")

	academicInfo_ = AcademicInfoSchema(
		registered = datetime.datetime.now(),
		graduationYear = year_,
		status = 'registered',
	)

	registrationInfo_ = RegistrationInfoSchema(
		international = False
	)

	contactInfo_ = ContactInfoSchema(
	)


	student = StudentSchema(
		name = name_,
		discipline = discipline_,
		year = 1,
		registrationInfo = registrationInfo_,
		academicInfo = academicInfo_,
		contactInfo = contactInfo_
	)
	student.save()

def isDeansList(student):
	studentGPA = student.academicInfo['gpa']
	meanGPA = sum(studentGPA)/len(studentGPA)
	numDeansList = 0
	if meanGPA >= 2.7:
		numDeansList += 1
	print ("%.2f %d" % (meanGPA, numDeansList) )

