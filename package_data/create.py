from uuid import uuid4


def create_db(post_data, db):
    name = post_data['name']
    email = post_data['email']
    role_type = post_data['role_type']
    status = post_data['status']

    cur = db.cursor()
    try:
        query = "INSERT INTO crud_table (id, name, email, role_type, status) " \
                "VALUES ('" + str(uuid4()) + "', '" + str(name) + "', '" + str(email) + "', '" + str(role_type) + "', '" + str(status) + "')"
        cur.execute(query)
        db.commit()
    except Exception as e:
        return {'Error': str(e).split()[1].replace('\"', '') + " " + str(e).split()[2] + " " + str(e).split()[-1].replace("'crud_table.", "").replace("'", "").replace('\")', '')}

    return {"User": 'Registered successfully'}
