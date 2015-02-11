use test;

db.grades.aggregate(
[
	{$unwind:"$scores"},
	{$match:{"scores.type" : {"$ne":"quiz"}}},
	{$group:{
		_id:{"class":"$class_id","student":"$student_id"},
		"avge":{"$avg":"$scores.score"}}},
	{$group:{
		_id:{"class":"$_id.class"},
		"avge":{"$avg":"$avge"}}},
	{$sort:{"avge":-1}}	

])

