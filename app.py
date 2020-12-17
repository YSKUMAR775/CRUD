from flask import Flask, request, jsonify
from package_register import database, account_register, validations, password_encryption, login_token, account_login
from package_data import account_login_fetch, database2, create, read, update, delete


app = Flask(__name__)


@app.route("/register", methods=['POST'])
def register():
    db = database.db_connect()
    post_data = request.get_json()
    encrypted_password = password_encryption.pass_encrypt(post_data)
    validations_data = validations.valid(post_data)
    registered_data = account_register.reg_data(post_data, validations_data, encrypted_password, db)

    return jsonify(registered_data)


@app.route("/login", methods=["POST"])
def login():
    db = database.db_connect()
    post_data = request.get_json()
    list_data = account_login.auth_lgn(post_data, db)
    password_check_final = password_encryption.pass_check(post_data, list_data)
    token_generate = login_token.lgn_token(list_data, post_data, db, password_check_final)

    return jsonify(token_generate)


@app.route("/create/user_id=<user_id>", methods=['POST'])
def create_data(user_id):
    token = request.headers['token_data']
    post_data = request.get_json()
    db = database2.db_connect2()
    list_data = account_login_fetch.acct_fetch(user_id, token, db)
    info = create.create_db(user_id, token, list_data, post_data, db)

    return jsonify(info)


@app.route("/read/user_id=<user_id>", methods=['GET'])
def read_data(user_id):
    token = request.headers['token_data']
    db = database2.db_connect2()
    list_data = account_login_fetch.acct_fetch(user_id, token, db)
    info = read.read_db(user_id, token, db, list_data)

    return jsonify(info)


@app.route("/update/user_id=<user_id>", methods=['POST'])
def update_data(user_id):
    token = request.headers['token_data']
    post_data = request.get_json()
    db = database2.db_connect2()
    list_data = account_login_fetch.acct_fetch(user_id, token, db)
    info = update.update_db(user_id, token, post_data, db, list_data)

    return jsonify(info)


@app.route("/delete/user_id=<user_id>", methods=['POST'])
def delete_data(user_id):
    token = request.headers['token_data']
    post_data = request.get_json()
    db = database2.db_connect2()
    list_data = account_login_fetch.acct_fetch(user_id, token, db)
    info = delete.delete_db(user_id, token, post_data, db, list_data)

    return jsonify(info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
