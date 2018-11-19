import xlrd


def open_excel(file='file.xls'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception as e:
		print(str(e))


# excel_table_byname函数用于打开excel文件 return list
def excel_table_byname(file=r'C:\Users\bobbr\Desktop\装载问题测试1.xls',
                       colnameindex=0,
                       by_name='Sheet2'):
	# 输入表格文件路径|第一行为表头|Sheet1
	data = open_excel(file)
	table = data.sheet_by_name(by_name)  # 获得表格
	nrows = table.nrows  # 拿到总共行数
	colnames = table.row_values(colnameindex)  # 某一行数据 ['序号', '长', '宽','高','数量']
	list = []
	for rownum in range(1, nrows):  # 也就是从Excel第二行开始，第一行表头不算
		row = table.row_values(rownum)
		app = []
		for i in range(0, len(colnames)):
			app.append(int(row[i]))
		list.append(app)
	return list

def main():
    #输出结果文字版本
    tables = OkStart()
    tables = EasyWatch(tables)
    #print(tables)
    for row in tables:
        print(row)
    print(len(tables))

if __name__ =="__main__":
    main()