class Usuario:

    def __init__(self, USU_ID, USU_UUID, USU_NOMBRE, USU_USUARIO, USU_CONTRASENA, USU_ESTADO):
        self.USU_ID         = USU_ID
        self.USU_UUID       = USU_UUID
        self.USU_NOMBRE     = USU_NOMBRE
        self.USU_USUARIO    = USU_USUARIO
        self.USU_CONTRASENA = USU_CONTRASENA
        self.USU_ESTADO     = USU_ESTADO




    def to_dict(self):
        return{
            "USU_ID"         : self.USU_ID,
            "USU_UUID"       : self.USU_UUID,
            "USU_NOMBRE"     : self.USU_NOMBRE,
            "USU_USUARIO"    : self.USU_USUARIO,
            "USU_CONTRASENA" : self.USU_CONTRASENA,
            "USU_ESTADO"     : self.USU_ESTADO
        }