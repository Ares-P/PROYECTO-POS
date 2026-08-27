class Mesa:

    def __init__(self, MES_ID, MES_UUID, MES_NOMBRE, MES_CAPACIDAD, MES_ESTADO):
        self.MES_ID           = MES_ID
        self.MES_UUID         = MES_UUID
        self.MES_NOMBRE       = MES_NOMBRE
        self.MES_CAPACIDAD    = MES_CAPACIDAD
        self.MES_ESTADO       = MES_ESTADO


    def to_dict(self):
            return{
                "MES_ID"             : self.MES_ID,
                "MES_UUID"           : self.MES_UUID,
                "MES_NOMBRE"         : self.MES_NOMBRE,
                "MES_CAPACIDAD"      : self.MES_CAPACIDAD,
                "MES_ESTADO"         : self.MES_ESTADO
            }