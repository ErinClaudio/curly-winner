from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from code.security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'erin1234'
api = Api(app)

jwt = JWT(app, authenticate, identity)
items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)  # Clearer as a list comprehension
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'an item with name {} already exists '. format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)
