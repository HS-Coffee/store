class  Mankind:
    __na = ""
    __age = 0
    __sex = ""
    def getNa(self):
        return self.__na
    def getAge(self):
        return self.__age
    def getSex(self):
        return self.__sex
    def setNa(self,name):
        self.__na = name
    def setAge(self,age):
        self.__age = age
    def setSex(self,sex):
        self.__sex = sex

class Clas(Mankind):
    __job = ""
    def getJob(self):
        return self.__job
    def setJob(self,job):
        self.__job = job
    def work(self):
        print(self.getJob(),self.getNa(),"正在工作")
class Student(Clas):
    __ID = ""
    def getID(self):
        return self.__ID
    def setID(self,ID):
        self.__ID = ID
    def study(self):
        print(self.getNa(),"正在学习")
    def say(self):
        print(self.getNa(),"正在唱歌")

class Test:
    def test(self):
        st = Student()
        st.setNa("张三")
        st.setAge(25)
        st.setID("6969")
        st.setSex("纯爷们")
        st.setJob("上街的傻子")
        st.work()
        st.say()
        st.study()
test = Test()
test.test()