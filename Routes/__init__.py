from .Producto import producto_bp
from .Categoria import categoria_bp
from .Usuario import usuario_bp
from .Pedido import pedido_bp
from .Pago import pago_bp
from .Caja import caja_bp
from .Mesa import mesa_bp
from .Rol import rol_bp
from .Metodo_pago import metodo_pago_bp
from .Estado_Pedido import estado_pedido_bp
from .Detalle_Pedido import detalle_pedido_bp
from .Movimiento_Caja import movimiento_caja_bp


def loadRoutes(app):

    app.register_blueprint(producto_bp, url_prefix="/productos")
    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(usuario_bp, url_prefix="/usuarios")
    app.register_blueprint(pedido_bp, url_prefix="/pedidos")
    app.register_blueprint(pago_bp, url_prefix="/pagos")
    app.register_blueprint(caja_bp, url_prefix="/cajas")
    app.register_blueprint(mesa_bp, url_prefix="/mesas")
    app.register_blueprint(rol_bp, url_prefix="/roles")
    app.register_blueprint(metodo_pago_bp, url_prefix="/metodos-pago")
    app.register_blueprint(estado_pedido_bp, url_prefix="/estados-pedido")
    app.register_blueprint(detalle_pedido_bp, url_prefix="/detalles-pedido")
    app.register_blueprint(movimiento_caja_bp, url_prefix="/movimientos-caja")