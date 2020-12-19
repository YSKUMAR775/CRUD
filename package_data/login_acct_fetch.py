def acct_fetch(user_id, token, db):
    cur = db.cursor()
    query = "SELECT * FROM crud_register where user_id = ('" + str(user_id) + "') OR token = ('" + str(token) + "')"
    cur.execute(query)
    table_data = cur.fetchall()
    list_data = []
    for data in table_data:
        dict_data = {"user_id": data[0], "user_name": data[1], "phone": data[2], "email": data[3],
                     "password": data[4], "token": data[5], "role_name": data[6]}
        list_data.append(dict_data)

    return list_data
