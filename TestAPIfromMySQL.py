# ryan robitaille 12/6/2012
# simple Tableau Data Extract creation from a single microsoft sql server sql statement

import dataextract as tde # saves some typing, cause i'm a lazy fucker
import os, time , mysql.connector # for file manipulation, script timing (not necc), database access!

###################### FOR YOUR PARAMETERS, SON! ######################
tdefilename = 'ufo_datas.tde'
sql = "select OrderID, Order_Priority, Order_Quantity from superstore;"
sql1 = "select OrderID, Order_Priority, Order_Quantity from superstore where ;"# whatever
sqlserverhost = '10.26.171.33'
sqlusername = 'root'
sqlpassword = ''
sqldatabase = 'superstore'
rowoutput = False # for DEBUGGING data errors / slows shit down 10X however
###################### FOR YOUR PARAMETERS, SON! ######################

dotsevery = 75

start_time = time.time() # simple timing for test purposes

mssql_db = mysql.connector.connect(host=sqlserverhost, user=sqlusername, password=sqlpassword, database=sqldatabase) # as_dict very important
mssql_cursor = mssql_db.cursor(dictionary = True)
mssql_cursor1 = mssql_db.cursor(dictionary = True)
mssql_cursor.execute(sql)
mssql_cursor1.execute(sql1)

# for row in mssql_cursor:
#     print row['OrderID']



# try:  # Just for testing purposes and re-running
#     tdefile = tde.Extract('test.tde') #in CWD
# except: 
#     os.system('del test.tde')
#     os.system('del DataExtract.log')
#     tdefile = tde.Extract('test.tde')

# tableDef = tde.TableDefinition() #create a new table def

# # using integers for now because the literal defs are not in the python module code
# tableDef.addColumn("OrderID", 7) #INTEGER
# #tableDef.addColumn("OrderDate", 12) #Date
# #tableDef.addColumn("Order_Priority", 15) #Char_string
# tableDef.addColumn("Order_Quantity", 7) #INT
# # tableDef.addColumn("field_type13", 7) #DATETIME
# # tableDef.addColumn("field_type14", 14) #DURATION
# # tableDef.addColumn("field_type15", 15) #CHAR_STRING
# # tableDef.addColumn("field_type16", 16) #UNICODE_STRING

# # ok, lets print out the table def, just for shits and giggles
# for c in range(0,tableDef.getColumnCount()):
#     print 'Column: ' + str(tableDef.getColumnName(c)) + ' Type: ' + str(tableDef.getColumnType(c))

# # lets add the new def as a table in the extract
# tabletran = tdefile.addTable("Extract",tableDef) 
# # why table NEEDS to be called 'Extract' is beyond me

# rowsinserted = 1
# count = 0
# # let's create a bunch of rows! wheeeeee!
# for row in mssql_cursor:
#         newrow = tde.Row(tableDef)
#         #newrow.setNull(0) #column
#         newrow.setInteger(0,row['OrderID']) #column, value
#         #newrow.setDate(1, 2012, 12, 2) #column, value
#         #newrow.setCharString(2,row['Order_Priority']) #column, value (1/0)
#         newrow.setInteger(1, row['Order_Quantity']) #column, y,m,d
#         # newrow.setDateTime(4, 2012, 12, 2, 18, 25, 55, 0000) #column, y,m,d,h,m,s,frac
#         # newrow.setDuration(5, 6, 18, 25, 55, 0000) #column, d,h,m,s,frac
#         # newrow.setCharString(6, 'Character String') #column, 'value'
#         # newrow.setString(7, 'Unicode String!') #column, 'value'
#         rowsinserted = rowsinserted + 1 #count this row!
#         tabletran.insert(newrow) #insert row into TDE table
#         newrow.close()

# tdefile.close()

# timetaken = time.time() - start_time #just for timing and fun
# print str(rowsinserted) + ' rows inserted in ' + str(timetaken) + ' seconds'
# print '    (' + str(rowsinserted/timetaken) + ' rows per second)'