import xlrd

workbook = xlrd.open_workbook('first_file.xlsx')

#get sheet by index
worksheet = workbook.sheet_by_index(0)

#find total no of rows
rows = worksheet.nrows

#read rows returns tuple

for row in range (rows):
    first_col,second_col = worksheet.row_values(row)
    print(first_col, ' ', second_col)


