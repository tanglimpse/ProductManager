import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

"""
c.execute("DROP TABLE PRODUCT")

c.execute('''
        CREATE TABLE PRODUCT
       (
       GNAME           NVARCHAR(100),
       PNAME           NVARCHAR(100),
       SIZE        NVARCHAR(100),
       NUMBER        NVARCHAR(100),
       primary key (GNAME,PNAME)
       )
       ''')

c.execute("INSERT INTO PRODUCT (GNAME,PNAME,SIZE,NUMBER) \
      VALUES ('好112121', '好', '好','hjk')")

      

 """



conn.commit()

'''

cursor=c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


guest="'好'"
guest1="'好'"
guest2="'好'"
guest3=123344

cursor = c.execute("SELECT * FROM GUEST WHERE NAME=" + guest)
row = [r for r in cursor]
if (len(row) > 0):
    print(row[0][0])

conn.commit()


cursor=c.execute("SELECT * FROM GUEST WHERE NAME="+guest)
row=[r for r in cursor]
if(len(row)>0):
    c.execute("DELETE FROM GUEST WHERE NAME ="+guest)

c.execute("INSERT INTO GUEST (NAME,COMPANY,ADDRESS,PHONE) \
      VALUES ({myname},{mycompany}, {myaddress}, {myphone} )" \
          .format(myname=guest,mycompany=company,myaddress=address,myphone=phone))

c.execute("DELETE FROM GUEST WHERE NAME ='好112121' ")


cursor = c.execute("SELECT * FROM   GUEST")
for row in cursor:
   print( row[0])


c.execute("INSERT INTO GUEST (NAME,COMPANY,ADDRESS,PHONE) \
      VALUES ('好112121', '好', '好', 13122752708 )")
c.execute("UPDATE GUEST set COMPANY = 25011 where NAME='好112121'")



'''


conn.close()