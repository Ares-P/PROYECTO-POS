class Categoria:

    def __init__(self, CAT_ID, CAT_UUID, CAT_NOMBRE, CAT_DESCRIPCION, CAT_ESTADO):
        self.CAT_ID             = CAT_ID
        self.CAT_UUID           = CAT_UUID
        self.CAT_NOMBRE         = CAT_NOMBRE
        self.CAT_DESCRIPCION    = CAT_DESCRIPCION
        self.CAT_ESTADO         = CAT_ESTADO

    def to_dict(self):
            return{
                "CAT_ID"            : self.CAT_ID,
                "CAT_UUID"          : self.CAT_UUID,
                "CAT_NOMBRE"        : self.CAT_NOMBRE,
                "CAT_DESCRIPCION"   : self.CAT_DESCRIPCION,
                "CAT_ESTADO"        : self.CAT_ESTADO
            }