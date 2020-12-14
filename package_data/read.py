def read_db(db):
    cur = db.cursor()
    query = "SELECT * FROM crud_table"
    cur.execute(query)
    fetch_table = cur.fetchall()
    list_table = []
    for table in fetch_table:
        dict_data = {'id': table[0], 'name': table[1], 'email': table[2], 'role_type': table[3], 'status': table[4]}
        list_table.append(dict_data)
    return list_table
