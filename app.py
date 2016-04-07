from flask import Flask, jsonify, request
from flask.ext.mysqldb import MySQL
import cv2
import numpy as np
from imgprocess import imgproc
import urllib


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
	imgproc(str(url),iid)
	#cv2.imwrite(str(id)+".png", procimg)
	return jsonify({'message' : 'It works!'})



if __name__ == "__main__":
	app.run()
