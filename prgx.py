import subprocess#######################^&*((((((((#*@!Q%(#^%!)@#^!&*^#)!#
import pymysql as MySQLdb#######################^&*((((((((#*@!Q%(#^%!)@#^!&*^#)!#
import time#######################^&*((((((((#*@!Q%(#^%!)@#^!&*^#)!#
class cl():
    db = MySQLdb.connect(
host='sql3.freemysqlhosting.net',
user='sql3521617',
passwd='9nliDkYDut',
port=3306,
db="sql3521617"
)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `key_id_` ORDER BY `hwid_` ASC ")
    rows = cursor.fetchall()
    for row in rows:
        hw = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        hwid = row[0]
    if hw in hwid:
        class mai():
            ans = True
            while ans:
                print(""" 2.Exit """"")
                ans = input("SELECT: \n")

                if ans == "2":
                    exit()