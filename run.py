from flask import Flask, request, render_template
from controllers import usuario_controller
from controllers import cliente_controller
from controllers import producto_controller
from controllers import venta_controller
from database import db

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

app.register_blueprint(usuario_controller.usuario_dp)
app.register_blueprint(cliente_controller.cliente_dp)
app.register_blueprint(producto_controller.producto_dp)
app.register_blueprint(venta_controller.venta_dp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return(dict(is_active=is_active))

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)

    