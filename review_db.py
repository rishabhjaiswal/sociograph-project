import sqlite3

# conn = sqlite3.connect('my.db')
# print "Opened database successfully";

# conn.execute('CREATE TABLE REVIEW (ID NUMBER, TITLE TEXT, RATING NUMBER, COMMENTS TEXT)')
# print "Table created successfully";
# conn.close()

def get_all():
	conn = sqlite3.connect('my.db')
	print "Database successfully connected"
	value= conn.execute('''SELECT * FROM "REVIEW";''')
	count=value.fetchall();
	conn.close()
	print "databse closed"
	return count



def select_by_id(id):
	conn = sqlite3.connect('my.db')
	print "Database successfully connected"
	value= conn.execute('''SELECT * FROM "REVIEW" WHERE ID = ?;''',(id,))
	count=value.fetchall();
	conn.close()
	print "databse closed"
	if count:
		return count[0]
	else:
		return

def insert(title=None,rating=None,comments=None):
	conn = sqlite3.connect('my.db')
	print "Database successfully connected"
	value= conn.execute('''SELECT * FROM "REVIEW" ORDER BY ID DESC LIMIT 1;''')
	count=value.fetchall();
	if count:
		id=count[0][0]+1
	else:
		id=1
	conn.execute('''INSERT INTO "REVIEW" (ID,TITLE,RATING,COMMENTS)VALUES (?,?,?,?)''',(id,title,rating,comments) )
	conn.commit()
	conn.close()
	print "inserted row"
	print "databse closed"
	return

def delete_by_id(id):
	conn = sqlite3.connect('my.db')
	print "Database successfully connected"
	value= conn.execute("""DELETE from REVIEW WHERE ID = ? """,(id,))
	a=value.fetchall()
	print value.fetchall()
	conn.commit()
	conn.close()
	print "databse closed"
	if not a:
		return "no review at given id"
	return "row deleted"

def update_by_id(id,title=None,rating=None,comments=None):
	conn = sqlite3.connect('my.db')
	print "Opened database successfully"
	print id,title,rating,comments
	if title:
		conn.execute("""UPDATE REVIEW SET TITLE = ? WHERE ID= ? """,
  (title,id))
	if rating:
		conn.execute("""UPDATE REVIEW SET RATING = ? WHERE ID= ? """,
  (rating,id))
	if comments:
		conn.execute("""UPDATE REVIEW SET COMMENTS = ? WHERE ID= ? """,
  (comments,id))
	conn.commit()
	conn.close()
	print "databse closed"
	return

