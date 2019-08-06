import pyodbc


def read(conn):
    print("read")
    cursor =  conn.cursor()
    cursor.execute("select * from emaloyeedetails")
    for row in cursor:
        print(f'row = {row}')
    print() 

def create(conn):
    print("read")
    cursor =  conn.cursor()
    cursor.execute('insert into emaloyeedetails(EmpName,EmailId) values(?,?);', ('Python','PythonEmailId')
    )
    conn.commit()
    read(conn)


def update(conn):
    print("read")
    cursor =  conn.cursor()
    cursor.execute('update  emaloyeedetails set EmpName = ? where EmailId = ?;', ('UpdatePython','PythonEmailId')
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("read")
    cursor =  conn.cursor()
    cursor.execute('delete emaloyeedetails  where empid = ?;', (22)
    )
    conn.commit()
    read(conn)


# conn = pyodbc.connect(
#     "Driver= {SQL Server Native Client 11.0};"
#     "Server= TF/SQLEXPRESS;"
#     "Database=TFAppliationDB;"
# )
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TF\SQLEXPRESS;'
                      'Database=TFAppliationDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', 
#                       host='TF/SQLEXPRESS', database='TFAppliationDB', trusted_connection='yes')

read(conn)
create(conn)
update(conn)
delete(conn)

