import json
import uuid

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


def is_json_check(forwarded_request):
    if forwarded_request.is_json is True:
        return True
    else:
        return False


def create_json():
    with open('data.json', 'w') as data:
        json.dump({'database': {}}, data)


def json_interation(parameter, data_to_write=None):
    if parameter == 'r':
        with open('data.json', parameter) as data_r:
            data = json.load(data_r)
            return data

    elif parameter == 'w':
        with open('data.json', parameter) as data_w:
            data_w.write(data_to_write)  #


# add new user
# • Добавление User
@app.route('/users', methods=['POST'])
def add_new():
    is_json = is_json_check(request)
    if is_json is True:
        content = request.get_json()

        temp = data_r['database']
        # generating unique id
        id_new = str(uuid.uuid4())
        if id_new not in temp.keys():
            temp[id_new] = content['name']
            json_interation('w', json.dumps(data_r))
            return jsonify({'status': 'added successfully'})
        else:
            return jsonify({'status': 'already exists'})


# • Получение списка User
@app.route('/users', methods=['GET'])
def get_all():
    temp = data_r['database']
    return jsonify({'database': f"{temp}"})


# get user by id
# • Получение User по Id
@app.route('/users_id', methods=['GET'])
def get_by_id():
    is_json = is_json_check(request)
    if is_json is True:
        content = request.get_json()
        id_searched = content['id']
        temp = data_r['database']
        if id_searched in temp.keys():
            return jsonify({f'{id_searched}': f'{temp[id_searched]}'})
        else:
            return jsonify({'status': 'not found'})


# alter username by id
# • Редактирование User по Id
@app.route('/users', methods=['PUT'])
def alter_by_id():
    is_json = is_json_check(request)
    if is_json is True:
        content = request.get_json()
        new_name = content['new_name']
        id_searched = content['id']
        temp = data_r['database']
        if id_searched in temp.keys():
            temp[id_searched] = new_name
            json_interation('w', json.dumps(data_r))
            return jsonify({id_searched: new_name})


# delete user by id
# • Удаление User по Id
@app.route('/users', methods=['DELETE'])
def delete_by_id():
    is_json = is_json_check(request)
    if is_json is True:
        content = request.get_json()  # + exception
        id_searched = content['id']
        temp = data_r['database']
        if id_searched in temp.keys():
            username = temp[id_searched]
            del temp[id_searched]
            json_interation('w', json.dumps(data_r))
            return jsonify({'status': f'{username} deleted'})


if __name__ == '__main__':
    create_json()
    data_r = json_interation('r')
    app.run(host='127.0.0.1', port=8080)
