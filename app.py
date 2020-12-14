from flask import Flask, request, jsonify
from package_data import database, create, read, update, delete

app = Flask(__name__)


@app.route("/create", methods=['POST'])
def create_data():
    post_data = request.get_json()
    db = database.db_connect()
    info = create.create_db(post_data, db)

    return jsonify(info)


@app.route("/read", methods=['GET'])
def read_data():
    db = database.db_connect()
    info = read.read_db(db)

    return jsonify(info)


@app.route("/update", methods=['POST'])
def update_data():
    post_data = request.get_json()
    db = database.db_connect()
    info = update.update_db(post_data, db)

    return jsonify(info)


@app.route("/delete", methods=['POST'])
def delete_data():
    post_data = request.get_json()
    db = database.db_connect()
    info = delete.delete_db(post_data, db)

    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True)
