class Carrera:
    __codigo=''
    __nombre=''
    __fechainic=''
    __duracion=''
    __titulo=''
    def __init__(self,codigo,nombre,fechainic,duracion,titulo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__fechainic=fechainic
        self.__duracion=duracion
        self.__titulo=titulo
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getFechainic(self):
        return self.__fechainic
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self):
        return self.__titulo