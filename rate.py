import sqlite3

conn = sqlite3.connect('rate.db', check_same_thread=False)
    


def createT():
    print("Opened database successfully")
    
    #conn.execute(CREATE TABLE rate(ID INT PRIMARY KEY    NOT NULL))     
    
    conn.execute('''CREATE TABLE rate(ID INT PRIMARY KEY, NAME TEXT ,RATE  FLOAT ,MESSAGE TEXT, ANONIM TEXT)''')
     
    print("Table created successfully")
    conn.close()
    
def printT():
    cursor = conn.execute("SELECT id, name, rate, message, anonim from rate")
    
    df_mentah = {'id':[],'name':[],'rate':[],'message':[], 'anonim':[]}
    
    for row in cursor:
        df_mentah['id'].append(row[0])
        df_mentah['name'].append(row[1])
        df_mentah['rate'].append(row[2])
        df_mentah['message'].append(row[3])
        df_mentah['anonim'].append(row[4])
        print('id :',row[0],'\nnama :', row[1], '\nrate :', row[2], '\nmessage :',row[3], '\nanonim :', row[4], '\n')
        
    return df_mentah
    
def resetid():
    idi = conn.execute("SELECT id from rate")
    ids = []
    
    for i in idi:
        ids.append(i)
    
    for j in range(len(ids)):
        conn.execute(f"UPDATE rate set ID = {j} where ID = {ids[j][0]};")
        
  
def inputT(name, rate, message, anonim):
    idi = conn.execute("SELECT id from rate")
    ids = []
    
    for i in idi:
        ids.append(i)
    
    rate = str(rate)
    
    isi = str(f"INSERT INTO rate (ID,NAME,RATE,MESSAGE,ANONIM)  VALUES ({len(ids)}, '{name}', {rate}, '{message}', '{anonim}' )")
    
    conn.execute(isi)
    
    conn.commit()
    
    print('input succes!')
    
def deleteT(id):
    conn.execute(f"DELETE from rate where ID = {id};")
    resetid()
    conn.commit()


def resetT():
    idi = conn.execute("SELECT id from rate")
    ids = []
    
    for i in idi:
        ids.append(i)
    
    for j in ids:
        conn.execute(f"DELETE from rate where ID = {j[0]};")
        conn.commit()
        


#createT()
#resetT()
#\inputT(name='Default', rate=5, message='Default', anonim='on')
# inputT(name='Syabilla', rate=10, message='oke bagus')
# inputT(name='Syablla', rate=10, message='oke bagus')
# inputT(name='Default', rate=10, message='Default')
# inputT(name='Syabilla', rate=10, message='oke bagus')
# inputT(name='Syablla', rate=10, message='oke bagus')
# inputT(name='Default', rate=10, message='Default')
# inputT(name='Syabilla', rate=10, message='oke bagus')
# inputT(name='Syablla', rate=10, message='oke bagus')



# deleteT(0)
#deleteT(1)
# deleteT(2)
# deleteT(3)
#deleteT(4)
# deleteT(5)
#deleteT(6)
#printT()