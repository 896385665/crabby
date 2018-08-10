from . import cart_blue
from flask import render_template


@cart_blue.route('/cart/list')
def cart_list():
    return render_template('cart.html')
