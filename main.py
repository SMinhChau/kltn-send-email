from flask_restful import Api, Resource
from flask import Flask, request
from task import send

app = Flask(__name__)
api = Api(app)

class SendMailResource(Resource):

    def post(self):
        _data =  request.json
        send.delay(**_data)
        return {'status': 'success'}
        


api.add_resource(SendMailResource, '/send-mail')

if __name__ == '__main__':
    app.run(debug=True, port=5005, host='0.0.0.0')
