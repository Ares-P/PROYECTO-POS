class Metodo_pago:

    def __init__(self, MET_PAG_ID, MET_PAG_UUID, MET_PAG_NOMBRE, MET_PAG_ESTADO, MET_PAG_DESCRIPCION ):
        self.MET_PAG_ID              = MET_PAG_ID
        self.MET_PAG_UUID            = MET_PAG_UUID
        self.MET_PAG_NOMBRE          = MET_PAG_NOMBRE
        self.MET_PAG_ESTADO          = MET_PAG_ESTADO
        self.MET_PAG_DESCRIPCION     = MET_PAG_DESCRIPCION


    def to_dict(self):
            return{
                "MET_PAG_ID"             : self.MET_PAG_ID,
                "MET_PAG_UUID"           : self.MET_PAG_UUID,
                "MET_PAG_NOMBRE"         : self.MET_PAG_NOMBRE,
                "MET_PAG_ESTADO"         : self.MET_PAG_ESTADO,
                "MET_PAG_DESCRIPCION"    : self.MET_PAG_DESCRIPCION
            }