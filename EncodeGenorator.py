import cv2 
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-33ca0-default-rtdb.firebaseio.com/",
    'storageBucket':'faceattendancerealtime-33ca0.appspot.com'

   
})


# importing student imges 
folderpath = 'Images'
imgpathList = os.listdir(folderpath)
studentid = []

imgList = [] 
for path in imgpathList:

    imgList.append(cv2.imread(os.path.join(folderpath,path)))
    studentid.append(os.path.splitext(path)[0])

    fileName = f'{folderpath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
   # print(os.path.splitext(path)[0])

# print(len(imgList))

def findEncoding(imagesList):
    encodeList = []
    for img in imagesList:

      img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
      encode = face_recognition.face_encodings(img)[0]
      encodeList.append(encode)
      print(encode)

    return encodeList

print("Encoding Starting ....")
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIDs = [encodeListKnown,studentid]
print("encoding Done ")

file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnownWithIDs,file)
file.close()
