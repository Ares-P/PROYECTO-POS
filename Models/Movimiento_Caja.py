class Movimiento_Caja:

    def __init__(self, MOV_CAJ_ID, MOV_CAJ_UUID, MOV_CAJ_TIPO_MOVIMIENTO, MOV_CAJ_MONTO, MOV_CAJ_DESCRIPCION, MOV_CAJ_FECHA_HORA, MOV_CAJ_CAJ_ID):
        self.MOV_CAJ_ID                 = MOV_CAJ_ID
        self.MOV_CAJ_UUID               = MOV_CAJ_UUID
        self.MOV_CAJ_TIPO_MOVIMIENTO    = MOV_CAJ_TIPO_MOVIMIENTO
        self.MOV_CAJ_MONTO              = MOV_CAJ_MONTO
        self.MOV_CAJ_DESCRIPCION        = MOV_CAJ_DESCRIPCION
        self.MOV_CAJ_FECHA_HORA         = MOV_CAJ_FECHA_HORA
        self.MOV_CAJ_CAJ_ID             = MOV_CAJ_CAJ_ID


    def to_dict(self):
            return{
                "MOV_CAJ_ID"                : self.MOV_CAJ_ID,
                "MOV_CAJ_UUID"              : self.MOV_CAJ_UUID,
                "MOV_CAJ_TIPO_MOVIMIENTO"   : self.MOV_CAJ_TIPO_MOVIMIENTO,
                "MOV_CAJ_MONTO"             : self.MOV_CAJ_MONTO,
                "MOV_CAJ_DESCRIPCION"       : self.MOV_CAJ_DESCRIPCION,
                "MOV_CAJ_FECHA_HORA"        : self.MOV_CAJ_FECHA_HORA,
                "MOV_CAJ_CAJ_ID"            : self.MOV_CAJ_CAJ_ID
            }