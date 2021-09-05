import pandas as pd
archivo=pd.read_csv('credits.csv')
archivo=pd.DataFrame(archivo)



lc=0
lcr=0
lj=0
for i in range(0,len(archivo)):
    actores=archivo.iloc[i]['cast']
    actores=eval(actores)
    produccion=archivo.iloc[i]['crew']
    produccion=eval(produccion)
    

    for j in range(0,len(actores)):
        actor=actores[j]
        cast_name=actor['name']
        if(len(cast_name)>lc):
            lc=len(cast_name)
    
    for k in range(0,len(produccion)):
        trab=produccion[k]

        crew_name=trab['name']
        if(len(crew_name)>lcr):
            lcr=len(crew_name)

        crew_job=trab['job']
        if(len(crew_job)>lj):
            lj=len(crew_job)
    # if(i%5000==0):
    #     proc=i/len(archivo)
    #     print('> ',str(proc))
                                                                                                                                                                   
print('longitud cast name = ',str(lc))
print('longitud crew name = ',str(lcr))
print('longitud crew job = ',str(lj))