from mongoengine import *
import datetime
import lists

class CustomQuerySet(QuerySet):
	def is_graduation_elliglble(self):
		#TODO complete me using logical errors
		#want to return documents if peyCompleted= True and hoursCompleted= True
		return self.filter()

	def find_by_discipline_and_year(self, discipline_, year_):
		return self.filter(
			Q(discipline = discipline_) & Q(year = year_)
		)

	def find_student(self, name_):
		return self.filter(name= name_)

class AcademicInfoSchema(EmbeddedDocument):
	registered = DateTimeField(required=True)
	status  = StringField( max_length=20, choices = lists.ACADEMIC_STATUS, required=True )
	graduationYear = IntField( min_value = 2016, max_value = 2019, required=True)

	#TODO add missing schema for:
	#- peyCompleted[bool]
	#- hoursCompleted[bool]
	#- gpa [an array of DecimalField]
	#- status[string that has a max #chars =20, options based from list.ACADEMIC_STATUS and is required]
	#  StringField(choices = lists.ACADEMIC_STATUS )

class RegistrationInfoSchema(EmbeddedDocument):
	paid = BooleanField(default=False)
	international = BooleanField(required=True)

class ContactInfoSchema(EmbeddedDocument):
	email = EmailField(max_length = 50)
	phone = StringField(max_length = 9)


class StudentSchema(Document):
	name = IntField()	#max characters is 50 & is required
	year = IntField(min_value = 1, max_value = 4)
	discipline = StringField( max_length=20, choices= lists.DISCIPLINES)

	#EmbeddedDocuments 
	
	#TODO: add missing embedded document fields (RegistrationInfoSchema, ContactInfoSchema)
	academicInfo = EmbeddedDocumentField(AcademicInfoSchema)

	meta = {
		'collection': 'students',
		'queryset_class': CustomQuerySet
	}
