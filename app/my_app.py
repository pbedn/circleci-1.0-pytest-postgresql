def hello():
    return "Hello world"


def using_database(con, cur):
    cur.execute("UPDATE gtfs SET active=false WHERE route='000070' ")
    con.commit()
