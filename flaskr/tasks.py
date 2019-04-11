import requests
import time
import datetime
from flaskr.db import get_db
import traceback
from flask import Flask, current_app

app = Flask(__name__)
app.config.from_pyfile('../flaskr/config.py')

def count_words_at_url(url):
    with app.app_context():
        try:
            db = get_db()
            db.execute("UPDATE words_data SET status=?,submitted_on=?  WHERE url=? ",('running',datetime.date.today(),url))
            db.commit()
        except:
            traceback.print_exc()
            print("INSERTION FAILED in tasks1.py")
            db.rollback()
        try:
            resp = requests.get(url)
            words= len(resp.text.split())
        except:
            words=0
        try:
            db.execute("UPDATE words_data SET status=? ,words_count=? WHERE url=? ",('finished',words,url))
            db.commit()
        except:
            print("INSERTION FAILED in tasks2.py")
            db.rollback()
        finally:
            return words
