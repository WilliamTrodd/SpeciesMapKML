#-------------------------------------------------------------------------------
# Name:        bat_map_cli
# Purpose:
#
# Author:      William Trodd
#
# Created:     09/07/2018
# Copyright:   (c) willi_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import openpyxl

def get_sheet(path):
    wb = openpyxl.load_workbook(path, data_only = True)
    return wb

def display_sheets(workbook):
    counter = 1
    sheet_list = []
    for sheet in workbook:
        sheet_list.append(sheet.title)
        print(counter, sheet_list[counter-1])
        counter += 1
    return sheet_list


def load_sheet(workbook, sheet):
    return(workbook[sheet])

def show_columns(sheet):
    current_cell = ['A','1']
    cell_string = current_cell[0]+current_cell[1]

    column_headers = []
    counter = 1
    while sheet[cell_string].value != None:

        column_headers.append(sheet[cell_string].value)
        print(counter, column_headers[counter-1])

        current_cell[0] = chr(ord(current_cell[0])+1)

        cell_string = current_cell[0]+current_cell[1]
        counter += 1

    return(column_headers)


def get_column_items(sheet, column_num):
    column_items = []
    for row in sheet.iter_rows(min_row = 2):
        item = row[column_num].value
        if item != None and item != 0:
            if column_items == []:
                column_items.append(item)
            elif item not in column_items:
                column_items.append(item)
    return column_items



def main():
    wb_path = input("Please enter the sheet file path:")

    wb = get_sheet(wb_path)
    sheet_list = display_sheets(wb)

    sheet_num = int(input("Please enter the sheet number"))

    sheet = load_sheet(wb, sheet_list[sheet_num-1])

    column_headers = show_columns(sheet)

    columns_str = input("Please enter the columns whose items you wish to see (comma-separated):")

    columns = columns_str.split(",")

    for column in columns:
        column_items = get_column_items(sheet, int(column) -1 )
        print(column_items)


main()




