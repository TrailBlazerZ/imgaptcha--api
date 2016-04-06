from flask import Flask, jsonify, request
from flask.ext.mysqldb import MySQL

app = Flask(__name__)

#app.config['MYSQL_HOST'/'MYSQL_USER'/'MYSQL_PASSWORD'] are set to default
app.config['MYSQL_DB'] = 'imagecaptcha'
mysql = MySQL(app)

im = [{'id':'1234', 'name':'tiger', 'url':'abcd'}, {'id':'4567', 'name':'tiger', 'url':'abcd'}]

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
	return jsonify({'img': im})
"""	images = []
	#return jsonify({'message' : 'It works!'})
	for i in range(0,len(rv)):
		id,name,url = rv[i] 
		obj = {'id' : val, 'name' : name, 'url' : url}
		images.append(obj)
		print images
		print rv[i]"""

@app.route('/image/<string:name>', methods=['GET'])
def returnType(name):
	img = [image for image in images if image['name'] == name]
	return jsonify({'res' : img})

if __name__ == "__main__":
	app.run()
