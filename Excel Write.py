'''Excel Write - Writes a dictionary to an Excel file.
This program also performs some text formatting and Excel math actions. '''

import xlsxwriter


def xlsx_write():
    workbook = xlsxwriter.Workbook('Excel_Write.xlsx')                #New Excel file that we are creating and writing to
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})                        #Assigning bold font to the variable 'bold'
    money = workbook.add_format({'num_format': '$#,##0'})             #Assigning a dollar sign to 'money'
    italic_bold = workbook.add_format({'italic': True, 'bold':True})  #Assigning bold and italic to 'italic_bold'

    worksheet.write('A1', 'Cost of Activities',italic_bold)           #Writes heading 'Cost of Activities' in bold and italic in cell A1
    worksheet.write('A2', 'Task', bold)                               #Writes label 'Task' in bold in cell A2
    worksheet.write('B2', 'Cost', bold)                               #Writes label 'Cost' in bold in cell B2


    Tasks = (['Movie', 20], ['Food', 15], ['Shopping', 45], ['Bills', 60])   #Dictionary of Tasks and Costs for each task

    row = 2                                                           #Starting at row 1
    col = 0                                                           #Starting at column 0

    for item, time in Tasks:                                          #Iterates through each task and cost in dictionary
        worksheet.write(row, col, item)                               #Writes each task to column A
        worksheet.write(row, col + 1, time, money)                    #Writes each cost to column B with a dollar sign
        row += 1                                                      #Up increments the row for the next set of tasks and costs

    worksheet.write(row, 0, 'Total', bold)                            #Writes in bold 'Total' on the next line
    worksheet.write(row, 1, '=SUM(B2:B6)', money)                     #Adds up the costs and displays them with a dollar sign
    workbook.close()                                                  #Close Excel File

    print("Your Excel file 'Excel_Write.xlsx' has been written.")

xlsx_write()