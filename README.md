# Proyecto-Sistemas-Gestores-de-Bases-de-Datos
Proyecto final de la materia de Sistemas Gestores de Base de Datos
En este repositorio se encuentran los script necesarios para realizar una serie de consultas de los datos
de la página https://www.kaggle.com/rounakbanik/the-movies-dataset, en total son 8 consultas que se hacen
en base a los CSV de cedits.csv y movies-metadata.csv. Cabe destacar que ambos csv tienen datos no atómicos
que deben ser preprocesados para generar nuevos archivos csv que nos serán útiles en las consultas.

El sistema gestos de base de datos que se utilizará será PostgreSQL.

El archivo movies_metadata.csv tiene algunos saltos de línea que no corresponden con el formato CSV y es por
esto que se tienen que eliminar antes de hacer cualquier preprocesado. El preprocesado se hace con los script
preCredits.py y preMetadata.csv, el resultado de esto son 5 archivos CSV que contienen la información que 
se colocará en las tablas de la base de datos.

Los archivos consultaLen.py y consultaLenCastCrew.py se encargan de calcular el tamaño máximo de las cadenas
de caracteres contenidas en los CSV generados. Esto se hace para poder generar adecuadamente el esquema de las
tablas de la base de datos.

El archivo create_tables.sql se encarga de crear las tablas en nuestra BD (base de datos).

El archivo drop_tablas.sql se encarga de eliminar las tablas (incluyendo el esquema).

Como se probaron dos métodos de inserción de datos, uno con el archivo copyData.sql y otro con un 
archivo generado con el script generaInsertCast.py. Ambos métodos sirven para insertar los datos de los 
CSV en su respectiva tabla.

Con el script deleteTablas.sql podemos borrar el contenido de cada tabla.

Los script insercion.sql, delete.sql y update.sql sirven para insertar, borra y actualizar un registro de cada tabla de la BD.

Los script encargados de las consultas son los que tienen dicho nombre "consulta" con su respectivo número.

Los script creacion_indices.sql y borra_indices.sql se encargan de crear y eliminar los índices de la BD.
Es importante que la creación de los índices se realice antes de insertar los datos en las tablas.
