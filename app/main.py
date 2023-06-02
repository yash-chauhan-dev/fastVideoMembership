from cassandra.cqlengine.management import sync_table
from fastapi import FastAPI

from app import db
from app.users.models import User

app = FastAPI()
DB_SESSION = None


@app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)


@app.get('/users')
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)
