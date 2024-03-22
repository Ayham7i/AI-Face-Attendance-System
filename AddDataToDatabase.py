import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-33ca0-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "777777":
    {
        "name":"Ayham Al-Akhali",
        "major":"Computer Science",
        "starting_year":2021,
        "total_attendance":7,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2022-12-11 00:54:34",
    },
        "963852":
    {
        "name":"Elon Musk",
        "major":"AI",
        "starting_year":2020,
        "total_attendance":10,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2022-12-11 00:54:34",
    },
        "852741":
    {
        "name":"Emaly Blu",
        "major":"Software Engineering",
        "starting_year":2022,
        "total_attendance":9,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2022-12-11 00:54:34",
    }
}

for key, value in data.items():
    ref.child(key).set(value)
  