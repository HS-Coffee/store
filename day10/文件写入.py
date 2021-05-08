'''
    存储数据：
        1.变量
        2.元组，列表，字典，集合
        3.数据库：mysql   (pymysql)
        4.文件读写：.txt  （python提供了对文件读写）
    1. 打开文件
        模式：
            r、w、b(图片、MP3、mp4),a(附加)，+可读可写
    2. 写入数据
    3. 关闭资源
'''
# 打开 : 句柄，把柄
f = open(file="../../狼腾资料/python自动化测试/Project_Doc/day10/代码/day10/古诗.txt", mode="w+", encoding="utf-8")

# 写个数据
f.write("咏鹅")
f.write("【烙饼王】")
f.write("鹅鹅鹅，曲项向天歌。")

# print(f.read())  # 禁止使用
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines()) # ["静夜思","【李白】",""]

# 关闭资源
f.close()

# 任务：将《静夜思》  拷贝一份  到b.txt文件里














