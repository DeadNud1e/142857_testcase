from flask import Flask, jsonify
import os
from utils import query_to_dict, get_db_result

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
    return "/product-category - all product - category pairs, /products all products with categories, /categories all categories with products"

@app.route("/categories", methods=['GET'])
def categories():
    query = "SELECT c.name as category, array_agg(p2.name) as product_names FROM product p2 " + \
            "left join productcategory p on p.product_id =p2.product_id  " + \
            "right join category c  on p.category_id =c.category_id  " + \
            "group by c.name order by c.name"
    return jsonify(categories=query_to_dict(get_db_result(query)))

@app.route("/products", methods=['GET'])
def products():
    query = "SELECT p2.name as product, array_agg(c.name) as category_names FROM product p2 " + \
            "left join productcategory p on p.product_id =p2.product_id  " + \
            "left join category c  on p.category_id =c.category_id  " + \
            "group by p2.product_id order by p2.name"
    return jsonify(products=query_to_dict(get_db_result(query)))

@app.route("/product-category", methods=['GET'])
def product_category():
    query = "SELECT p2.name as product_name, c.name as category_name FROM product p2 " + \
            "join productcategory p on p.product_id =p2.product_id  " + \
            "join category c  on p.category_id =c.category_id  " + \
            "order by p2.product_id"
    return jsonify(product_category=query_to_dict(get_db_result(query)))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)