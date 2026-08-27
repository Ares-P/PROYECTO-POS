class Pedido:

    def __init__(self, PED_ID, PED_UUID, PED_DESCUENTO, PED_IMPUESTO, PED_TOTAL, PED_FECHA_HORA, PED_NUMERO_ORDEN, PED_METODO_ENTREGA, PED_SUBTOTAL ):
        self.PED_ID                 = PED_ID
        self.PED_UUID               = PED_UUID
        self.PED_DESCUENTO          = PED_DESCUENTO
        self.PED_IMPUESTO           = PED_IMPUESTO
        self.PED_TOTAL              = PED_TOTAL
        self.PED_FECHA_HORA         = PED_FECHA_HORA
        self.PED_NUMERO_ORDEN       = PED_NUMERO_ORDEN
        self.PED_METODO_ENTREGA     = PED_METODO_ENTREGA
        self.PED_SUBTOTAL           = PED_SUBTOTAL



    def to_dict(self):
            return{
                "PED_ID"                : self.PED_ID,
                "PED_UUID"              : self.PED_UUID,
                "PED_DESCUENTO"         : self.PED_DESCUENTO,
                "PED_IMPUESTO"          : self.PED_IMPUESTO,
                "PED_TOTAL"             : self.PED_TOTAL,
                "PED_FECHA_HORA"        : self.PED_FECHA_HORA,
                "PED_NUMERO_ORDEN"      : self.PED_NUMERO_ORDEN,
                "PED_METODO_ENTREGA"    : self.PED_METODO_ENTREGA,
                "PED_SUBTOTAL"          : self.PED_SUBTOTAL
            }