from flask import Flask
import os

app = Flask(__name__)

@app.route("/kill", methods=['POST']) #runs onn port 5000
def kill():
	os.system("sudo shutdown now")
	return '', 204


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
	return 'ok', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)