import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
a=wb.get_sheet_names()
print(a)
sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
type(sheet)
print(type(sheet))
print(sheet.title)
anotherSheet = wb.get_active_sheet()
print(anotherSheet)
