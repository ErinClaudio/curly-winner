from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
    'store_name': 'My Wonderful Store',
    'items': [
        {'name': 'My item',
         'price': 20.00

         }]},
    {
        'store_name': 'My Wonderful Store part2',
        'items': [
            {'name': 'My item part2',
             'price': 30.00}]}]

'''
#so this is either rider(person)
or the individual ride(ie the miles you put in on that day,
From the house to the coffee place and back)

1. the methods need Strava appropriate names
'''


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'store_name': request_data['name'],
        'items': [],

    }
    stores.append(new_store)
    return jsonify(new_store)


# GET  /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['store_name'] == name:
            return jsonify(store)
    return jsonify({"please try again that was an error"})


# GET  /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item  {name;, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(store_name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == store_name:
            new_item = {
                'store_name': request_data['name'],
                'price': request_data['price'],
                }
            store_name['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'this is an error message you made a mistake. '})


# GET  /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(store_name):
    for store_items in stores:
        if store_items['store_name'] == store_name:
            return jsonify({'items': stores['items']})
    return jsonify({"please try again that was an error"})


app.run(port=5000)
