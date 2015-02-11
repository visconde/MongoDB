import pymongo
import sys

#get connection to Mongo
connection = pymongo.MongoClient("mongodb://localhost")

#get DB
school = connection.school
#get collections
students = school.students

#set cursor to get the results
#query = {'type':'homework'}
cursor  = students.find()
#cursor.sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

#iterate results
for student in cursor:
	scores = student['scores']
	
	lowestHomework = 100000000
	homeworkCount = 0
	lowest = None
	
	for score in scores:
		if (score['type'] == "homework" and score['score'] < lowestHomework):
			lowestHomework = score['score']
			lowest = score
			homeworkCount+=1
			
	if (lowest is not None and homeworkCount > 1):
		query = {'_id':student['_id']}
		update = {'$pull':{'scores':lowest}}
		students.update(query, update)
		
		#other way would be to update the array and replace the complete student doc:
		#scores.remove(lowest)

	#student['scores'] = scores
	#students.update({'_id':student['_id']}, student)
	