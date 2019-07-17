import pymysql
from app.lib.password_hashing import hash_password, verify_password
from app import db, cursor


def create_user(user):
    password = hash_password(user["password"])

    sql = "INSERT INTO users(user_name, user_email, user_password, user_address, user_phone, created_by, actions) VALUES ('%s','%s','%s','%s','%s', %d, %d)" % (user["user_name"], user["user_email"], password, user["user_address"], user["user_phone"], user["created_by"], user["actions"])

    status = 0
    res = ''

    try:
        cursor.execute(sql)
        db.commit()
        status = 200
        res = 'User created successfully'

    except pymysql.Error as e:
        try:
            print("MySQL Error [%d]: %s") % (e.args[0], e.args[1])
            return None
        except IndexError:
            print ("MySQL Error: %s") % str(e)
            return None

    except:
        db.rollback()
        status = 401
        res = 'Something went wrong. Try again'

    return res, status

def delete_user(data):
    sql = "SELECT * FROM users WHERE user_email = '%s'" % data["user_email"]
    print(sql)
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result[7])
        if result[7] == 4 or result[7] == 15 or result[7] == 7:
            sql2 = "DELETE FROM users WHERE user_email = '%s'" % data["user_email"]
            print(sql2)
            cursor.execute(sql2)
            db.commit()
            status = 200
            res = "User deleted successfully"
        else:
            status = 201
            res = "Not authorized"

    except:
        print("Error: unable to fetch data")

    return res, status

def get_users():
    sql = "SELECT * FROM users"
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        data = []
        for rec in result:
            user = {
                'id': rec[0],
                'user_name': rec[1],
                'user_email': rec[2],
                'user_address': rec[4],
                'user_phone': rec[5],
                'created_by': rec[6],
                'actions': rec[7]
            }
            data.append(user)
        status = 200
        res = data
    except:
        print("Error: unable to fetch data")

    return res, status
