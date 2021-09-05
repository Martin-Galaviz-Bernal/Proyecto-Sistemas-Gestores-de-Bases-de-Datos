import pandas as pd
archivo=pd.read_csv('movies_metadata2.csv')
archivo=pd.DataFrame(archivo)

metadata=pd.DataFrame()
meta_title=[]
meta_orig_title=[]
meta_id=[]
meta_vote_counts=[]
meta_vote_avg=[]

generos=pd.DataFrame()
gen_id=[]
gen_nombre=[]

pelicula_genero=pd.DataFrame()
id_gen=[]
id_pel=[]

for i in range(0,len(archivo)):
    gen=archivo.iloc[i]['genres']
    gen=eval(gen)
    meta_title.append(archivo.iloc[i]['title'])
    meta_orig_title.append(archivo.iloc[i]['original_title'])
    meta_id.append(archivo.iloc[i]['id'])
    meta_vote_counts.append(archivo.iloc[i]['vote_count'])
    meta_vote_avg.append(archivo.iloc[i]['vote_average'])
    

    for j in range(0,len(gen)):
        gene=gen[j]
        gen_id.append(gene['id'])
        gen_nombre.append(gene['name'])
        id_gen.append(gene['id'])
        id_pel.append(archivo.iloc[i]['id'])

    
    if(i%5000==0):
        proc=i/len(archivo)
        print('> {0:1.3f}'.format(proc))
                                                                                                                                                                   

metadata.insert(0,'id',meta_id,True)
metadata.insert(1,'title',meta_title,True)
metadata.insert(2,'original_title',meta_orig_title,True)
metadata.insert(3,'vote_average',meta_vote_avg,True)
metadata.insert(4,'vote_counts',meta_vote_counts,True)
metadata.drop_duplicates(subset=['id'],keep='first',inplace=True)
metadata.to_csv('metadata.csv',index=False)


generos.insert(0,'id',gen_id,True)
generos.insert(1,'name',gen_nombre,True)
generos.drop_duplicates(subset=['id'],keep='first',inplace=True)
generos.to_csv('genero.csv',index=False)


pelicula_genero.insert(0,'id_movie',id_pel,True)
pelicula_genero.insert(1,'id_gen',id_gen,True)
##pelicula_genero.drop_duplicates(subset=['id_movie'],keep='first',inplace=True)
pelicula_genero.to_csv('asociacion_genero_movies.csv',index=False)