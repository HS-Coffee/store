import xlrd
import xlwt
from day13_遍历工具 import tools

tool = tools()

fname,data = tool.rd("12月份衣服销售数据.xlsx","12月份各种服饰销售情况")
wb = xlwt.Workbook()
sheet1 = wb.add_sheet("12月份各种服饰销售情况")
sheet2 = None

#添加第一行标题
for i,n in enumerate(data[0]):
    sheet1.write(0,i,n)
del data[0]


item = []   #商品种类
su = 0      #销售总额
sall = 0
#获取总销售额 / 商品种类
for a,b in enumerate(data):
    # print(b)
    su = su + b[2]*b[4]
    print(su)
    sall = sall + b[4]
    # print(sall)
    if b[1] not in item:
        item.append(b[1])
su = round(su,1)

#计算日销售量
daysall = sall / len(data)
daysall = round(daysall,0)
print(len(data),"\n",su,"\n",daysall)

for a,b in enumerate(data):
    for c,d in enumerate(b):
        sheet1.write(a+1,c,d)

mark = a+3
sheet1.write(mark,0,"本月销售额为:"+str(su))
sheet1.write(mark,3,"平均日销售量为:"+str(daysall))

# 统计各项本月销售占比,并添加对应新sheet
for j,i in enumerate(item) :
    sa = 0
    for a, b in enumerate(data) :
        if i == b[1] :
            sa = sa + b[4]
    sa = round(sa / sall * 100, 1)
    print(i,sa)
    sheet1.write(mark+j,4,i+"本月销售额占比:"+str(sa)+"%")
    sheet2 = wb.add_sheet(i)
    sheet2.write(0,0,"名称")
    sheet2.write(0, 1, "本月销售量")
    sheet2.write(1, 0, i)
    sheet2.write(1, 1, str(sa)+"%")

wb.save("12月份衣服销售数据x.xls")

