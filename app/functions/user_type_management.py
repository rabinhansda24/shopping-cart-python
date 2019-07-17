import pymysql
from flask import jsonify
from app import db, cursor


def add_user_type(data):
    sql = "INSERT INTO user_type (user_type, user_action,created_by) VALUES ('%s','%s',%d)" % (data["user_type"], data["user_action"], data["created_by"])
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        db.commit()
        status = 200
        res = 'User type created'
    except:
        status = 401
        res = 'Something went wrong'
    
    return res, status

def delete_user_type(data):
    sql = "SELECT * FROM user_type WHERE usertype_id = %d" % data["usertype_id"]
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[2] == 4 or result[2] == 15 or result[2] == 7:
            sql2 = "DELETE FROM user_type WHERE usertype_id = %d" % data["usertype_id"]
            print(sql2)
            cursor.execute(sql2)
            db.commit()
            status = 200
            res = "User type deleted successfully"
        else:
            status = 201
            res = "Not authorized"
        print(result)
        print(type(result))

    except:
        print("Error: unable to fetch data")

    return res, status
