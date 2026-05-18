from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://adityacloudg23_db_user:<CaEmtJWUMPZEF0g6>@cluster0.0sd1u4i.mongodb.net/?appName=Cluster0"
)

db = client["attendance_system"]
