import pandas as pd
archivo=pd.read_csv('movies_metadata2.csv')
archivo=pd.DataFrame(archivo)

metadata=pd.DataFrame()

lt=0
lot=0

for i in range(0,len(archivo)):
    
    meta_title=archivo.iloc[i]['title']
    meta_orig_title=archivo.iloc[i]['original_title']
    if(len(meta_title)>lt):
        lt=len(meta_title)
    if(len(meta_orig_title)>lot):
        lot=len(meta_orig_title)

    
    # if(i%5000==0):
    #     proc=i/len(archivo)
    #     print('> {0:1.3f}'.format(proc))
                                                                                                                                                                   

print('longitud title = ',str(lt))
print('longitud original title = ',str(lot))