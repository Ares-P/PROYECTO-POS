class Producto:

    def __init__(self, PRO_ID, PRO_UUID, PRO_NOMBRE, PRO_DESCRIPCION, PRO_PRECIO, PRO_DISPONIBLE, PRO_ESTADO, PRO_CAT_ID ):
        self.PRO_ID             = PRO_ID
        self.PRO_UUID           = PRO_UUID
        self.PRO_NOMBRE         = PRO_NOMBRE
        self.PRO_DESCRIPCION    = PRO_DESCRIPCION
        self.PRO_PRECIO         = PRO_PRECIO
        self.PRO_DISPONIBLE     = PRO_DISPONIBLE
        self.PRO_ESTADO         = PRO_ESTADO
        self.PRO_CAT_ID         = PRO_CAT_ID

    def to_dict(self):
            return{
                "PRO_ID"            : self.PRO_ID,
                "PRO_UUID"          : self.PRO_UUID,
                "PRO_NOMBRE"        : self.PRO_NOMBRE,
                "PRO_DESCRIPCION"   : self.PRO_DESCRIPCION,
                "PRO_PRECIO"        : self.PRO_PRECIO,
                "PRO_DISPONIBLE"    : self.PRO_DISPONIBLE,
                "PRO_ESTADO"        : self.PRO_ESTADO,
                "PRO_CAT_ID"        : self.PRO_CAT_ID
            }