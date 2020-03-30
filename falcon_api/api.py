import falcon
import json
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


class DataCatcher(object):
	def on_get(self,req,resp):
		"""handles get requests"""
		resp.status = falcon.HTTP_405
		resp.body = ("\n405 - Method not allowed\n")

	def on_post(self, req, resp):
		"""handles post requests"""
		
		if req.content_length != 0:
			raw_data = req.bounded_stream.read()
			data =None
			data = json.loads(raw_data)["data"]
			print(data)
			"""
			try:
				data = json.loads(raw_data)["data"]
				print(data)
			except:
				data = None
			"""
			if data:
				print(raw_data)
				with sqlite3.connect("../db.db") as conn:
					cur = conn.cursor()
					cur.execute("INSERT INTO daily (x,y,z,zaman) values(?,?,?,?)",(str(data["x"]),str(data["y"]), str(data["z"]), str(time.time())))
					conn.commit()
		
				resp.status = falcon.HTTP_200

			else:
				resp.status = falcon.HTTP_500
				resp.body = ("\nCheck data format\n")	
				return 0

			resp.body = raw_data
		
		else:
			resp.status = falcon.HTTP_503
			resp.body =("\nUnexpected Problems\n")

api = falcon.API()
data_catcher = DataCatcher()

api.add_route('/data_read',data_catcher)

