import os
import subprocess
import time
import pymysql

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

subprocess.run("sudo apt-get update && sudo apt-get install -y mysql-server", shell=True, check=True)

subprocess.run("sudo sed -i 's/^bind-address.*/bind-address = 192.168.56.10/' /etc/mysql/mysql.conf.d/mysqld.cnf", shell=True, check=True)

subprocess.run("sudo systemctl restart mysql", shell=True, check=True)

time.sleep(5)

conn = pymysql.connect(host='localhost', user='root', unix_socket='/var/run/mysqld/mysqld.sock')
cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"CREATE USER IF NOT EXISTS '{DB_USER}'@'192.168.56.11' IDENTIFIED BY '{DB_PASS}'")
cursor.execute(f"GRANT ALL PRIVILEGES ON {DB_NAME}.* TO '{DB_USER}'@'192.168.56.11'")
cursor.execute("FLUSH PRIVILEGES")

conn.commit()
conn.close()
