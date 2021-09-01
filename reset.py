import openpyxl

workbook = openpyxl.load_workbook('Tech Club.xlsx')
sheet = workbook.active


for i in range(2, 195):
    sheet.cell(row=i, column=12).value = -1


workbook.save('Tech Club.xlsx')
