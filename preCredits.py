import pandas as pd
archivo=pd.read_csv('credits.csv')
archivo=pd.DataFrame(archivo)
cast_id=[]
cast_name=[]
cast_id_movie=[]
crew_id=[]
crew_name=[]
crew_job=[]
crew_id_movie=[]

for i in range(0,len(archivo)):
    actores=archivo.iloc[i]['cast']
    actores=eval(actores)
    produccion=archivo.iloc[i]['crew']
    produccion=eval(produccion)
    id_movie=archivo.iloc[i]['id']

    for j in range(0,len(actores)):
        actor=actores[j]
        cast_id_movie.append(id_movie)
        cast_id.append(actor['id'])
        cast_name.append(actor['name'])
    
    for k in range(0,len(produccion)):
        trab=produccion[k]
        crew_id_movie.append(id_movie)
        crew_id.append(trab['id'])
        crew_name.append(trab['name'])
        crew_job.append(trab['job'])
    if(i%5000==0):
        proc=i/len(archivo)
        print('> ',str(proc))
                                                                                                                                                                   
cast=pd.DataFrame()
cast.insert(0,'id',cast_id,True)
cast.insert(1,'name',cast_name,True)
cast.insert(2,'id_movie',cast_id_movie,True)
cast.to_csv('cast2.csv',index=False)

crew=pd.DataFrame()
crew.insert(0,'id',crew_id,True)
crew.insert(1,'name',crew_name,True)
crew.insert(2,'job',crew_job,True)
crew.insert(3,'id_movie',crew_id_movie,True)
crew.to_csv('crew2.csv',index=False)
