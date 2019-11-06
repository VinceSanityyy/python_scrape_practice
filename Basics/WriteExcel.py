from xlsxwriter import Workbook

#create workbook
workbook = Workbook('first_file.xlsx')

#add worksheet
worksheet = workbook.add_worksheet()

#write function row column data
for row in range(20):
    worksheet.write(row,0,'Row Number')
    worksheet.write(row,1,row)


workbook.close()
