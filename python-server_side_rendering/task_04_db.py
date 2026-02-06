from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# -------- Read JSON --------
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []


# -------- Read CSV --------
def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        return []
    return products


# -------- Read SQLite --------
def read_sqlite():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()

    except Exception:
        return None  # Used to detect DB errors

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # -------- Select data source --------
    if source == 'json':
        data = read_json()

    elif source == 'csv':
        data = read_csv()

    elif source == 'sql':
        data = read_sqlite()
        if data is None:
            return render_template('product_display.html',
                                   error="Database error",
                                   products=[])

    else:
        return render_template('product_display.html',
                               error="Wrong source",
                               products=[])

    # -------- Filter by ID --------
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p['id'] == product_id]

            if not filtered:
                return render_template('product_display.html',
                                       error="Product not found",
                                       products=[])

            data = filtered

        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid id",
                                   products=[])

    return render_template('product_display.html',
                           products=data,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

