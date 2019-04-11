from flask import Blueprint,render_template,request,jsonify
from flaskr.db import get_db
from redis import Redis
from rq import Queue
import datetime
import traceback
from flaskr.tasks import count_words_at_url

q = Queue(connection=Redis())
bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('index.html')



@bp.route('/job_submission',methods=['POST','GET'])
def job_submission():
    if request.method=="POST":
        entered_url=str(request.form.get('entered_text'))
        try:
            db = get_db()
            new=db.execute("INSERT INTO words_data (url,words_count,submitted_on,status) VALUES (?,?,?,?)",(entered_url,None,None,"In Queue"))
            db.commit()
        except KeyError as ae:
            print("key error",ae)
        except UnboundLocalError as ul:
            print("UnboundLocalError",ul)
        except NameError as ne:
            print("Name Error ",ne)
        except RuntimeError as re:
            print("run time error",re)
        except :
            traceback.print_exc()
        finally:
            result = q.enqueue(count_words_at_url,entered_url)
            tasks_count=len(q)
            return jsonify({"tasks_count":tasks_count})

@bp.route('/read_data',methods=['POST','GET'])
def count_words():
    if request.method=="POST":
        #catching the URL name entered by user
        entered_text=str(request.form.get('entered_text'))
        try:
            db = get_db()
            rows = db.execute("SELECT * FROM words_data").fetchall()
        except KeyError as ae:
            print("key error",ae)
        except UnboundLocalError as ul:
            print("UnboundLocalError",ul)
        except NameError as ne:
            print("Name Error ",ne)
        except RuntimeError as re:
            print("run time error",re)
        except:
            traceback.print_exc()
            rows=[]
        finally:
            row_tags=""
            for tuples in rows:
                row_tags+="<tr>"
                for field in tuples:
                    row_tags+="<td>"+str(field)+"</td>"
                row_tags+="</tr>"
            tasks_running=len(q)
            return jsonify({"row_tags": row_tags,"tasks_running":tasks_running})
