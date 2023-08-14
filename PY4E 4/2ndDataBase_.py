import sqlite3
# import sqlite3 library

conn = sqlite3.connect('emaildb.sqlite2')
# then we creat a connection

cur = conn.cursor()
# So in making that connection to the databases, we sort of end up with an open thats two steps. That theres the connnection to the database which checks access to the file and the cursor is kind of like our handle. Its NOT as simple as just open and reading it, but here you open and then you send SQL commands the cursor and then you get your response thropugh that same cursor.
# the file email.sqlite doesnt exist before all this, so we make it exist by making the variable we did
cur.execute('DROP TABLE IF EXISTS Counts')
#no table exists so this is useless...for now

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')
#this test is only has triple quotes to show its longer

fname = input("Enter file name: ")
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count)
                VALUES (?, 1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
