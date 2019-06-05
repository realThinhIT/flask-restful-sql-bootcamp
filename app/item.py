from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from register import UserRegister

app = Flask(__name__)
app.secret_key = 'thinh'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []

# def itemss():
#     global items
#     items = [1, 2, 3]
#
# itemss()
#
# print(items)


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next((i for i in items if i['name'] == name), None)

        return {
                   'item': item
               }, 200 if item else 404

    @jwt_required()
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {
                    'message': 'An item with {} already existed.'.format(name)
                }, 400

        body = request.get_json()
        new_item = {
            'name': name,
            'price': body['price']
        }
        items.append(new_item)

        return new_item, 201

    @jwt_required()
    def put(self, name):
        item = next((item for item in items if item['name'] == name), None)
        body = request.get_json()

        if item is None:
            return None, 404
        else:
            item.update(body)
            return {
                       'message': 'Item updated successfully!'
                   }, 200

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda i: i['name'] != name, items))

        return {
            'message': 'Item deleted'
        }, 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {
            'items': items
        }, 200


api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
