import pandas as pd
import csv


def download_csv(user_id, token, list_data, db, file_name):
    if len(list_data) == 0:
        return {'Error': 'invalid voter_id and token'}
    elif list_data[0]['user_id'] != user_id:
        return {'Error': 'invalid registered user_id'}
    elif list_data[0]['token'] != token:
        return {'Error': 'invalid registered token'}
    elif list_data[0]['role_name'] == 'admin':
        df = pd.read_sql_query("select * from crud_table", con=db)
        df.to_csv(file_name, index=False)
        return {'file_name': file_name}
        # cur = db.cursor()
        # query = "SELECT * FROM crud_table"
        # cur.execute(query)
        # result = cur.fetchall()
        # c = csv.writer(open('crud.csv', 'w'))
        # for x in result:
        #     c.writerow(x)
        # or    # result.to_csv("./Desktop/crud.csv")
        # return {'file_name': c}
    else:
        return {'Error': 'you are not an admin'}
