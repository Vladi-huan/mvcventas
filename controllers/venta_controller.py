from flask import request, redirect, url_for, blueprints, Blueprint
from datetime import datetime
from models.producto_model import Producto
from models.cliente_model import Cliente
from models.venta_model import Venta
from views import venta_view

venta_dp = Blueprint('venta',__name__,url_prefix="/ventas")

@venta_dp.route("/")
def index():
    #recupera todos los registros de la tabla ventas en forma de objeto
    ventas = Venta.get_all()
    return venta_view.list(ventas)

@venta_dp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        producto_id = request.form['producto_id']
        cantidad = request.form['cantidad']
        fecha_str = request.form['fecha']

        fecha = datetime.strptime(fecha_str,'%Y-%m-%d').date()

        venta = Venta(cliente_id=cliente_id, producto_id=producto_id, cantidad=cantidad,fecha=fecha)
        venta.save()
        return redirect(url_for('venta.index'))

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    return venta_view.create(clientes, productos)


@venta_dp.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    venta = Venta.get_by_id(id)
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        producto_id = request.form['producto_id']
        cantidad = request.form['cantidad']
        fecha_str = request.form['fecha']

        fecha = datetime.strptime(fecha_str,'%Y-%m-%d').date()
        #actualizar
        venta.update(cliente_id=cliente_id, producto_id=producto_id, cantidad=cantidad,fecha=fecha)
        return redirect(url_for('venta.index'))

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    return venta_view.create(clientes, productos)


@venta_dp.route("/delete/<int:id>")
def delete(id):
    venta = Venta.get_by_id(id)
    venta.delete()
    return redirect(url_for('venta.index'))