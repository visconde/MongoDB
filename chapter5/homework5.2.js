use test;
db.zips.aggregate([
{$match:{$or: 
		[{"state":{"$eq":"NY"}},
		{"state":{"$eq":"CA"}}
	]}},
{$group:{_id:{"state":"$state", "city":"$city"}, "pop": {"$sum":"$pop"} } },

{$match:{"pop":{"$gt":25000}}},	
	
{$group:{_id:"1", "pop": {"$avg":"$pop"} } }
	
	]
)