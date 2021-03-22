import sys
!{sys.executable} -m pip install mysql-connector-python

import mysql.connector
miConexion = mysql.connector.connect(user='root', 
                              password='cisco',
                              host='db',
                              )
miCursor = miConexion.cursor()
miCursor.execute("CREATE DATABASE IF NOT EXISTS net_inventory")
miCursor.execute("SHOW DATABASES")
databases = miCursor.fetchall()
print(databases)
sql="use net_inventory"
miCursor.execute(sql)

sql="""create table if not exists equipos ( 
         device_type  VARCHAR(50),  
         device_ip VARCHAR(40),  
         device_username VARCHAR(20),  
         device_password VARCHAR(20),  
         device_port INTEGER(6)  
   )"""
miCursor.execute(sql)   
while True:
        device_type = input("coloca el tipo de equipo :")
        device_ip   = input("coloca la direccion ip del equipo :")
        device_username = input("coloca el usuario del equipo :")
        device_password = input("coloca el password del equipo :")
        device_port = int(input("coloca el numero de puerto :"))
        equipos = (device_type,device_ip,device_username,device_password,device_port)
        sql="insert into equipos(device_type, device_ip, device_username, device_password, device_port) values (%s,%s,%s,%s,%s)"
        miCursor.execute(sql,equipos)
        print("Valor del último codigo de artículo generado:", miCursor.lastrowid)
        miConexion.commit()
        consulta = input("deseas agregar otro equipo? Y/N :")
        if consulta == "N":
                miConexion.close()
                print (" OK Bye!!!")
                break
        else:
             print ("\n agregando otro dispositivo")

