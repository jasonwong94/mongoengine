from mongoengine import *
import datetime
import lists

class CustomQuerySet(QuerySet):
	def is_graduation_elliglble(self):
		return self.filter(
			Q(academicInfo__peyCompleted= True) | Q(academicInfo__hoursCompleted= True) 
		)

	def find_by_discipline_and_year(self, discipline_, year_):
		return self.filter(
			Q(discipline = discipline_) & Q(year = year_)
		)

	def find_student(self, name_):
		return self.filter(name= name_)

class AcademicInfoSchema(EmbeddedDocument):
	registered = DateTimeField(required=True)
	status  = StringField( max_length=20, choices = lists.ACADEMIC_STATUS, required=True )
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
	discipline = StringField( max_length=20, choices= lists.DISCIPLINES)

	#EmbeddedDocuments 
	registrationInfo = EmbeddedDocumentField(RegistrationInfoSchema)
	contactInfo = EmbeddedDocumentField(ContactInfoSchema)
	academicInfo = EmbeddedDocumentField(AcademicInfoSchema)

	meta = {
		'collection': 'students',
		'queryset_class': CustomQuerySet
	}
