import xlrd
file_path = r"C:\Users\Pratik Giri\Downloads\Orders-With Nulls.xlsx"
# To open the Workbook
book = xlrd.open_workbook(file_path)
sheet = book.sheet_by_index(0)
# For row 0 and column 0
sheet.cell_value(0, 0)