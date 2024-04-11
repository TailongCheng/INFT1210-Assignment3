# from flask import Flask
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def hello_cloud():
#   return 'Hello from Cheng ECS Container.'

# # Without port=8080, the docker container ip works, but GCP VM local ip and external ip doesnt work.
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/')
def main_route():
    return 'Hello Cloud! From Homepage!'
 
@app.route('/host')
def host_route():
    return 'Hello Cloud! From Host!'
 
@app.route('/ip')
def ip_route():
    # Get client's IP address from the request object
    client_ip = request.remote_addr
    return f'IP route data display. Client IP: {client_ip}'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')
