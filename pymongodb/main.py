import pymongo


myclient = pymongo.MongoClient("mongodb://root:1234@localhost:27017/")

db_name = 'users'

table_name = 'user_info'

mydb = myclient[db_name] # create db

mycol = mydb[table_name] # create table


# mydict = { "name": "John", "surname": "Doe", "address": "Highway 37" }

# x = mycol.insert_one(mydict)


# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)



# print(x.inserted_id)

# x = mycol.find_one()

# print(x['name'], x['address'])

####### filter

# for x in mycol.find({"address": { "$regex": "^[a-z]" }  }, { "_id":0, } ):
#     print(x)

####### sort

# for x in mycol.find().sort([("name", pymongo.ASCENDING), ("address", pymongo.DESCENDING)]):
#     print(x)

# myquery = { "address": {"$regex": "^S"} }

####### delete

# x = mycol.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")

####### update


# myquery = { "address": "Canyon 123" }

# newvalues = { "$set": { "address": "Valley 345" } }


# x = mycol.update_many(myquery, newvalues)

# print(x.updated_count, "documents updated.")


######## limiting

myresult = mycol.find().limit(5)

for x in myresult:
    print(x)

