from DBUtils import DBTools

db = DBTools()


class Logic:
    #新增逻辑
    def xinZeng(self,account,username,password,country,province,street,door,):
        sql = "select count(*) from bank"
        users = db.select(sql, [])
        if len(users) >= 100 :
            return 3
        users = ()
        sql = "select account from bank where account = %s"
        parame = [account]
        users = db.select(sql, parame)
        if len(users) != 0 :
            return 2
        else :
            users = ()
            sql = "INSERT INTO bank VALUES(%s,%s,%s,%s,%s,%s,%s,0,'中国工商银行-昌平支行');"
            param = [account, username, password, country, province, street, door]
            num = db.update(sql, param)
            if num >= 1 :
                return 1
            else :
                return 4

    #存钱逻辑
    def cunQian(self,account,money):
        sql = "select account from bank where account  = %s ;"
        parame = [account]

        users = db.select(sql, parame)
        if len(users) != 0 :
            sql = "UPDATE bank SET money = money + %s WHERE account = %s ;"
            parame = [money, account]
            db.update(sql, parame)
            return True
        else :
            return False

    #取钱逻辑
    def quQian(self,take_user,take_password,take_money):
        # 判断 用户存在
        sql = "select account from bank where account = %s;"
        parame = [take_user]
        users = db.select(sql, parame)
        if len(users) != 0 :
            # 判断 密码正确
            users = ()
            sql = "select account from bank where account = %s and password = %s;"
            parame = [take_user, take_password]
            users = db.select(sql, parame)
            if len(users) != 0 :
                # 判断 余额足够
                users = ()
                sql = "select account from bank where account = %s and password = %s and money >= %s ;"
                parame = [take_user, take_password, take_money]
                users = db.select(sql, parame)
                if len(users) != 0 :
                    # 满足 扣钱
                    users = ()
                    sql = "update bank set money = money - %s where account = %s "
                    parame = [take_money, take_user]
                    db.update(sql, parame)
                    return 0  # 成功 返回值0
                else :
                    return 3  # 钱不够返回3
            else :
                return 2  # 用户密码不正确返回2
        else :
            return 1  # 返回1

    #转账逻辑
    def zhuanZhang(self,send_user,send_userPw,send_to,send_money):
        sql = "select account from bank where account = %s or account = %s"
        parame = [send_user, send_to]
        users = db.select(sql, parame)
        if len(users) == 2 :
            users = ()
            sql = "select account from bank where account = %s and password = %s"
            parame = [send_user, send_userPw]
            users = db.select(sql, parame)
            if len(users) == 1 :
                users = ()
                sql = "select account from bank where account = %s and password = %s and money >= %s"
                parame = [send_user, send_userPw, send_money]
                users = db.select(sql, parame)
                if len(users) == 1 :
                    sql = "update bank set money = (money - %s) where account = %s ;"
                    parame = [send_money, send_user]
                    db.update(sql, parame)
                    sql = "update bank set money = (money + %s) where account = %s ;"
                    parame = [send_money, send_to]
                    db.update(sql, parame)
                    return 0
                else :
                    return 3
            else :
                return 2
        else :
            return 1
class Test:
    def quQian(self,account,password,money):
        logic = Logic()
        info = logic.quQian(account,password,money)
        print(info)


test = Test()
test.quQian("87DxvnZT","111111","50")