from firebase import firebase
from flask import current_app
from os import environ


class Config:
    def __init__(self):
        self.fb = firebase.FirebaseApplication(
            environ.get("RNOAPI_FIREBASE_URI")
            , None
        )

    def get(self, key, default=None):
        return self.fb.get("/rno-api/"+key, None) or default
