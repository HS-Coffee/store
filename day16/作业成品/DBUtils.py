class DBTools :
    import pymysql
    # 声明变量:
    host = "localhost"
    user = "root"
    password = ""
    database = "银行"

    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()

    def update(self, sql, param) :
        num = self.cursor.execute(sql, param)
        self.con.commit()
        return num

    def select(self, sql, param) :
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def shutdown(self) :
        self.cursor.close()
        self.con.close()