#衣服名称\单价\库存数量
a0 = "羽绒服"
a1=253.6
a2=500
b0 = "牛仔裤"
b1=86.3
b2=600
c0 = "风衣"
c1=96.8
c2=335
d0 = "皮草"
d1=135.9
d2=855
e0 = "T恤"
e1=65.8
e2=632
f0 = "衬衫"
f1=49.3
f2=562

#  1
nam1 = a0
prc1 =a1
num1 =a2
sal1 =10
#  2
nam2 = b0
prc2 =b1
num2 =b2
sal2 =60
#  3
nam3 = c0
prc3 =c1
num3 =c2
sal3 =43
#  4
nam4 = d0
prc4 =d1
num4 =d2
sal4 =63
#  5
nam5 = e0
prc5 =e1
num5 =e2
sal5 =63
#  6
nam6 = f0
prc6 =f1
num6 =f2
sal6 =120
#  7
nam7 = b0
prc7 =b1
num7 =b2
sal7 =72
#  8
nam8 = a0
prc8 =a1
num8 =a2
sal8 =69
#  9
nam9 = b0
prc9 =b1
num9 =b2
sal9 =35
#  10
nam10 =a0
prc10 =a1
num10 =a2
sal10 =140
#  11
nam11 =b0
prc11 =b1
num11 =b2
sal11 =90
#  12
nam12 =d0
prc12 =d1
num12 =d2
sal12 =24
#  13
nam13 =e0
prc13 =e1
num13 =e2
sal13 =45
#  14
nam14 =c0
prc14 =c1
num14 =c2
sal14 =25
#  15
nam15 =b0
prc15 =b1
num15 =b2
sal15 =60
#  16
nam16 =e0
prc16 =e1
num16 =e2
sal16 =129
#  17
nam17 =a0
prc17 =a1
num17 =a2
sal17 =10
#  18
nam18 =c0
prc18 =c1
num18 =c2
sal18 =43
#  19
nam19 =e0
prc19 =e1
num19 =e2
sal19 =63
#  20
nam20 =b0
prc20 =b1
num20 =b2
sal20 =60
#  21
nam21 =d0
prc21 =d1
num21 =d2
sal21 =63
#  22
nam22 =c0
prc22 =c1
num22 =c2
sal22 =60
#  23
nam23 =e0
prc23 =e1
num23 =e2
sal23 =58
#  24
nam24 =b0
prc24 =b1
num24 =b2
sal24 =140
#  25
nam25 =e0
prc25 =e1
num25 =e2
sal25 =48
#  26
nam26 =c0
prc26 =c1
num26 =c2
sal26 =43
#  27
nam27 =d0
prc27 =d1
num27 =d2
sal27 =57
#  28
nam28 =a0
prc28 =a1
num28 =a2
sal28 =10
#  29
nam29 =e0
prc29 =e1
num29 =e2
sal29 =63
#  30
nam30 =c0
prc30 =c1
num30 =c2
sal30 =78
#总销售额
Z1 = sal1 * prc1 + sal2 * prc2 + sal3 * prc3 + sal4 * prc4 + sal5 * prc5 + sal6 * prc6 + sal7 * prc7 + sal8 * prc8 + \
     sal9 * prc9 + sal10 * prc10 + sal11 * prc11 + sal12 * prc12 + sal13 * prc13 + sal14 * prc14 + sal15 * prc15 + \
     sal16 * prc16 + sal17 * prc17 + sal18 * prc18 + sal19 * prc19 + sal20 * prc20 + sal21 * prc21 + sal22 * prc22 + \
     sal23 * prc23 + sal24 * prc24 + sal25 * prc25 + sal26 * prc26 + sal27 * prc27 + sal28 * prc28 + sal29 * prc29 + \
     sal30 * prc30
