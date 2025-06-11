#Import the flask package
from flask import Flask
from flask_restful import Resource, Api

# Initialize app
app = Flask(__name__)

api = Api(app)

#GET "/"
@app.route("/", methods=["GET"])
def index():
    return {"message": "Welcome to my first flask app"}

#flask restful
class Index(Resource):
    def get():
        return {"message": "Welcome to my first flask app"}
    
    def post():
        pass

    def patch():
        pass

    def delete():
        pass

app.add_resource("/", Index)
