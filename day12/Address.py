#地址类
class Address:
    __country = ""
    __province = ""
    __street = ""
    __door = ""
    def setCountry(self,country):
        self.__country = country
    def setProvince(self,province):
        self.__province = province
    def setStreet(self,street):
        self.__street = street
    def setDoor(self,door):
        self.__door = door
    def getCountry(self):
        return self.__country
    def getProvince(self):
        return self.__province
    def getStreet(self):
        return self.__street
    def getDoor(self):
        return  self.__door