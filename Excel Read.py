''' Excel Read - Reads and Excel file and adds it to a local list.
The extra commas, quotation marks, and text that is imported along with the data
is removed, and the data is converted back to the string, integer, or boolean
data type that it originally was. '''

import xlrd

ex_sheet = []                                           #My test list
ex_sheet_two = []
book = xlrd.open_workbook("myfile.xlsx")                #Open Excel file
print ("The number of worksheets is", book.nsheets)
print ("Worksheet name(s):", book.sheet_names())
sh = book.sheet_by_index(0)                             #sh = sheet we are working on




def temp_list():
    print ('Line by line read in from Excel:')
    for rx in range(sh.nrows):                              #For each row
        print (sh.row(rx))
        ex_sheet.append(sh.row(rx))                         #Add row to my test list as a new list
    print()
    print('Entire sheet read in from Excel:')
    print (ex_sheet)                                        #Print worksheet that has been read in from Excel

    sort_sheet()


def sort_sheet():                                       #Sorting function
    global ex_sheet
    global ex_sheet_two                                 #My second test list
    for word in ex_sheet:                               #For each list in my test list
        ex_word = []                                    #Establishes list for my temporary sublists
        for cell in word:                               #For each item in my sublists
            new_cell = str(cell)                        #Converts info to strings to remove excess words

            if "bool:" in str(cell):                        #If the word 'bool:' is found
                newest_cell = new_cell.replace("bool:",'')  #Remove and replace with nothing
                ex_word.append(newest_cell == '1')           #Add newly made True or False to temporary sublist

            elif "number:" in str(cell):                        #Repeat steps in "bool:" for "number:"
                newest_cell = new_cell.replace("number:",'')
                newest_cell = newest_cell.replace(".0",'')
                ex_word.append(int(newest_cell))

            elif "text:" in str(cell):                          #Repeat steps in "bool:" for "text:"
                newest_cell = new_cell.replace("text:",'')
                newest_cell = newest_cell.replace("'",'')
                ex_word.append(str(newest_cell))

            elif "empty:" in str(cell):                                            #Repeat here is desired
                newest_cell = new_cell.replace("empty:''",'no entry provided')
                ex_word.append(str(newest_cell))

            else:                                   #Add to temporary sublist is no additional wordage found
                newest_cell = str(new_cell)
                ex_word.append(str(newest_cell))
        ex_sheet_two.append(list(ex_word))          #Add temporary sublist to list
                                                    #Sublist cleared after this operation

    print()
    print('Cleaned up version of Excel sheet read into Python.')
    print (ex_sheet_two)                            #Print final list


temp_list()
