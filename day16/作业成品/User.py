#用户类
class User:
    __account = ""
    __username = ""
    __password = ""
    __money = 0
    __address = None
    def setAccount(self,account):
        self.__account = account
    def setUsername(self,username):
        self.__username = username
    def setPassword(self,password):
        self.__password = password
    def setAddress(self,address):
        self.__address = address
    def setMoney(self,money):
        self.__money = money
        return money
    def getAccount(self):
        return self.__account
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getMoney(self):
        return self.__money
    def getAddress(self):
        return self.__address
