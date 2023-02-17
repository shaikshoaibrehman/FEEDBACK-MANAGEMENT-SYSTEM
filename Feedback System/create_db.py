import sqlite3

def create_db():
    con=sqlite3.connect(database=r'fms.db' )
    cur=con.cursor()
    cur.execute( "CREATE  TABLE  IF NOT EXISTS faculty (fac_id INTEGER PRIMARY KEY  , fac_name text ,gender text  , contact text  , doj text  ,  email text  , pass text  )"   )
    # if want to password in the details then add {pass text, } before utype
    con.commit()
    
    
    cur.execute( "CREATE  TABLE  IF NOT EXISTS feedback(fac_id INTEGER ,fac_name text   ,sem text , q1 text,q2 text,q3 text,q4 text,q5 text)"   )
    con.commit()
    
    cur.execute( "CREATE  TABLE  IF NOT EXISTS student(usn text PRIMARY KEY ,name text ,sem text,password text ,email text)"   )
    con.commit()
create_db()