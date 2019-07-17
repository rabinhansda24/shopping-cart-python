import pymysql
from flask import jsonify
from app import db, cursor

def create_product(product):
    sql = "INSERT INTO products (product_name, product_description, product_price, product_qty, created_by, actions) VALUES('%s','%s','%8.2f','%d','%d', '%d')" % (
        product["product_name"], product["product_description"], product["product_price"], product["product_qty"], product["created_by"], product["actions"])
    print(sql)
    status = 0
    res = ''

    try:
        cursor.execute(sql)
        db.commit()
        status = 200
        res = 'Product created successfully'

    except pymysql.Error as e:
        try:
            print("MySQL Error" + str(e) ) 
            return None
        except IndexError:
            print("MySQL Error: %s") % str(e)
            return None

    except:
        db.rollback()
        status = 401
        res = 'Something went wrong. Try again'

    return res, status

def delete_product(data):
    sql = "SELECT * FROM products WHERE product_id = %d" % data["product_id"]
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[6] == 4 or result[6] == 15 or result[6] == 7:
            sql2 = "DELETE FROM products WHERE product_id = %d" % data["product_id"]
            print(sql2)
            cursor.execute(sql2)
            db.commit()
            status = 200
            res = "Product deleted successfully"
        else:
            status = 201
            res = "Not authorized"
        print(result)
        print(type(result))
        
    except:
        print("Error: unable to fetch data")

    return res, status


def get_product(product_id):
    sql = "SELECT * FROM products WHERE product_id = %d" % product_id
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(type(result))
        data = {
            'id': result[0],
            'product_name': result[1],
            'product_description': result[2],
            'product_price': result[3],
            'product_qty': result[4],
            'created_by': result[5],
            'actions': result[6]
        }
        status = 200
        res = data 
            

    except:
        print("Error: unable to fetch data")
    return res, status
def get_products():
    sql = "SELECT * FROM products"
    status = 0,
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(type(result))
        data = []
        for rec in result:
            product = {
                'id': rec[0],
                'product_name': rec[1],
                'product_description': rec[2],
                'product_price': rec[3],
                'product_qty': rec[4],
                'created_by': rec[5],
                'actions': rec[6]
            }
            data.append(product)
        status = 200
        res = data

    except:
        print("Error: unable to fetch data")

    return res, status

def edit_product(data):
    sql = "SELECT * FROM products WHERE product_id = %d" % data["product_id"]
    print(sql)
    status = 0
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(type(result[6]))
        if result[6] == 2 or result[6] == 3 or result[6] == 6 or result[6] == 7 or result[6] == 15:
            sql = "UPDATE products SET product_name = '%s',product_description = '%s',product_price = '%8.2f', product_qty = '%d', created_by = '%d', actions = '%d' WHERE product_id = %d" % ( 
                data["product_name"], data["product_description"], data["product_price"], data["product_qty"], data["created_by"], data["actions"], data["product_id"])
            print(sql)
            status = 0
            res = ''

            try:
                cursor.execute(sql)
                db.commit()
                status = 200
                res = 'Product updated successfully'

            except pymysql.Error as e:
                try:
                    print("MySQL Error" + str(e))
                    return None
                except IndexError:
                    print("MySQL Error: %s") % str(e)
                    return None

            except:
                db.rollback()
                status = 401
                res = 'Something went wrong. Try again'

        else:
            status = 201
            res = "Not authorized"

    except:
        print("Error: unable to fetch data")

    return res, status


