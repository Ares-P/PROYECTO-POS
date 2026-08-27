class Caja:

    def __init__(self, CAJ_ID, CAJ_UUID, CAJ_ID_CAJA, CAJ_FECHA_APERTURA, CAJ_ESTADO, CAJ_SALDO_INICIAL, CAJ_SALDO_FINAL, CAJ_FECHA_CIERRE):
        self.CAJ_ID                = CAJ_ID
        self.CAJ_UUID              = CAJ_UUID
        self.CAJ_ID_CAJA           = CAJ_ID_CAJA
        self.CAJ_FECHA_APERTURA    = CAJ_FECHA_APERTURA
        self.CAJ_ESTADO            = CAJ_ESTADO
        self.CAJ_SALDO_INICIAL     = CAJ_SALDO_INICIAL
        self.CAJ_SALDO_FINAL       = CAJ_SALDO_FINAL
        self.CAJ_FECHA_CIERRE      = CAJ_FECHA_CIERRE


    def to_dict(self):
            return{
                "CAJ_ID"               : self.CAJ_ID,
                "CAJ_UUID"             : self.CAJ_UUID,
                "CAJ_ID_CAJA"          : self.CAJ_ID_CAJA,
                "CAJ_FECHA_APERTURA"   : self.CAJ_FECHA_APERTURA,
                "CAJ_ESTADO"           : self.CAJ_ESTADO,
                "CAJ_SALDO_INICIAL"    : self.CAJ_SALDO_INICIAL,
                "CAJ_SALDO_FINAL"      : self.CAJ_SALDO_FINAL,
                "CAJ_FECHA_CIERRE"     : self.CAJ_FECHA_CIERRE
            }