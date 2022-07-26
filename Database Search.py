import sqlite3

database = sqlite3.connect(college.sqlite3)
cur = database.cursor()
target_search = input("Enter your search: ")
command = (""" SELECT StudentName,StudentID
                FROM student
                WHERE StudentID = ?; """)
Cur.execute(command,[target_search])
for row in cur:
    print(row[0],'C' + str(row[1])+')')