import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://loudwave-54180-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

user_ref = db.reference(f"users/{os.environ['UID']}")
user_ref.update({"deploy_status": 0})
print("Set deploy_status to 0 due to cancellation.")
