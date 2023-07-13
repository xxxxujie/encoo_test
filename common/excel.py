import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def read_excel_dict(file, sheet_name="Sheet1"):
    workbook = openpyxl.load_workbook(file)
    # 获取表格，指定sheet变量类型
    sheet: Worksheet = workbook[sheet_name]
    rows = list(sheet.values)

    cases = rows[1:]
    # 标题
    title = rows[0]
    rows = [dict(zip(title, row)) for row in cases]
    return rows
