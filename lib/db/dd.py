from os.path import isfile
from sqlite3 import connect

DB_PATH = "./data/db/database.db"
BUILD_PATH = "./data/db/build.sql"

cxn = connect(DB_PATH, check_same_thread=False)
cur = cxn.cursor()


def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()

        return inner


@with_commit
def build():
    if isfile(BUILD_PATH):
        scriptexec(BUILD_PATH)


 def commit():
    cxn.commit()


 def close():
    cxn.close()


 def field(command, *values):
    pass


 def field(command, *values):
    cur.execute(command, tuple(values))

    if (fetch := cur.fetchone()) is not None:
        return fetch[0]



 def record(command, *values):
    cur.execute(command, tuple(values))

    return cur.fetchone()


def records(command, *values):
    cur.execute(command, tuple(values))


def field(command, *values):
    cur.execute(command, tuple(values))
