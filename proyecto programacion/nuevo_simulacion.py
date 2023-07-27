from comunidad import Comunidad
from enfermedad import Peste_negra
from persona import Persona
import random
import json

with open('nombres_apellidos.json') as file:
    data = json.load(file)

def ecuacion(ca, b,dias_an, inf_prob):
    prob_inf = (inf_prob * 30)/100
    infec = []
    new_ca = []
    i=0
    s=0
    prob = 0
    while len(ca) != 0:
        prob = 0
        contacto = []
        if len(ca) <= 4:
            if len(ca) == 1:
                new_ca.append(ca[0])
                ca.remove(ca[0])
                pass
            elif len(ca) == 2:
                p1 = ca[0]
                p2 = ca[1]
                contacto = [p1,p2]
                ca.remove(p1)
                ca.remove(p2)
            elif len(ca) == 3:
                p1 = ca[0]
                p2 = ca[1]
                p3 = ca[2]
                contacto = [p1,p2,p3]
                ca.remove(p1)
                ca.remove(p2)
                ca.remove(p3)
            elif len(ca) == 4:
                p1 = ca[0]
                p2 = ca[1]
                p3 = ca[2]
                p4 = ca[3]
                contacto = [p1,p2,p3,p4]
                ca.remove(p1)
                ca.remove(p2)
                ca.remove(p3)
                ca.remove(p4)
            for a in contacto:
                if a[3] == True:
                    prob = prob + prob_inf
            for b in contacto:
                if b[3] == False:
                    if prob == 0:
                        new_ca.append(b)
                    else:
                        con_est = random.choice([True,False])
                        if con_est == True:
                            prob = prob + 10
                        r = random.choice(range(100))
                        if r <= prob:
                            b[3] = True
                            new_ca.append(b)
                        else:
                            new_ca.append(b)
                else:
                    new_ca.append(b)
        else:                
            p1 = random.choice(ca)
            p2 = random.choice(ca)
            p3 = random.choice(ca)
            p4 = random.choice(ca)
            if (p1 == p2 or p1 == p3 or p1 == p4
            or p2 == p3 or p2 == p4 or p3 == p4):
                pass
            else:
                contacto = [p1,p2,p3,p4]
                ca.remove(p1)
                ca.remove(p2)
                ca.remove(p3)
                ca.remove(p4)
                for a in contacto:
                    if a[3] == True:
                        prob = prob + prob_inf
                for b in contacto:
                    if b[3] == False:
                        if prob == 0:
                            new_ca.append(b)
                        else:
                            con_est = random.choice([True,False])
                            if con_est == True:
                                prob = prob + 10
                            r = random.choice(range(100))
                            if r <= prob:
                                b[3] = True
                                new_ca.append(b)
                            else:
                                new_ca.append(b)
                    else:
                        new_ca.append(b)
    for x in new_ca:
        if x[3] == True:
            i = i+1
            infec.append(x)
        else:
            s = s+1
    dias_an.append(infec)
    return(new_ca,s,i,dias_an)

def m_o_r(ca,dias_an,y,muertos,recuperados):
    can = len(dias_an)
    for x in dias_an[can-3]:
        if x[3] == True and x[4]==True and x[5]==False:
            prob = random.choice(range(100))
            if prob <= y:
                ca.remove(x)
                x[5] = True
                recuperados.append(x)
            else:
                ca.remove(x)
                x[4] = False
                muertos.append(x)
    dias_an.remove(dias_an[0])        
    return(ca,muertos,recuperados)

def vacunacion(ca, can_per, recuperados):
    per_vac = []
    contador = 0
    can_per_vac = round((40*can_per)/100)
    quarter = round((25*can_per_vac)/100)
    mid = round((50*can_per_vac)/100)
    while contador != can_per_vac:
        examinar = random.choice(ca)
        if examinar[3] == False:
            per_vac.append(examinar)
            ca.remove(examinar)
            contador = contador +1
    contador = 0
    while contador != quarter:
        ra = random.choice(per_vac)
        ra[5] = True
        recuperados.append(ra)
        ra = random.choice(per_vac)
        posibilidad = random.choice(range(100))
        if 25 >= posibilidad:
            ra[5] = True
            recuperados.append(ra)
        else:
            ca.append(ra)
        contador = contador + 1
    for a in per_vac:
        posibilidad = random.choice(range(100))
        if 50 >= posibilidad:
            a[5] = True
            recuperados.append(a)
        else:
            ca.append(a)
    return ca, recuperados


def ejecutar(can_per, dias, inf_prob, rec_prob):
    muertos=[]
    recuperados = []
    dias_an = []
    graf_s = [can_per]
    graf_i = [1]
    graf_r = [0]
    graf_m = [0]
    per = Persona() # import class persona
    ca = per.crear_persona(can_per)
    com = Comunidad() #import class comunidad
    enf = Peste_negra() # import class enfermedad
    dia_cont = 1  #dia en el que inicia la simulacion y avanza
    com.cantidad_persona = can_per
    m = 0  #cantidad de individuos muertos
    i = 1  #cantidad de individuos infectado
    r = 0  #cantidad de individuos recuperado
    b = enf.infect_probabilidad = inf_prob  #tasa de transmision
    y = rec_prob #tasa de recuperacion
    s = com.cantidad_persona-i
    informacion_general =[[dia_cont,s,i,r,m]]
    print("[dia",dia_cont,"][supseptible:",s,"][infectado: ",
        i,"][recuperados:",len(recuperados),"][muertos:",len(muertos),"]")
    while dia_cont != dias:
        if dia_cont == 4:
            ca, recuperados = vacunacion(ca,can_per,recuperados)
        ca, s, i, dias_an = ecuacion(ca,b,dias_an,inf_prob)
        if len(informacion_general) >= 4:
           ca, muertos,recuperados = m_o_r(ca,dias_an,y,muertos,recuperados)
        graf_s.append(s)
        graf_i.append(i)
        graf_r.append(len(recuperados))
        graf_m.append(len(muertos))
        dia_cont = dia_cont+1
        informacion_general.append(
            [dia_cont,s,i,len(recuperados),len(muertos)])
        print("[dia",dia_cont,"][supseptible:",s,"][infectado: ",
        i,"][recuperados:",len(recuperados),"][muertos:",len(muertos),"]")
    return graf_s,graf_i,graf_r,graf_m