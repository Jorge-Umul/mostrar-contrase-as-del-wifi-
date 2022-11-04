import os 
cmd="netsh wlan show profile"
resultados=os.popen(cmd)
print(resultados.read())
archivoExcel=open('resultadosdelwifi.csv', 'a')
usuario=input("ingresa el nombre de la red: ")
cmd2="netsh wlan show profile"+ usuario + "key-clear"
resultados_del_wifi=os.popen(cmd2)
archivoExcel.write(resultados_del_wifi.read())