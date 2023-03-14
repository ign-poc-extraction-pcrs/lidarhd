from flask import Blueprint, render_template, redirect, url_for


route = Blueprint('route', __name__, url_prefix='/')

@route.route('/')
def index():
    return redirect(url_for('route.lidarhd'))


@route.route('/lidarhd', methods=['GET'])
def lidarhd():
    return render_template('pages/lidarhd.html')

