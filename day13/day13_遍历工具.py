class tools:

    def wt(self,file,sheet,data):
        import xlwt
        wb = xlwt.Workbook()
        sheet = wb.add_sheet(sheet)
        for a,b in enumerate(data):
            for c,d in enumerate(b):
                sheet.write(a,c,d)
        wb.save(file+".xls")

    def rd(self,file,sheet):
        import xlrd
        li = file.replace(".xls", "").split("\\")  # []
        fname = li[len(li) - 1]
        wb = xlrd.open_workbook(filename=file,encoding_override=True)
        sheet = wb.sheet_by_name(sheet)
        rows = sheet.nrows
        cols = sheet.ncols
        data = []
        for i in range(rows) :
            data.append(sheet.row_values(i))
        return fname,data


