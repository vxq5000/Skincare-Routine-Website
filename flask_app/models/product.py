from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Product:
    def __init__(self,data):
        self.id=data['id']
        self.time_of_day=data['time_of_day']
        self.cleanser=data['cleanser']
        self.serum=data['serum']
        self.moisturizer=data['moisturizer']
        self.treatment=data['treatment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.reported_by={}

    @classmethod
    def save(cls,data):
        query="INSERT INTO products (time_of_day,cleanser,serum,moisturizer,treatment, user_id) VALUES (%(time_of_day)s,%(cleanser)s,%(serum)s,%(moisturizer)s,%(treatment)s,%(user_id)s);"
        return connectToMySQL('routine').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM products WHERE id=%(id)s"
        results=connectToMySQL('routine').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query="SELECT * FROM products;"
        results= connectToMySQL('routine').query_db(query)
        products=[]
        for row in results:
            products.append(cls(row))
        return products

    @classmethod
    def update(cls,data):
        query="UPDATE products SET time_of_day=%(time_of_day)s, cleanser=%(cleanser)s,serum=%(serum)s, moisturizer=%(moisturizer)s, treatment=%(treatment)s WHERE id=%(id)s;"
        return connectToMySQL('routine').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM products WHERE id = %(id)s;"
        return connectToMySQL('routine').query_db(query,data)

    @staticmethod
    def is_valid(product):
        is_valid=True
        if 'time_of_day' not in product:
          is_valid= False
          flash("Must select Morning or Nighttime Routine")
        if len(product['cleanser']) ==0:
          is_valid= False
          flash("Please select Cleanser!")
        if len(product['serum'])==0:
          is_valid= False
          flash("Please select Serum!")
        if len(product['moisturizer']) ==0:
          is_valid= False
          flash("You Need to Moisturize!")
        if len(product['treatment'])==0:
          is_valid= False
          flash("Please Pick an Extra Treatment!")
        return is_valid   