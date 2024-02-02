import subprocess

comando = '"C:\\Users\hjfno\\Documents\\GitHub\\hdb\\hdb.exe" insert miempresa clientes cliente4 "Este es el cliente 4"'

resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

if resultado.returncode == 0:
    print("ok")
else:
    print("ko")
