import mysql.connector

mymbd = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "1234",
    database="LaPlateforme",
)

cursor=mymbd.cursor()

cursor.execute("SELECT * FROM etudiant")

result = cursor.fetchall()


print(result)


cursor.close()
mymbd.close()
