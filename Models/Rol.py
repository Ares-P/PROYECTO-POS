class Rol:

    def __init__(self,ROL_ID, ROL_UUID, ROL_NOMBRE, ROL_DESCRIPCION):
        self.ROL_ID           =  ROL_ID
        self.ROL_UUID         =  ROL_UUID
        self.ROL_NOMBRE       =  ROL_NOMBRE
        self.ROL_DESCRIPCION  =  ROL_DESCRIPCION


    def to_dict(self):
        return{
            "ROL_ID"          : self.ROL_ID,
            "ROL_UUID"        : self.ROL_UUID,
            "ROL_NOMBRE"      : self.ROL_NOMBRE,
            "ROL_DESCRIPCION" : self.ROL_DESCRIPCION
        }