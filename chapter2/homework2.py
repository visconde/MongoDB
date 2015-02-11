import pymongo
import sys

#get connection to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

#get DB
students = connection.students
#get collections
grades = students.grades

#set cursor to get the results
query = {'type':'homework'}
cursor  = grades.find(query)
cursor.sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

#iterate results
old_student = -1
for student in cursor:
	curr_student = student['student_id']
	if (curr_student != old_student):
		grades.remove({'_id' : student['_id']})
		print ('Removed this shit:', student)
	old_student = curr_student	