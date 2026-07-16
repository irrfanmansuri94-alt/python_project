from pymongo import MongoClient
import certifi
try:
    MONGO_URI = "mongodb+srv://irrfanmansuri94_db_user:irfan123@cluster0.vforyyh.mongodb.net/?appName=Cluster0"
    client = MongoClient(MONGO_URI,tls=True,tlsCAFile=certifi.where())
    client.admin.command("ping")
    db = client["ssus12345"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB Connected Successfully")
    print(client.list_database_names())


except Exception as e:
    print("MongoDB Error:",e)
