import pandas as pd

# 1- Cargo el dataset a lo machito ponce.
df = pd.read_csv(r"C:\Users\Equipo\OneDrive\Desktop\cris\data science\Proyecto personal analisis de datos\Netflix\netflix1.csv")

# 1.2- Visualización inicial de los datos sucios Nene.
#como dice el print pedimos las primeros 5 filas ¿Por que?  Para verificar que la carga de datos fue correcta Si el archivo se cargó mal, 
# df.head() puede mostrar datos incompletos, con caracteres extraños, o mal alineados 
# (lo que indicaría problemas con el delimitador o el encoding).

print("Primeras 5 filas:") 

print(df.head())

# 1.3 Resumen de la información ¿Que hace esto? Bueno ,esto funca para  obtener un resumen técnico del DataFrame.
#La función df.info() es como una “ficha técnica” del dataset y se usa casi siempre al inicio del análisis.
#te va a tirar informacion como el rango del indice , columnas , filas  y demas hierbas.

print("\nResumen del DataFrame:")
print(df.info())

# Esta funcion es una cosa maravillosa Identificar valores nulos en cada columna ¿Por que? No  hay por que solo lo hace , si vos se lo pedis. 
# Detecta rápidamente cuántos valores faltantes hay en cada columna.
print("Valores nulos por columna:")
print(df.isnull().sum())

# La columna 'listed_in' es la única con valores nulos, y es una cantidad muy pequeña.

df['listed_in'].fillna('Desconocido', inplace=True) # Entonces esta linea Selecciona solo la columna listed_in del DataFrame. Busca todas las celdas que tengan NaN (vacías) y las reemplaza por el texto "Desconocido".

#Esto es útil cuando un valor faltante puede reemplazarse por algo genérico, en lugar de eliminar la fila.

print("\nVerificación de valores nulos después de la limpieza:") # Verificación de que no hay valores nulos
print(df.isnull().sum())

# Ahora deberiamos ver que columnas, no aportan informacion relevante para nuestro analisis y tirarla a la bosta.
#vamos a usar Drop (todos sabemos que hace Drop no lo voy a explicar) ,
#  mirando las columnas gracias a .info  y por que quiero ,determino que las siguientes no van a formar parte del grupo selecto.
# 'director' no aporta valor para un análisis cuantitativo. (Cuantitativo viene de cuantificar → trabajar con datos que se pueden medir o contar numéricamente.)
# 'show_id' es un identificador único que no se usará
# 'date_added' tiene muchos valores nulos y no es clave para este análisis
df.drop(columns=['director', 'show_id', 'date_added'], inplace=True)

print("\nColumnas restantes después de la eliminación:")
print(df.columns)



# Bueno aca se pone medio confusa la cosa . Vamos a convertir  el tipo de dato de 'release_year' por eso desgloso el codigo parte por parte como Jack.

print("\nTipo de dato original de 'release_year':", df['release_year'].dtype) #df['release_year'].dtype: Mira qué tipo de datos tiene la columna release_year. Por ejemplo, puede ser object (texto) o float (decimal).
df['release_year'] = df['release_year'].astype(int) #astype(int): Cambia los valores de la columna a enteros. Por ejemplo, "2015" (texto) → 2015 (número).
#Se hace esto para que pandas pueda trabajar con estos valores como números, por ejemplo para comparaciones o gráficos.
print("Tipo de dato de 'release_year' después de la conversión:", df['release_year'].dtype) #esto no tengo que explicar que hacer, no? 


# Creación de la nueva columna 'main_genre' (Lo hacemos para simplificar y organizar los datos)
#Lo que pasa es lo siguiente, las peliculas y series pueden tener varios generos , ej: "Comedy, Drama, Romance".
#Si quieres analizar tendencias por género, contar cuántas comedias hay, o hacer gráficos, es más fácil trabajar con un solo género principal por fila.
#Tomamos solo el primer género de la lista. Quitamos espacios sobrantes y Creamos una columna nueva llamada main_genre que es mucho más fácil de analizar.
df['main_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0].strip())

print("\nDataFrame con la nueva columna 'main_genre':")
print(df[['listed_in', 'main_genre']].head())

print("\nDataFrame final después de todas las transformaciones:")
print(df.head())
df.info()

#Esta parte es un extra para agregar un poco mas a nuestro analisis
#vamos usar la columna main_genre para contar la cantidad de series y películas por cada género principal.

conteo_generos = df['main_genre'].value_counts()  # df['main_genre'] Selecciona la columna main_genre del   DataFrame y despues value_counts()  hace la magia ,  método clave.
#Recorre la columna y cuenta cuántas veces aparece cada valor único. 
#El resultado es una nueva Series de Pandas, donde el índice son los géneros y los valores son los conteos.

# Muestra el resultado
print("Conteo de series y películas por género principal:")
print(conteo_generos)
