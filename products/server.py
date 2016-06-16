from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = "fjsldhgl"
mysql = MySQLConnection(app, 'products_db')


@app.route('/')
def index():
    query = "SELECT * FROM products"
    products = mysql.query_db(query)
    return render_template('index.html', products=products)


@app.route('/show/<product_id>/')
def show(product_id):
    query = "SELECT * FROM products WHERE product_id = :product_id"
    data = {"product_id": product_id}
    product = mysql.query_db(query, data)
    if product:
        return render_template('show.html', product=product[0])
    else:
        flash("There is no product with the id of "+str(product_id), "error")
        return redirect('/')


@app.route('/delete/<product_id>/')
def delete(product_id):
    query = "DELETE FROM products WHERE product_id = :product_id"
    data = {"product_id": product_id}
    mysql.query_db(query, data)
    flash("Product deleted", "success")
    return redirect('/')


@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/add/process/', methods=['POST'])
def add_process():
    errors = False

    name = request.form['product_name']
    price = request.form['product_price']
    description = request.form['product_description']

    if len(name) == 0:
        flash("Please enter a product name", "error")
        errors = True

    if len(price) == 0:
        flash("Please enter a product price", "error")
        errors = True

    try:
        float(price)
    except:
        flash("Please enter a valid price (eg. 20.50)", "error")
        errors = True

    if len(description) == 0:
        flash("Please enter a product description", "error")
        errors = True

    if errors:
        return redirect('/add/')

    query = "INSERT INTO products (name, price, description, created_at, updated_at) VALUES (:name, :price, :description, NOW(), NOW())"
    data = {
        "name": name,
        "price": price,
        "description": description
    }

    mysql.query_db(query, data)
    flash("You successfully added the product: "+name, "success")
    return redirect('/')


@app.route('/update/<product_id>/')
def update(product_id):
    query = "SELECT * FROM products WHERE product_id = :product_id"
    data = {'product_id':product_id}
    products = mysql.query_db(query, data)
    return render_template('update.html', product=products[0])


@app.route('/update/<product_id>/process/', methods=['POST'])
def update_process(product_id):
    errors = False

    name = request.form['product_name']
    price = request.form['product_price']
    description = request.form['product_description']

    if len(name) == 0:
        flash("Please enter a product name", "error")
        errors = True

    if len(price) == 0:
        flash("Please enter a product price", "error")
        errors = True

    try:
        float(price)
    except:
        flash("Please enter a valid price (eg. 20.50)", "error")
        errors = True

    if len(description) == 0:
        flash("Please enter a product description", "error")
        errors = True

    if errors:
        return redirect('/update/'+str(product_id))

    query = "UPDATE products SET name = :name, price = :price, description = :description, updated_at = NOW() WHERE product_id = :product_id"
    data = {
        'name': name,
        'price': price,
        'description': description,
        'product_id': product_id
    }
    mysql.query_db(query, data)

    flash("Product: "+name+" successfully updated!","success")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
