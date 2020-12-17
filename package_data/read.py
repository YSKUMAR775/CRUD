def read_db(user_id, token, db, list_data):
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['user_id'] != user_id:
        return {'Error': 'invalid registered user_id'}
    elif list_data[0]['token'] != token:
        return {'Error': 'invalid registered token'}
    elif list_data[0]['user_id'] == user_id and list_data[0]['token'] == token:
        if list_data[0]['role_name'] == 'admin':
            cur = db.cursor()
            query = "SELECT * FROM crud_table"
            cur.execute(query)
            fetch_table = cur.fetchall()
            list_table = []
            for table in fetch_table:
                dict_data = {'id': table[0], 'name': table[1], 'email': table[2], 'role_type': table[3],
                             'status': table[4]}
                list_table.append(dict_data)
            return list_table
        else:
            return {'Error': 'you are not an registered admin to fetch the data'}
