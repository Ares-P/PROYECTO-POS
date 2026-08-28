class Pago:

    def __init__(self, PAG_ID, PAG_UUID, PAG_ID_PAGO, PAG_REFERENCIA, PAG_ESTADO, PAG_FECHA_PAGO, PAG_VALOR_PAGADO, PAG_PED_ID, PAG_MET_PAG_ID,  PAG_CAJ_ID):
        self.PAG_ID               = PAG_ID
        self.PAG_UUID             = PAG_UUID
        self.PAG_ID_PAGO          = PAG_ID_PAGO
        self.PAG_REFERENCIA       = PAG_REFERENCIA
        self.PAG_ESTADO           = PAG_ESTADO
        self.PAG_FECHA_PAGO       = PAG_FECHA_PAGO
        self.PAG_VALOR_PAGADO     = PAG_VALOR_PAGADO
        self.PAG_PED_ID           = PAG_PED_ID
        self.PAG_MET_PAG_ID       = PAG_MET_PAG_ID
        self.PAG_CAJ_ID           = PAG_CAJ_ID


    def to_dict(self):
            return{
                "PAG_ID"              : self.PAG_ID,
                "PAG_UUID"            : self.PAG_UUID,
                "PAG_ID_PAGO"         : self.PAG_ID_PAGO,
                "PAG_REFERENCIA"      : self.PAG_REFERENCIA,
                "PAG_ESTADO"          : self.PAG_ESTADO,
                "PAG_FECHA_PAGO"      : self.PAG_FECHA_PAGO,
                "PAG_VALOR_PAGADO"    : self.PAG_VALOR_PAGADO,
                "PAG_PED_ID"          : self.PAG_PED_ID,
                "PAG_MET_PAG_ID"      : self.PAG_MET_PAG_ID,
                "PAG_CAJ_ID"          : self.PAG_CAJ_ID
            }