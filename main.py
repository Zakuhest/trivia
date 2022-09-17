#librerias
import random
import time

#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

mensaje_carga = "Cargando pregunta."
mensaje_ruleta = "Calculando puntaje final."
bonus_ruleta = 0
c = 1 #contador

estado_trivia = True
intento = 0

save_name = []


#Número de intentos
print(GREEN+"\nIntentos:",str(intento)+".",end="\n"+RESET)
  
  #Bienvenida a la trivia
print(BLUE+"""
Bienvenido a mi trivia sobre la Champions League, donde pondré a prueba tus conocimientos deportivos. 
 
Antes de comenzar, podrías escribir tu nombre?: \n
"""+RESET)
  
time.sleep(2)
name = input(MAGENTA+"Escribe tu nombre: "+RESET) #Ingresar nombre del usuario
save_name.append(name)

while estado_trivia:
  #Número de intentos actualizado
  if intento > 0:
    print(GREEN+"\nIntentos:",str(intento)+".",end="\n"+RESET)
  
  puntaje = random.randint(0,10) #puntaje aleatorio
  
  #Instrucciones de la trivia
  print(BLUE+"\nGenial,",str(save_name[0]) + "!. Responde las siguientes preguntas, escribiendo la alternativa que creas correcta y presionando 'Enter' podrás enviar tu respuesta:"+RESET)
  print(GREEN+"\nComenzaras con:",puntaje,"puntos.",end="\n"+RESET)
  
  for time_carga in range (6,0,-1): #desafio a
    if c in (1,3):
      time.sleep(1)
      print(WHITE+"\n"+mensaje_carga+RESET)
      c = 1
      
    time.sleep(1)
    print(WHITE+mensaje_carga+"."*c+RESET)
    c += 1
    
  #Primera pregunta de la trivia
  print(
    YELLOW+"""
  1.- ¿Cuántos clubes franceses han ganado la Champions?
    a) Uno
    b) Tres
    c) Cinco
    d) Ninguno
    """+RESET #correcto a
  )
  respuesta_1 = input(MAGENTA+str(save_name[0])+" escribe aquí tu 1° respuesta: "+RESET)
  
  while respuesta_1 not in ("a","b","c","d","p"):
    respuesta_1 = input(RED+str(save_name[0])+", esa no es una alternativa válida."+RESET+MAGENTA+" Por favor, escribe nuevamente tu 1° respuesta: "+RESET)
    #respuestas alternativas
  if respuesta_1 == "b":
    print(RED+"\nTres clubes franceses? No es correcto!"+RESET)
    puntaje-=random.randint(0,5) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_1 == "c":
    print(RED+"\nCinco clubes franceses? No es correcto!"+RESET)
    puntaje-=random.randint(0,5) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_1 == "d":
    print(RED+"\nNingún club francés? No es correcto!"+RESET)
    puntaje-=random.randint(0,5) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_1 == "p":
    print(GREEN+"\nEncontraste un mensaje oculto,",str(save_name[0])+"!"+RESET)
    puntaje+=random.randint(15,30) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  else:
    print(GREEN+"\nMuy bien,",str(save_name[0])+"!","Es correcto que solo un club francés ha ganado la Champions!"+RESET)
    puntaje+=random.randint(5,10) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  
  for time_carga in range (6,0,-1):
    if c in (1,3):
      time.sleep(1)
      print(WHITE+"\n"+mensaje_carga+RESET)
      c = 1
      
    time.sleep(1)
    print(WHITE+mensaje_carga+"."*c+RESET)
    c += 1
  
  #Segunda pregunta de la trivia
  print(
    YELLOW+"""
  2.- ¿Quién anotó el único gol en la final del 98 entre el Real Madrid y Juventus?
    a) Suker
    b) Mijatovic
    c) Hierro
    d) Ninguno
    """+RESET#correcto b
  )
  respuesta_2 = input(MAGENTA+str(save_name[0]) + " escribe aquí tu 2° respuesta: "+RESET)
  
  while respuesta_2 not in ("a","b","c","d","x"):
    respuesta_2 = input(RED+str(save_name[0]) + ", esa no es una alternativa válida."+RESET+MAGENTA+" Por favor, escribe nuevamente tu 2° respuesta: "+RESET)
    #respuestas alternativas
  if respuesta_2 == "a":
    print(RED+"\nSuker anotó el único gol? No es correcto!"+RESET)
    puntaje-=random.randint(5,10) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_2 == "c":
    print(RED+"\nHierro anotó el único gol? No es correcto!"+RESET)
    puntaje-=random.randint(5,10) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_2 == "d":
    print(RED+"\nNingún jugador anotó el único gol? No es correcto!"+RESET)
    puntaje-=random.randint(5,10) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_2 == "x":
    print(GREEN+"\nEncontraste un mensaje oculto,",str(save_name[0])+"!"+RESET)
    puntaje+=random.randint(15,30) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  else:
    print(GREEN+"\nMuy bien,",str(save_name[0])+"!","Es correcto que Mijatovic anotó el único gol en la final del 98 entre el Real Madrid y Juventus!"+RESET)
    puntaje+=random.randint(5,10) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  
  for time_carga in range (6,0,-1):
    if c in (1,3):
      time.sleep(1)
      print(WHITE+"\n"+mensaje_carga+RESET)
      c = 1
      
    time.sleep(1)
    print(WHITE+mensaje_carga+"."*c+RESET)
    c += 1
  
  #Tercera pregunta de la trivia
  print(
    YELLOW+"""
  3.- ¿Cuántos peruanos han disputado la final de la Copa de Europa/Champions League?
    a) 1
    b) 2
    c) 3
    d) 6
    """+RESET#correcto b
  )
  respuesta_3 = input(MAGENTA+str(save_name[0]) + " escribe aquí tu 3° respuesta: "+RESET)
  
  while respuesta_3 not in ("a","b","c","d","r"):
    respuesta_3 = input(RED+str(save_name[0]) + ", esa no es una alternativa válida."+RESET+MAGENTA+" Por favor, escribe nuevamente tu 3° respuesta: "+RESET)
    #respuestas alternativas
  if respuesta_3 == "a":
    print(RED+"\nSolo fue un peruano? No es correcto!"+RESET)
    puntaje-=random.randint(10,15) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_3 == "c":
    print(RED+"\nTres peruanos? No es correcto!"+RESET)
    puntaje-=random.randint(10,15) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_3 == "d":
    print(RED+"\nSeis peruanos? No es correcto!"+RESET)
    puntaje-=random.randint(10,15) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_3 == "r":
    print(GREEN+"\nEncontraste un mensaje oculto,",str(save_name[0])+"!"+RESET)
    puntaje+=random.randint(15,30) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  else:
    print(GREEN+"\nMuy bien,",str(save_name[0])+"!","Es correcto que dos peruanos disputaron la final de la Copa Europa/Champions League!"+RESET)
    puntaje+=random.randint(5,10) #desafio a
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  
  for time_carga in range (6,0,-1):
    if c in (1,3):
      time.sleep(1)
      print(WHITE+"\n"+mensaje_carga+RESET)
      c = 1
      
    time.sleep(1)
    print(WHITE+mensaje_carga+"."*c+RESET)
    c += 1
  
  #Cuarta pregunta de la trivia
  print(
    YELLOW+"""
  4.- ¿Qué jugador entró a una final y anotó cuando apenas tenía 16 segundos en la cancha?
    a) Müller
    b) Kluivert
    c) Lars Ricken
    d) Rivaldo
    """+RESET#correcto c
  )
  respuesta_4 = input(MAGENTA+str(save_name[0]) + " escribe aquí tu 4° respuesta: "+RESET)
  
  while respuesta_4 not in ("a","b","c","d","m"):
    respuesta_4 = input(RED+str(save_name[0]) + ", esa no es una alternativa válida."+RESET+MAGENTA+" Por favor, escribe nuevamente tu 4° respuesta: "+RESET)
    #respuestas alternativas
  if respuesta_4 == "a":
    print(RED+"\nMüller anotó en la final? No es correcto!"+RESET)
    puntaje//=2
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_4 == "b":
    print(RED+"\nKluivert anotó en la final? No es correcto!"+RESET)
    puntaje+=5
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_4 == "d":
    print(RED+"\nRivaldo anotó en la final? No es correcto!"+RESET)
    puntaje-=5
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  elif respuesta_4 == "m":
    print(GREEN+"\nEncontraste un mensaje oculto,",str(save_name[0])+"!"+RESET)
    puntaje+=random.randint(15,30)
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  else:
    print(GREEN+"\nMuy bien,",str(save_name[0])+"!","Es correcto que Lars Ricken entró a una final de Champions League y anotó cuando apenas tenía 16 segundos en la cancha!"+RESET)
    puntaje*=2
    print(GREEN+"Puntaje actual:",puntaje,end="\n"+RESET)
  
  for time_carga in range (6,0,-1): #desafio b
    if c in (1,3):
      time.sleep(1)
      print(WHITE+"\n"+mensaje_ruleta+RESET)
      c = 1
      
    time.sleep(1)
    print(WHITE+mensaje_ruleta+"."*c+RESET)
    c += 1
  bonus_ruleta = random.randint(0,5)
  puntaje+= bonus_ruleta
  
  #Fin de la trivia
  print(CYAN+"\nGracias,",str(save_name[0])+", por jugar mi trivia sobre la Champions League!!. Alcanzaste", puntaje,"puntos, con un bonus por ruleta de",bonus_ruleta, end=" puntos.\n"+RESET)
  
  time.sleep(4)
  pregunta_estado = input(BLUE+str(save_name[0])+", deseas nuevamente realizar el test? (y/n): "+RESET).lower()

  if pregunta_estado != "y":
    time.sleep(2)
    print(CYAN+"\nEspero que te hayas divertido,",str(save_name[0])+"!. Ojalá puedas volver pronto para jugar. Hasta luego."+RESET)
    estado_trivia = False

  intento+=1
