import pandas as pd

def AddComi(cad):
    cad2=''
    for i in range(0,len(cad)):
        cad2+=cad[i]
        if(cad[i]=="\'"):
            cad2+="\'"
    return cad2

#Insertamos valores de cast.csv
archivo=pd.read_csv('cast.csv')
archivo=pd.DataFrame(archivo)

print('INSERT INTO casti(id,name,id_movie)\n\tVALUES')
for i in range(0,len(archivo)):
    
    id=archivo.iloc[i]['id']
    name=archivo.iloc[i]['name']
    name=AddComi(name)
    id_movie=archivo.iloc[i]['id_movie']
    if(i!=len(archivo)-1):
        print('\t\t({0},\'{1}\',{2}),'.format(id,name,id_movie))
    else:
        print('\t\t({0},\'{1}\',{2})\n;'.format(id,name,id_movie))

#Insertamos valores de crew.csv
archivo=pd.read_csv('crew.csv')
archivo=pd.DataFrame(archivo)

print('INSERT INTO crew(id,name,job,id_movie)\n\tVALUES')
for i in range(0,len(archivo)):
    
    id=archivo.iloc[i]['id']
    name=archivo.iloc[i]['name']
    name=AddComi(name)
    job=archivo.iloc[i]['job']
    job=AddComi(job)
    id_movie=archivo.iloc[i]['id_movie']
    if(i!=len(archivo)-1):
        print('\t\t({0},\'{1}\',\'{2}\',{3}),'.format(id,name,job,id_movie))
    else:
        print('\t\t({0},\'{1}\',\'{2}\',{3})\n;'.format(id,name,job,id_movie))

#Insertamos valores de genero.csv
archivo=pd.read_csv('genero.csv')
archivo=pd.DataFrame(archivo)

print('INSERT INTO genero(id,name)\n\tVALUES')
for i in range(0,len(archivo)):
    
    id=archivo.iloc[i]['id']
    name=archivo.iloc[i]['name']
    name=AddComi(name)

    if(i!=len(archivo)-1):
        print('\t\t({0},\'{1}\'),'.format(id,name))
    else:
        print('\t\t({0},\'{1}\')\n;'.format(id,name))


#Insertamos valores de metadata.csv
archivo=pd.read_csv('metadata.csv')
archivo=pd.DataFrame(archivo)

print('INSERT INTO metadata(id,title,original_title,vote_average,vote_counts)\n\tVALUES')
for i in range(0,len(archivo)):
    
    id=archivo.iloc[i]['id']
    title=archivo.iloc[i]['title']
    title=AddComi(title)
    otitle=archivo.iloc[i]['original_title']
    otitle=AddComi(otitle)
    vote_avg=archivo.iloc[i]['vote_average']
    vote_cnt=archivo.iloc[i]['vote_counts']
    if(i!=len(archivo)-1):
        print('\t\t({0},\'{1}\',\'{2}\',{3},{4}),'.format(id,title,otitle,vote_avg,vote_cnt))
    else:
        print('\t\t({0},\'{1}\',\'{2}\',{3},{4})\n;'.format(id,title,otitle,vote_avg,vote_cnt))

#Insertamos valores de asociacion_genero_movies.csv
archivo=pd.read_csv('asociacion_genero_movies.csv')
archivo=pd.DataFrame(archivo)

print('INSERT INTO asociacion_genero_movies(id_gen,id_movie)\n\tVALUES')
for i in range(0,len(archivo)):
    
    id_gen=archivo.iloc[i]['id_gen']
    id_movie=archivo.iloc[i]['id_movie']

    if(i!=len(archivo)-1):
        print('\t\t({0},{1}),'.format(id_gen,id_movie))
    else:
        print('\t\t({0},{1})\n;'.format(id_gen,id_movie))