### Autor Cesar Chirinos
### Fecha 19 Agosto 2016
### publicado en https://stickybitshell.wordpress.com/2016/08/19/calculadora-de-parley-parte-3/

logros=[]
monto = int(input("escriba monto a jugar: \n"))

while True:  ### Bloque 1 ###
    print ''
    log = raw_input("Escriba el pago del logro: \n")
    if  (len (log) > 1):
        logro = int(log)
        logros.append(logro)
        
    else:
        break

    
num=[]
cantidad = len(logros)

print "Cantidad de Logros", cantidad
i = 0

for i in range(0,cantidad): ### Bloque 2 ###
    if logros[i]>= 0:
      LOG=(1+(logros[i]/100.0000))
      num.append(LOG)
    else:
      logros[i]= logros[i]*(-1)
      LOG=(1+(100.0000/logros[i]))
      num.append(LOG)
    i+=1
    
cantidad11 = len(num)

print "Lista de logros ",num
i =  0
multiplo_logro = 1
for i in range(0,(cantidad11)): ### Bloque 3 ###
    multiplo_logro = multiplo_logro*(num[i])
    print multiplo_logro
premio = monto * multiplo_logro
print premio