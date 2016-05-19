from mongoengine import *
import datetime

DISCIPLINES = ('Chemical', 'Civil', 'Electrical', 'Industrial', 'Mechanical', 'Materials')
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

class AcademicInfoSchema(EmbeddedDocument):
	registered = DateTimeField()
	status  = StringField( max_length=20, choices = ACADEMIC_STATUS )
	peyCompleted = BooleanField()
	hoursCompleted = BooleanField()
	graduationYear = IntField( min_value = 2016, max_value = 2019)
	gpa = ListField(
		DecimalField(min_value=0, max_value=4.0) )

class RegistrationInfoSchema(EmbeddedDocument):
	paid = BooleanField()
	international = BooleanField()

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


def isDeansList(student):
	studentGPA = student.academicInfo['gpa']
	meanGPA = sum(studentGPA)/len(studentGPA)
	numDeansList = 0
	if meanGPA >= 2.7:
		numDeansList += 1
	print ("%.2f %d" % (meanGPA, numDeansList) )