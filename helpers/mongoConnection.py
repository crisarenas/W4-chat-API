from pymongo import MongoClient

client = MongoClient()
db = client.get_database("my_api")

'''def get_company(name):
    curs = db.companies.find({"name":name}, {"name":1,"founded_year":1})
    return list(curs)'''


def insert_user(collection, user):
    curs = db[collection].insert_one(user)
    return {"_id": curs.inserted_id}