class DBUtils:
    import pymysql
    # 声明变量:
    dbinfo = ["localhost", "root", "", "上传银行"]
    def setConnect(self,dbinfo):
        self.dbinfo == dbinfo

    con = pymysql.connect(host=dbinfo[0], user=dbinfo[1], password=dbinfo[2], database=dbinfo[3])
    cursor = con.cursor()
    def connect(self):
        import pymysql
        con = pymysql.connect(host=dbinfo[0], user=dbinfo[1], password=dbinfo[2], database=dbinfo[3])
        cursor = con.cursor()
    #增加\删除\改动命令
    def update(self, sql, param) :
        num = self.cursor.execute(sql, param)
        self.con.commit()
        return num

    #查询命令
    def select(self, sql, param) :
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    #关闭连接
    def shutdown(self) :
        self.cursor.close()
        self.con.close()

class Turn:

    #数据库转换为表
    def Db_to_excel(self,dbinfo,table):
        import pymysql
        import xlwt

        wb = xlwt.Workbook()

        #创建一个sheet,名称对应数据库表名称
        sheet = wb.add_sheet((table))

        data = DBUtils().select("select * from "+table,[])
        DBUtils().shutdown()
        for a,b in range(data):
            for c,d in enumerate(b):
                sheet.write(a,c,d)
        wb.save(dbinfo[3]+".xls")

    #Excel转换为数据库
    def Excel_to_db(self,file,shet,dbinfo):
        import pymysql
        import xlrd
        li = file.replace(".xls","").split("\\")  # []
        wb = xlrd.open_workbook(filename=file,encoding_override=True)
        dbinfo[3] = li[len(li) - 1]

        dbu = DBUtils()
        dbu.connect()

        sheet = wb.sheet_by_name(shet)
        rows = sheet.nrows
        cols = sheet.ncols
        for i in range(rows):
            d = sheet.row_values(i)
            s = "INSERT INTO " + shet + " VALUES("
            for j in d:
                s = s +"'"+ str(j) + "',"
            s = s.strip(",")
            sql = s +")"
            print(sql)
            dbu.update(sql,[])
        dbu.shutdown()
file = "G:\\PycharmProjects\\day13\\上传银行.xls"
shet = "bank"
dbinfo = ["localhost","root","","银行"]
turn = Turn()
turn.Excel_to_db(file,shet,dbinfo)