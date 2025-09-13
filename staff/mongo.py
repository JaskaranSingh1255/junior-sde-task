from pymongo import MongoClient, ASCENDING

client = MongoClient("mongodb://localhost:27017/")
db = client["assessment_db"]
collection = db["employees"]

index_info = collection.index_information()
if "employee_id_idx" in index_info:
    collection.drop_index("employee_id_idx")


if "employee_id_1" not in index_info:
    collection.create_index([("employee_id", ASCENDING)], name="employee_id_idx", unique=True)
