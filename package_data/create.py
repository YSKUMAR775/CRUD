def create_db(user_id, token, list_data, post_data, db):
    name = post_data['name']
    email = post_data['email']
    role_type = post_data['role_type']
    status = post_data['status']
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['user_id'] != user_id:
        return {'Error': 'invalid registered user_id'}
    elif list_data[0]['token'] != token:
        return {'Error': 'invalid registered token'}
    elif list_data[0]['role_name'] == 'admin':
        cur = db.cursor()
        try:
            query = "INSERT INTO crud_table (name, email, role_type, status) " \
                    "VALUES ('" + str(name) + "', '" + str(email) + "', " \
                    "'" + str(role_type) + "', '" + str(status) + "')"
            cur.execute(query)
            db.commit()
        except Exception as e:
            return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace("'crud_table.", "").replace("'", "").replace('\")', '')}

        return {"User": 'created successfully'}
    else:
        return {'Error': 'you are not an registered admin to add the user'}
