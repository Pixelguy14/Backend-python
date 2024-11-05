import firebase_admin
from firebase_admin import credentials, firestore

def intialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate('src/config/firebaseServiceAccount.json')
        firebase_admin.initialize_app(cred)
    return firestore.client()

