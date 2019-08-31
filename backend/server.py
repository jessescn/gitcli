from flask import  Flask,  jsonify
import requests 

app = Flask(__name__)

@app.route('/followers/<string:dev>', methods=["GET"])
def followersInfo(dev):
    response  = requests.get('https://api.github.com/users/%s' % dev).json()
    followers_number  = response['followers']
    
    return jsonify(followers_number), 200 


@app.route('/user/<string:user>', methods=['GET'])
def devInfo(user):
    response  = requests.get('https://api.github.com/users/%s' % user).json()
    return jsonify(response), 200
    
if __name__ == '__main__':
    app.run(debug=True)

