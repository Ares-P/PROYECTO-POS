class Detalle_Pedido:

    def __init__(self, DET_PED_ID, DET_PED_UUID, DET_PED_CANTIDAD, DET_PED_PRECIO_UNITARIO, DET_PED_SUBTOTAL):
        self.DET_PED_ID                 = DET_PED_ID
        self.DET_PED_UUID               = DET_PED_UUID
        self.DET_PED_CANTIDAD           = DET_PED_CANTIDAD
        self.DET_PED_PRECIO_UNITARIO    = DET_PED_PRECIO_UNITARIO
        self.DET_PED_SUBTOTAL           = DET_PED_SUBTOTAL


    def to_dict(self):
            return{
                "DET_PED_ID"               : self.DET_PED_ID,
                "DET_PED_UUID"             : self.DET_PED_UUID,
                "DET_PED_CANTIDAD"         : self.DET_PED_CANTIDAD,
                "DET_PED_PRECIO_UNITARIO"  : self.DET_PED_PRECIO_UNITARIO,
                "DET_PED_SUBTOTAL"         : self.DET_PED_SUBTOTAL
            }