import firebase_admin
from firebase_admin import credentials, db
import os

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://loudwave-54180-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

user_ref = db.reference(f"users/{os.environ['UID']}")

# Set both the URL and the deploy status
user_ref.update({
    "url": os.environ['NGROK_URL'],
    "deploy_status": 1
})

# Print the URL in a loop
url = os.environ['NGROK_URL']
for i in range(5):
    print(f"noVNC Link: {url}")
