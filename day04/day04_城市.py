ctiy = ["北京","上海","广东","深圳","天津","苏州",
        "重庆","杭州","无锡","青岛","佛山","武汉",
        "大连","成都","沈阳","宁波","南京","唐山",
        "东莞","烟台","郑州","济南"]
ctiy.remove("广东")
ctiy.insert(1,"广东")
print(ctiy)

GDP=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
count = 0
Sum = 0
while count < len(GDP) :
    Sum = GDP[count] + Sum
    count = count + 1
    print("当前循环为第",count,"次\t平均GDP为",round(Sum/count,2))
print("_-_-_-_-_-_-_-_-结束_-_-_-_-_-_-_-_-")