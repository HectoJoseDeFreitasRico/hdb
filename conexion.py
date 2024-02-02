import subprocess

operacion = "insert"
basededatos = "miempresa"
coleccion = "clientes"
documento = "cliente5"
contenido = "este es otro contenido de prueba"

comando = '"C:\\Users\hjfno\\Documents\\GitHub\\hdb\\hdb.exe" '+operacion+' '+basededatos+' '+coleccion+' '+documento+' "'+contenido+'"'
resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

if resultado.returncode == 0:
    print("ok")
else:
    print("ko")
