from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_cloud():
  return 'Hello from Cheng ECS Container.'

# Without port=8080, the docker container ip works, but GCP VM local ip and external ip doesnt work.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
