from flask import Blueprint, render_template, request, redirect, url_for
from models.order import Order
from models.user import User
from models.product import Product
from datetime import datetime
from flask import jsonify
from peewee import fn

order_bp = Blueprint('order', __name__, url_prefix='/orders')


@order_bp.route('/')
def list():
    orders = Order.select()
    return render_template('order_list.html', title='注文一覧', items=orders)


@order_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        order_date = datetime.now()
        Order.create(user=user_id, product=product_id, quantity=quantity, order_date=order_date)
        return redirect(url_for('order.list'))
    
    users = User.select()
    products = Product.select()
    return render_template('order_add.html', users=users, products=products)


@order_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(order_id):
    order = Order.get_or_none(Order.id == order_id)
    if not order:
        return redirect(url_for('order.list'))

    if request.method == 'POST':
        order.user = request.form['user_id']
        order.product = request.form['product_id']
        order.quantity = request.form['quantity']
        order.save()
        return redirect(url_for('order.list'))

    users = User.select()
    products = Product.select()
    return render_template('order_edit.html', order=order, users=users, products=products)

@order_bp.route('/stats/product-ratio')
def product_ratio():
    """
    商品ごとの購入数量割合を返す
    形式:
    [
      { "product": "りんご", "quantity": 10, "ratio": 25.0 },
      { "product": "みかん", "quantity": 30, "ratio": 75.0 }
    ]
    """

    # 商品ごとの数量合計を取得
    query = (
        Order
        .select(
            Product.name.alias('product_name'),
            fn.SUM(Order.quantity).alias('total_quantity')
        )
        .join(Product)
        .group_by(Product.id)
    )

    # 全商品の数量合計
    grand_total = sum(row.total_quantity for row in query)

    result = []
    for row in query:
        ratio = 0
        if grand_total > 0:
            ratio = row.total_quantity / grand_total * 100

        result.append({
            'product': row.product_name,
            'quantity': row.total_quantity,
            'ratio': round(ratio, 2)
        })

    return jsonify(result)
