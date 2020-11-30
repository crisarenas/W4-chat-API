from pymongo import MongoClient
import os
import dotenv
dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")



client = MongoClient(DBURL)         #get the value of environment variable and returns empty if not present
db = client.get_database("my_api")




'''def get_company(name):
    curs = db.companies.find({"name":name}, {"name":1,"founded_year":1})
    return list(curs)

'''
'''def insert_data(collection, data):
    curs = db[collection].insert_one(data)
    return {"_id": curs.inserted_id}  ''' 
