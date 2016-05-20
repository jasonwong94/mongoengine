from mongoengine import *
import students_schema
import lists

def printDisciplineInfo(Discipline):
	print("%s" % (Discipline.name))
	for student in Discipline.students:
		print student

class DisciplineSchema(Document):
	name = StringField( max_length=20, choice = lists.DISCIPLINES, unique = True)
	students = ListField(ReferenceField(students_schema.StudentSchema, dbref = False))

	meta = {
		'collection': 'engineering' 
	}