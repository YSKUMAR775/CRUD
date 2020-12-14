def update_db(post_data, db):
    name = post_data['name']
    email = post_data['email']
    role_type = post_data['update_role_type']
    status = post_data['update_status']

    cur = db.cursor()
    query = "SELECT * FROM crud_table where email = ('" + str(email) + "') OR name = ('" + str(name) + "')"
    cur.execute(query)
    fetch_table = cur.fetchall()
    list_table = []
    for table in fetch_table:
        dict_data = {'id': table[0], 'name': table[1], 'email': table[2], 'role_type': table[3], 'status': table[4]}
        list_table.append(dict_data)

    if len(list_table) == 0:
        return {'Error': 'invalid entry'}
    elif list_table[0]['name'] != name:
        return {'Error': 'name is incorrect'}
    elif list_table[0]['email'] != email:
        return {'Error': 'email is incorrect'}
    elif list_table[0]['email'] == email and list_table[0]['name'] == name:
        query = "UPDATE crud_table set role_type = ('" + str(role_type) + "'), status = ('" + str(status) + "') " \
                "WHERE email = ('" + str(email) + "')"
        cur.execute(query)
        db.commit()
        return {"User": 'updated successfully'}
