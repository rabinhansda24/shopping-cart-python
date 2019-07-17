from app import app
from flask import request, make_response, jsonify
from app.functions.user_management import create_user, delete_user, get_users
from app.functions.user_authentication import authenticate_user
from app.functions.product_management import create_product, edit_product, delete_product, get_product, get_products
from app.functions.user_type_management import add_user_type, delete_user_type



@app.route('/')
def hello():
    return 'Hellow, World!'

@app.route('/api/v1.0/user/create', methods=['POST'])
def user_add():
    user = request.json
    print(user)
    res, status = create_user(user)

    return make_response(jsonify(res = res, status = status))


@app.route('/api/v1.0/users', methods=['GET'])
def users():
    res, status = get_users()

    return make_response(jsonify(data = res, status = status))

@app.route('/api/v1.0/user/delete', methods=['DELETE'])
def user_delete():
    data = request.json
    res, status = delete_user(data)

    return make_response(jsonify(res = res, status = status))


@app.route('/api/v1.0/user/authenticate', methods=['POST'])
def login():
    user = request.json
    res, status = authenticate_user(user)

    return make_response(jsonify(data = res, status = status))


@app.route('/api/v1.0/product/create', methods=['POST'])
def add_product():
    product = request.json
    res, status = create_product(product)

    return make_response(jsonify(res = res, status = status))


@app.route('/api/v1.0/product/delete', methods=['DELETE'])
def product_delete():
    data = request.json
    res, status = delete_product(data)

    return make_response(jsonify(res = res, status = status))


@app.route('/api/v1.0/products', methods=['GET'])
def products():
    res, status = get_products()

    return make_response(jsonify(data=res, status=status))


@app.route('/api/v1.0/product/<int:product_id>', methods=['GET'])
def product(product_id):
    res, status = get_product(product_id)

    return make_response(jsonify(data = res, status = status))


@app.route('/api/v1.0/product/update', methods=['PUT'])
def updateproduct():
    data = request.json
    res, status = edit_product(data)

    return make_response(jsonify(res = res, status = status))


@app.route('/api/v1.0/usertype/add', methods=['POST'])
def addusertype():
    data = request.json
    res, status = add_user_type(data)

    return make_response(jsonify(res = res, status = status))


@app.route('/api/v1.0/usertype/delete', methods=['DELETE'])
def deleteusertype():
    data = request.json
    res, status = delete_user_type(data)

    return make_response(jsonify(res=res, status=status))







if __name__ == '__main__':
    app.run(debug = True)
