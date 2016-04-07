from flask import Flask, jsonify, request
from flask.ext.mysqldb import MySQL
import cv2
import numpy as np
from imgprocess import imgprocs, imgprocl
import urllib
from random import randint

app = Flask(__name__)

#app.config['MYSQL_HOST'/'MYSQL_USER'/'MYSQL_PASSWORD'] are set to default

app.config['MYSQL_DB'] = 'imagecaptcha'
mysql = MySQL(app)

#im = [{'id':'1234', 'name':'tiger', 'url':'abcd'}, {'id':'4567', 'name':'tiger', 'url':'abcd'}]

@app.route("/", methods=["GET"])
def main():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM images''')
	rv = cur.fetchall()
	#return jsonify({'message' : 'It works!'})
	for i in range(0,len(rv)):
		id,name,url = rv[i] 
		print rv[i]
	return str(rv)

@app.route('/images', methods=["GET"])
def returnImage():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM images''')
	rv = cur.fetchall()
	images = []
	#return jsonify({'message' : 'It works!'})
	for i in range(0,len(rv)):
		id,name,url = rv[i] 
		obj = {}
		obj['id'] = str(id)
		obj['name'] = str(name)
		obj['url'] = str(url)
		images.append(obj)
		'''
		images[i] = obj
		print images
		'''
		print str(id) + str(name) + str(url)
	return jsonify({'img':images})

@app.route('/image/<string:nname>', methods=['GET'])
def returnType(nname):
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM images''')
	rv = cur.fetchall()
	images = []
	#return jsonify({'message' : 'It works!'})
	for i in range(0,len(rv)):
		id,name,url = rv[i]
		obj = {}
		obj['id'] = str(id)
		obj['name'] = str(name)
		obj['url'] = str(url)
		images.append(obj)
	img = [image for image in images if image['name'] == nname]
	return jsonify({'res' : img})

@app.route('/procid/<string:iid>', methods=['GET','POST'])
def returnProcImg(iid):
	cur = mysql.connection.cursor()
	sql = "SELECT * FROM images \
	 	    WHERE id LIKE '%s'" % (iid)
	cur.execute(sql)
	rv = cur.fetchall()
	id,name,url = rv[0]
	print (id,name,url)
	# query = "SELECT * FROM imgprocess \
	# 		WHERE id LIKE '%s'" % (iid)
	# img = []
	# try:
	# 	print ("2")
	# 	cur.execute(query)
	# 	rvi = cur.fetchall()
	# 	obj = {}
	# 	# get the processed id and url from the table
	# 	idp, urlp = rvi[0]
	# 	obj['id'] = str(idp)
	# 	obj['url'] = str(urlp)
	# 	img.append(obj)
	# 	return jsonify({'res' : img})
	# except:
	# 	#sobel
	# 	#imgprocs(str(url),iid) 
	# 	#laplacian
	# 	print ("1")
	# 	new_url = "http://localhost:5000/cgi/" + str(id) + ".png" 
	# 	print (str(new_url))
	# 	print (str(url))
	# 	imgprocl(str(url),id)
	# 	query = "INSERT INTO imgprocess \
	# 			VALUES ('%s', '%s')" % (str(id), str(new_url))
	# 	cur.execute(query)
	# 	connection.commit()
	# 	img = []
	# 	obj = {}
	#Adding randomization in filters
	if (randint(0,1) == 1):
		imgprocl(str(url),id)
	else:
		imgprocs(str(url),id)
	img = []
	obj = {}
	port = "5500"
	#new_url = "http://localhost:5000/" + "cgi/" + str(id) + ".png"
	new_url = "http://localhost:" + str(port) + "/" + str(id) + ".png"
	obj['id'] = str(id)
	obj['url'] = str(new_url)
	img.append(obj)
	cur.close()
	return jsonify({'res' : img})
		#return jsonify({'message' : 'It works!'})


if __name__ == "__main__":
	app.run()
