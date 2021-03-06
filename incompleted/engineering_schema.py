from mongoengine import *
import students_schema
import lists

def printDisciplineInfo(Discipline):
	print("%s" % (Discipline.name))
	for student in Discipline.students:
		print student

class DisciplineSchema(Document):
	#TODO: add missing name field
	students = ListField(ReferenceField(students_schema.StudentSchema, dbref = False, reverse_delete_rule=PULL))

	meta = {
		'collection': 'engineering' 
	}