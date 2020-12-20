def delete_db(user_id, token, post_data, db, list_data):
    email = post_data['email']
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['user_id'] != user_id:
        return {'Error': 'invalid registered user_id'}
    elif list_data[0]['token'] != token:
        return {'Error': 'invalid registered token'}
    elif list_data[0]['role_name'] == 'admin':
        cur = db.cursor()
        query = "SELECT * FROM crud_table where email = ('" + str(email) + "')"
        cur.execute(query)
        fetch_table = cur.fetchall()
        list_table = []
        for table in fetch_table:
            dict_data = {'name': table[0], 'email': table[1], 'role_type': table[2], 'status': table[3]}
            list_table.append(dict_data)
        if len(list_table) == 0:
            return {'Error': 'invalid email'}
        elif list_table[0]['email'] == email:
            query = "DELETE FROM crud_table WHERE email = ('" + str(email) + "')"
            cur.execute(query)
            db.commit()
            return {"User": 'DELETED successfully'}
    else:
        return {'Error': 'you are not an registered admin to delete'}
