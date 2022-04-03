import sqlite3

connp = sqlite3.connect('predict.db', check_same_thread=False)
    


def createTP():
    print("Opened database successfully")
    
    #conn.execute(CREATE TABLE rate(ID INT PRIMARY KEY    NOT NULL))     
    
    connp.execute('''CREATE TABLE pred(ID INT PRIMARY KEY, TEKS TEXT ,JUDUL TEXT,URL TEXT, UJUDUL TEXT, UKONTEN TEXT, PSTRUE FLOAT, PSFALSE FLOAT, PDTRUE INT, PDFALSE INT, ERR BOOL)''')
     
    print("Table created successfully")
    connp.close()
    
def printTP():
    cursorp = connp.execute("SELECT ID,TEKS,JUDUL,URL,UJUDUL,UKONTEN,PSTRUE,PSFALSE,PDTRUE,PDFALSE,ERR from pred")
    
    df_mentah = {'id':[],'teks':[],'judul':[],'url':[],'ujudul':[],'ukonten':[],'pstrue':[],'psfalse':[],'pdtrue':[],'pdfalse':[],'err':[]}
    
    for row in cursorp:
        df_mentah['id'].append(row[0])
        df_mentah['teks'].append(row[1])
        df_mentah['judul'].append(row[2])
        df_mentah['url'].append(row[3])
        df_mentah['ujudul'].append(row[4])
        df_mentah['ukonten'].append(row[5])
        df_mentah['pstrue'].append(row[6])
        df_mentah['psfalse'].append(row[7])
        df_mentah['pdtrue'].append(row[8])
        df_mentah['pdfalse'].append(row[9])
        df_mentah['err'].append(row[10])
    
    print(df_mentah)    
    return df_mentah
    
def resetidP():
    idi = connp.execute("SELECT id from pred")
    ids = []
    
    for i in idi:
        ids.append(i)
    
    for j in range(len(ids)):
        connp.execute(f"UPDATE pred set ID = {j} where ID = {ids[j][0]};")
        
  
def inputTP(teks,judul,url,ujudul,ukonten,pstrue,psfalse,pdtrue,pdfalse,err):
    idi = connp.execute("SELECT id from pred")
    ids = []
    
    for i in idi:
        ids.append(i)
    
    
    connp.execute("INSERT INTO pred (ID,TEKS,JUDUL,URL,UJUDUL,UKONTEN,PSTRUE,PSFALSE,PDTRUE,PDFALSE,ERR)  VALUES (?,?,?,?,?,?,?,?,?,?,?)", (len(ids), teks, judul, url, ujudul, ukonten, pstrue, psfalse, pdtrue, pdfalse, err))
    
    connp.commit()
    
    print('input succes!')
    
def deleteTP(id):
    connp.execute(f"DELETE from pred where ID = {id};")
    resetidP()
    connp.commit()


def resetTP():
    idi = connp.execute("SELECT id from pred")
    ids = []
    
    for i in idi:
        ids.append(i)
    
    for j in ids:
        connp.execute(f"DELETE from pred where ID = {j[0]};")
        connp.commit()
        


#createTP()
#resetTP()
# inputT(name='Default', rate=5, message='Default')
# inputT(name='Syabilla', rate=10, message='oke bagus')
# inputT(name='Syablla', rate=10, message='oke bagus')
# inputT(name='Default', rate=10, message='Default')
# inputT(name='Syabilla', rate=10, message='oke bagus')
# inputT(name='Syablla', rate=10, message='oke bagus')
# inputT(name='Default', rate=10, message='Default')
# inputT(name='Syabilla', rate=10, message='oke bagus')
# inputT(name='Syablla', rate=10, message='oke bagus')
printTP()


# deleteT(0)
#deleteT(1)
# deleteT(2)
# deleteT(3)
#deleteT(4)
# deleteT(5)
#deleteT(6)