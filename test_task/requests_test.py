import json
import random

import requests

lst_id = []


def add_new_mhd(user_range):
    for user in range(0, user_range):
        payload = {'name': f'{user}'}
        r = requests.post('http://localhost:8080/users', json=payload)
        return r.text


def get_all_mhd():
    r = requests.get('http://localhost:8080/users')
    return r.text


def get_by_id_mhd(id):
    payload = {'id': f'{id}'}
    r = requests.get('http://localhost:8080/users_id', json=payload)
    return r.text


def alter_by_id_mhd(id, new_name):
    payload = {'id': f'{id}', 'new_name': new_name}
    r = requests.put('http://localhost:8080/users', json=payload)
    return r.text


def delete_by_id_mhd(id):
    payload = {'id': f'{id}'}
    r = requests.delete('http://localhost:8080/users', json=payload)
    return r.text


if __name__ == '__main__':
    add_new_mhd(15)
    lst = get_all_mhd()
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    for id in data['database']:
        lst_id.append(id)

    name = get_by_id_mhd(random.choice(lst_id))
    print(name)
    new_chosen_name = 'Rachel'
    new_altered = alter_by_id_mhd(random.choice(lst_id), new_chosen_name)
    get_all_mhd()
    delete_p = delete_by_id_mhd(random.choice(lst_id))
    print(delete_p)
    new_lst = get_all_mhd()
    print(new_lst)
