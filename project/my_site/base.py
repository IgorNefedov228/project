import sqlite3
 
con = sqlite3.connect("metanit.db")
cursor = con.cursor()
 

cursor.execute("""CREATE TABLE weightgain_brek
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                dish TEXT, 
                calories INTEGER,
                proteine INTEGER)
            """)