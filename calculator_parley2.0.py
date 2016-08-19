
logros=[]
monto = int(input("escriba monto a jugar: \n"))

while True:
    print ''
    log = raw_input("Escriba el pago del logro: \n")
    if  (len (log) > 1):
        logro = int(log)
        logros.append(logro)
        print logro
        
    else:
        break

    
num=[]
cantidad = len(logros)

print "AQQQQ", cantidad
i = 0

for i in range(0,cantidad):
    if logros[i]>= 0:
      LOG=(1+(logros[i]/100.0000))
      num.append(LOG)
    else:
      logros[i]= logros[i]*(-1)
      LOG=(1+(100.0000/logros[i]))
      num.append(LOG)
    i+=1
    
cantidad11 = len(num)

print num
i =  0
multiplo_logro = 1
for i in range(0,(cantidad11)):
    multiplo_logro = multiplo_logro*(num[i])
    print multiplo_logro
premio = monto * multiplo_logro
print premio