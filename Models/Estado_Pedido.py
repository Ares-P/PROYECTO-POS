class Estado_Pedido:

    def __init__(self, EST_PED_ID, EST_PED_UUID, EST_PED_NOMBRE, EST_PED_DESCRIPCION ):
        self.EST_PED_ID              = EST_PED_ID
        self.EST_PED_UUID            = EST_PED_UUID
        self.EST_PED_NOMBRE          = EST_PED_NOMBRE
        self.EST_PED_DESCRIPCION     = EST_PED_DESCRIPCION


    def to_dict(self):
            return{
                "EST_PED_ID"             : self.EST_PED_ID,
                "EST_PED_UUID"           : self.EST_PED_UUID,
                "EST_PED_NOMBRE"         : self.EST_PED_NOMBRE,
                "EST_PED_DESCRIPCION"    : self.EST_PED_DESCRIPCION
            }