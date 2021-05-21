import unittest
import xlrd
from ddt import ddt
from ddt import data
from ddt import unpack
from Calc import Calc

def getvalue(file,sheetnub):

    rd = xlrd.open_workbook(filename=file,encoding_override=True)
    sheet = rd.sheet_by_index(sheetnub)

    rows = sheet.nrows
    cols = sheet.ncols

    f = []
    for i in range(rows):
        f.append(sheet.row_values(i))

    return f



f1 = getvalue("测试数据.xls",0)
f2 = getvalue("测试数据.xls",1)
f3 = getvalue("测试数据.xls",2)
f4 = getvalue("测试数据.xls",3)

@ddt
class TestExcle(unittest.TestCase):

    @data(*f1)
    @unpack
    def test_Add(self,a,b,c):
        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(c,sum)

    @data(*f2)
    @unpack
    def test_Reduce(self,a,b,c):
        calc = Calc()
        sum = calc.reduce(a,b)
        self.assertEqual(c, sum)

    @data(*f3)
    @unpack
    def test_Multi(self,a,b,c):
        calc = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(c, sum)

    @data(*f4)
    @unpack
    def test_Division(self,a,b,c):
        calc = Calc()
        sum = calc.division(a,b)
        self.assertEqual(c, sum)
