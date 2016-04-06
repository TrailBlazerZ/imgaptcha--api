from flask import Flask, jsonify, request
app = Flask(__name__)

images = [{'id':'1234', 'name':'tiger', 'url':'abcd'}, {'id':'4567', 'name':'tiger', 'url':'abcd'}]

@app.route("/", methods=["GET"])
def main():
	return jsonify({'message' : 'It works!'})

@app.route('/image', methods=["GET"])
def returnImage():
	return jsonify({'img': images})

@app.route('/image/<string:name>', methods=['GET'])
def returnType(name):
	img = [image for image in images if image['name'] == name]
	return jsonify({'res' : img})

if __name__ == "__main__":
	app.run()
