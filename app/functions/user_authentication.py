import pymysql
from app.lib.password_hashing import hash_password, verify_password
from app import db, cursor


def authenticate_user(user):
    sql = "SELECT * FROM users WHERE user_email = '%s'" % (user["user_email"])
    print(sql)
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        if verify_password(result[0][3], user["password"]):
            status = 200
            user = {
                'id': result[0][0],
                'user_name': result[0][1],
                'user_email': result[0][2],
                'user_address': result[0][4],
                'user_phone': result[0][5],
                'created_by': result[0][6],
                'actions': result[0][7]
            }
            res = user
        else:
            status = 401
            res = 'Login failed'

    except pymysql.Error as e:
        try:
            print("MySQL Error [%d]: %s") % (e.args[0], e.args[1])
            return None
        except IndexError:
            print("MySQL Error: %s") % str(e)
            return None
    except:
        status = 401
        status = 'Login failed'
    
    return res, status
