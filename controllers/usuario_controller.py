from flask import request, redirect, url_for, blueprints, Blueprint
from models.usuario_model import Usuario
from views import usuario_view

usuario_dp = Blueprint('usuario',__name__,url_prefix="/usuarios")

@usuario_dp.route("/")
def index():
    #recupera todos los registros de la tabla usuarios en forma de objeto
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_dp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        usuario = Usuario(nombre, username,password,rol)
        usuario.save()
        return redirect(url_for('usuario.index'))
    

    return usuario_view.create()


@usuario_dp.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']
        #actualizar
        usuario.update(nombre=nombre, username=username, password=password, rol=rol)
        return redirect(url_for('usuario.index'))
    
    return usuario_view.edit(usuario)

@usuario_dp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))