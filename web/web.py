from flask import Flask
from flask import request
import sqlite3
import time

with sqlite3.connect("../db.db") as conn:
	try:
		new_table = time.time()
		cur = conn.cursor()
		cur.execute("ALTER TABLE daily RENAME TO DB_" + "_".join(str(new_table).split(".")))
		cur.execute("CREATE TABLE daily (x int ,y int,z int,zaman float)")

		cur.fetchall()
	except:
		cur = conn.cursor()
		cur.execute("CREATE TABLE daily (x int ,y int,z int,zaman float)")

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def Welcome_page():
	return "hârro!\nif u wanna see the results goto /show/data"



if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)