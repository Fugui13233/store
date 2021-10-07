import xlrd
'''
任务1：
    2020年全年的销售统计分析
    全年的销售总额
    每件衣服的销售（件数）占比
    每件衣服的月销售占比
    每件衣服的销售额占比
    最畅销的衣服是那种
    每个季度最畅销的衣服
    全年销量最低的衣服

任务2：
    写个算法，把excel中的数据存在一张表中。
    写个算法，把三国集团的数据，存在Excel表里。
'''

wb=xlrd.open_workbook(filename=r"E:\Python自动化测试\python课程\文件\day09【xlrd】\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
# st=wb.sheet_by_index(0)
# st.cell_value(0,0)
# rows=st.nrows #多少行
# clos=st.ncols #多少列
# print(rows,clos)

# 全年销售额
sum = 0
for a in range(0,12):
    st=wb.sheet_by_index(a)
    rows = st.nrows
    clos = st.ncols
    for i in range(1, rows):
        sum = st.row_values(i)[2] * st.row_values(i)[4] + sum
print("全年销售总额为：",round(sum,2))

# 每件衣服销售量占比
list=["羽绒服","牛仔裤","风衣","皮草","T血","马甲","小西装","休闲裤","卫衣","棉衣","铅笔裤","衬衫","皮衣"]
for e in range(len(list)):
    sum1 = 0
    sum2 = 0
    for b in range(0,12):
        st=wb.sheet_by_index(b)
        rows=st.nrows
        clos=st.ncols
        for d in range(1,rows):
            sum1 = sum1 + st.row_values(d)[4]
            if st.row_values(d)[1]==list[e]:
                sum2=sum2+st.row_values(d)[4]
    print(list[e],"的销售数量为：",sum2,"占比为：",'{:.2%}'.format (sum2/sum1))


# 每件衣服月销售量占比
for g in range(0,12):
    st = wb.sheet_by_index(g)
    rows = st.nrows
    clos = st.ncols
    for f in range(len(list)):
        sum3 = 0
        sum4 = 0
        for h in range(1,rows):
            sum3=sum3+st.row_values(h)[4]
            if st.row_values(h)[1]==list[f]:
                sum4=sum4+st.row_values(h)[4]
        print(g+1,"月",list[f],"销售占比为：",'{:.2%}'.format(sum4/sum3))


# 每件衣服的销售额占比
for j in range(len(list)):
    sum5 = 0
    sum6 = 0
    for k in range(0,12):
        st=wb.sheet_by_index(k)
        rows=st.nrows
        clos=st.ncols
        for l in range(1,rows):
            sum5 = sum5 + st.row_values(l)[2]*st.row_values(l)[4]
            if st.row_values(l)[1]==list[j]:
                sum6=sum6+st.row_values(l)[2]*st.row_values(l)[4]
    print(list[j],"的销售价格为：",round(sum6,2),"占比为：",'{:.2%}'.format(sum6/sum5))


# 最畅销的衣服是哪种
a=0
sum=0
for m in range(len(list)):
    sum7=0
    sum8=0
    for n in range(0,12):
        st=wb.sheet_by_index(n)
        rows=st.nrows
        cols=st.ncols
        for o in range(1,rows):
            sum7+=st.row_values(o)[4]
            if st.row_values(o)[1]==list[m]:
                sum8=sum8+st.row_values(o)[4]
        if sum8>sum:
            sum=sum8
            a=m
    print('最畅销的衣服是',list[a],'{:.2%}'.format(sum/sum7))


# sum=0
# a=0
# for k in range(len(list)):
#     data = 0
#     sum1=0
#     for i in range(0,12):
#         st=wb.sheet_by_index(i)
#         rows=st.nrows
#         cols=st.ncols
#         for j in range(1,rows):
#             sum1+=st.row_values(j)[4]
#             if st.row_values(j)[1]==list[k]:
#                 data=data+st.row_values(j)[4]
#     if sum==0:
#         sum=data
#     if sum>data:
#         sum=data
#         a=k
# print('最不畅销的衣服是',list[a],'{:.2%}'.format(sum/sum1))


# sum=0
# a=0
# b=0
# c=0
# d=0
# sum1=0
# sum2=0
# sum3=0
# for k in range(len(list)):
#     data = 0
#     data1=0
#     data2=0
#     data3=0
#     for i in range(12):
#         st=wb.sheet_by_index(i)
#         rows=st.nrows
#         cols=st.ncols
#         if i>=3 and i<=5:
#             for j in range(1,rows):
#                 sum1+=st.row_values(j)[4]
#                 if st.row_values(j)[1]==list[k]:
#                     data=data+st.row_values(j)[4]
#             if data>sum:
#                 sum=data
#                 a=k
#         elif i>=6 and i<=8:
#             for j in range(1, rows):
#                 if st.row_values(j)[1] == list[k]:
#                     data1 = data1 + st.row_values(j)[4]
#             if data1 > sum1:
#                 sum1 = data1
#                 b = k
#         elif i>=9 and i<=11:
#             for j in range(1, rows):
#                 if st.row_values(j)[1] == list[k]:
#                     data2 = data2 + st.row_values(j)[4]
#             if data2 > sum2:
#                 sum2 = data2
#                 c = k
#         else:
#             for j in range(1, rows):
#                 if st.row_values(j)[1] == list[k]:
#                     data3 = data3 + st.row_values(j)[4]
#             if data3 > sum3:
#                 sum3 = data3
#                 d = k
# print('第一个季度最畅销的衣服',list[a])
# print('第二个季度最畅销的衣服',list[b])
# print('第三个季度最畅销的衣服',list[c])
# print('第四个季度最畅销的衣服',list[d])
# # 每个季度的销量冠军