#羽绒服总销售量
aAll = sal1+sal8+sal10+sal17+sal28
#牛仔裤总销售量
bAll = sal2+sal7+sal9+sal11+sal15+sal20+sal24
#风衣总销售量
cAll = sal3+sal14+sal18+sal22+sal26+sal30
#皮草总销售量
dAll = sal4+sal12+sal21+sal27
#T恤总销售量
eAll = sal5+sal13+sal16+sal19+sal23+sal25+sal29
#衬衫总销售量
fAll =sal6
info1='''
---------------------销售数据--------------------------------
日期 \t\t服装名称\t\t价格/件\t\t库存数量\t\t销售量/每日
-----------------------------------------------------------'''
info2='''
-------------------销售额统计 -------------------------------
服装名称\t\t本月销售量\t\t本月销售额\t\t本月销售占比
-----------------------------------------------------------'''
print(info1)
print("1","\t\t\t",nam1,"\t\t",prc1,"\t\t",num1,"\t\t",sal1)
print("2","\t\t\t",nam2,"\t\t",prc2,"\t\t",num2,"\t\t",sal2)
print("3","\t\t\t",nam3,"\t\t",prc3,"\t\t",num3,"\t\t",sal3)
print("4","\t\t\t",nam4,"\t\t",prc4,"\t\t",num4,"\t\t",sal4)
print("5","\t\t\t",nam5,"\t\t",prc5,"\t\t",num5,"\t\t",sal5)
print("6","\t\t\t",nam6,"\t\t",prc6,"\t\t",num6,"\t\t",sal6)
print("7","\t\t\t",nam7,"\t\t",prc7,"\t\t",num7,"\t\t",sal7)
print("8","\t\t\t",nam8,"\t\t",prc8,"\t\t",num8,"\t\t",sal8)
print("9","\t\t\t",nam9,"\t\t",prc9,"\t\t",num9,"\t\t",sal9)
print("10","\t\t\t",nam20,"\t\t",prc20,"\t\t",num20,"\t\t",sal20)
print("11","\t\t\t",nam21,"\t\t",prc21,"\t\t",num21,"\t\t",sal21)
print("12","\t\t\t",nam22,"\t\t",prc22,"\t\t",num22,"\t\t",sal22)
print("13","\t\t\t",nam23,"\t\t",prc23,"\t\t",num23,"\t\t",sal23)
print("14","\t\t\t",nam24,"\t\t",prc24,"\t\t",num24,"\t\t",sal24)
print("15","\t\t\t",nam25,"\t\t",prc25,"\t\t",num25,"\t\t",sal25)
print("16","\t\t\t",nam26,"\t\t",prc26,"\t\t",num26,"\t\t",sal26)
print("17","\t\t\t",nam27,"\t\t",prc27,"\t\t",num27,"\t\t",sal27)
print("18","\t\t\t",nam28,"\t\t",prc28,"\t\t",num28,"\t\t",sal28)
print("19","\t\t\t",nam29,"\t\t",prc29,"\t\t",num29,"\t\t",sal29)
print("20","\t\t\t",nam20,"\t\t",prc20,"\t\t",num20,"\t\t",sal20)
print("21","\t\t\t",nam21,"\t\t",prc21,"\t\t",num21,"\t\t",sal21)
print("22","\t\t\t",nam22,"\t\t",prc22,"\t\t",num22,"\t\t",sal22)
print("23","\t\t\t",nam23,"\t\t",prc23,"\t\t",num23,"\t\t",sal23)
print("24","\t\t\t",nam24,"\t\t",prc24,"\t\t",num24,"\t\t",sal24)
print("25","\t\t\t",nam25,"\t\t",prc25,"\t\t",num25,"\t\t",sal25)
print("26","\t\t\t",nam26,"\t\t",prc26,"\t\t",num26,"\t\t",sal26)
print("27","\t\t\t",nam27,"\t\t",prc27,"\t\t",num27,"\t\t",sal27)
print("28","\t\t\t",nam28,"\t\t",prc28,"\t\t",num28,"\t\t",sal28)
print("29","\t\t\t",nam29,"\t\t",prc29,"\t\t",num29,"\t\t",sal29)
print("30","\t\t\t",nam30,"\t\t",prc30,"\t\t",num30,"\t\t",sal30)
print("-----------------------------------------------------------")
print("本月销售总额为：",round(Z1,2))
input("按回车键开始计算本月每种衣服的销售统计")
print(info2)
print(a0,"\t\t",aAll,"\t\t\t",round(aAll*a1,2),"\t\t",round((aAll*a1)/Z1*100,2),"%")
print(b0,"\t\t",bAll,"\t\t\t",round(bAll*b1,2),"\t\t",round((bAll*b1)/Z1*100,2),"%")
print(c0,"\t\t",cAll,"\t\t\t",round(cAll*c1,2),"\t\t",round((cAll*c1)/Z1*100,2),"%")
print(d0,"\t\t",dAll,"\t\t\t",round(dAll*d1,2),"\t\t",round((dAll*d1)/Z1*100,2),"%")
print(e0,"\t\t",eAll,"\t\t\t",round(eAll*e1,2),"\t\t",round((eAll*e1)/Z1*100,2),"%")
print(f0,"\t\t",fAll,"\t\t\t",round(fAll*f1,2),"\t\t",round((fAll*f1)/Z1*100,2),"%")
print("-----------------------------------------------------------")