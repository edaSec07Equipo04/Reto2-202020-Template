"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def nueva_lista(estructura):
    
    lista = lt.newList(datastructure= 'ARRAY_LIST',cmpfunction= None)
        
    return lista
 
def ananir_pelicula(lista,pelicula):
 
    lista = lt.addLast(lista,pelicula)
 
    return lista

def newCatalog():
    """ Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas

    Se crean indices (Maps) por los siguientes criterios:
    

    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
               'moviesIds': None,
               'producers':None,
               'directors':None,
               'actors':None,
               'genres':None,
               'countries':None}

    catalog['movies']=lt.newList('ARRAY_LIST',compareRecordIds)
    catalog['moviesIds'] = mp.newMap(328511,
                                     maptype= 'PROBING',
                                     loadfactor=0.5,
                                     comparefunction=compareRecordIds)
    catalog['producers'] = mp.newMap(32647,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=compareProducersByName)
    catalog['directors']=mp.newMap(350,
                                  maptype= 'PROBING',
                                  loadfactor=0.5,
                                  comparefunction=compareDirectorsByName)
    catalog['actors']=mp.newMap(350,
                               maptype= 'PROBING',
                               loadfactor=0.5,
                               comparefunction=compareActorsByName)
    catalog['genres']=mp.newMap(43,
                               maptype= 'PROBING',
                               loadfactor=0.5,
                               comparefunction=compareGenresByName)
    catalog['countries']=mp.newMap(350,
                               maptype= 'PROBING',
                               loadfactor=0.5,
                               comparefunction=compareCountriesByName)                                                             
    return catalog


def newProducer(company):
    """
    Crea una nueva estructura para modelar las películas de una productora
    y su promedio de calificación
    """
    producer = {'name': '', 'movies':None,'vote_average': 0.0}
    producer['name'] = company
    producer['movies'] = lt.newList('ARRAY_LIST',compareProducersByName)
    return producer

def newGenre(genre):
    #Requerimiento 4 - Sebastian Peña 
    """
    Crea una nueva estructura para modelar las peliculas de un genero 
    y su promedio de votos
    """
    genero = {'name': '','movies': None,'vote_count': 0.0 }
    genero['name']=genre
    genero['movies']=lt.newList('ARRAY_LIST',compareGenresByName)
    return genero 

    

    
#-----------------------------------------------
# Funciones para agregar informacion al catalogo
#-----------------------------------------------

def addMovie(catalog,movie):
    """
    Esta funcion adiciona una película a la lista de películas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['movies'],movie)
    mp.put(catalog['moviesIds'],movie['id'],movie)


def addMovieProducer(catalog,company,movie):
    """
    Lo que hace la función
    """
    
    producers = catalog['producers']
    existproducer = mp.contains(producers,company)
    if existproducer:
        entry = mp.get(producers,company)
        data = me.getValue(entry)
    else:
        data = newProducer(company)
        mp.put(producers,company,data)
    lt.addLast(data['movies'],movie)
    proavg = data['vote_average']
    movieavg = movie['vote_average']
    if (proavg == 0.0):
        data['vote_average'] = float(movieavg)
    else:
        data['vote_average'] = (proavg+float(movieavg))/2

def addMovieGenre(catalog,genre,movie):
    #Requerimiento 4 - Sebastian Peña
    """
    Esta funcion agrega cada pelicula por su genero.
    Ademas incluye el promedio de votos por genero
    """
    
    genres= catalog['genres']
    existgenre = mp.contains(genres,genre)
    if existgenre:
        entry = mp.get(genres,genre)
        data = me.getValue(entry)
    else:
        data = newGenre(genre)
        mp.put(genres,genre,data)
    lt.addLast(data['movies'],movie)

    promediado= data['vote_count']
    movie_pro = movie['vote_count']
    if (promediado == 0.0):
        data['vote_count']=float(movie_pro)
    else:
        data['vote_count']= ((promediado*(lt.size(data['movies'])-1))+float(movie_pro))/(lt.size(data['movies']))
        


# ==============================
# Funciones de consulta
# ==============================

def getGoviesByProductionCompany(catalog,producer):
    company = mp.get(catalog['producers'],producer)
    
    if company:
        lst = nueva_lista('ARRAY_LIST')
        result = me.getValue(company)
        totalMovies = lt.size(result['movies'])
        vote_average = result['vote_average']
        for i in range(1,lt.size(result['movies'])+1):
            movie = lt.getElement(result['movies'],i)
            ananir_pelicula(lst,movie['title'])
        return lst['elements'],totalMovies,vote_average
    
    return None

def MoviesByGenre(catalog,genre):
    #Requerimiento 4 - Sebastian Peña
    """
    funcion que retorna las peliculas, promedio de votos y numero de peliculas
    """
    genres=mp.get(catalog['genres'],genre)

    if genres:
        lst= nueva_lista('ARRAY_LIST')
        resultado = me.getValue(genres)
        totalMovies = lt.size(resultado['movies'])
        vote_count= resultado['vote_count']
        for i in range(1,lt.size(resultado['movies'])+1):
            movie=lt.getElement(resultado['movies'],i)
            ananir_pelicula(lst,movie['title'])
        return lst['elements'],totalMovies, vote_count

    return None

def moviesSize(catalog):
    """
    Número de películas en el catálogo
    """
    return lt.size(catalog['movies'])

def producersSize(catalog):
    """
    Número de productoras en el catálogo
    """
    return mp.size(catalog['producers'])
def genresSize(catalog):
    #Requerimiento 4 - Sebastian Peña
    """
    Numero de generos en el catalogo
    """
    return mp.size(catalog['genres'])


# ==============================
# Funciones de Comparacion
# ==============================

def compareRecordIds (recordA, recordB):
    '''
    Compara dos ids de películas
    '''
    if int(recordA) == int(recordB['key']):
        return 0
    elif int(recordA) > int(recordB['key']):
        return 1
    return -1 


def compareProducersByName(keyname, producer):
    """
    Compara dos nombres de productora. El primero es una cadena
    y el segundo un entry de un map
    """
    producerentry = me.getKey(producer)
    if (keyname == producerentry):
        return 0
    elif (keyname > producerentry):
        return 1
    else:
        return -1


def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de director. El primero es una cadena
    y el segundo un entry de un map
    """
    directorentry = me.getKey(producer)
    if (keyname == directorentry):
        return 0
    elif (keyname > directorentry):
        return 1
    else:
        return -1


def compareActorsByName(keyname, actor):
    """
    Compara dos nombres de actor. El primero es una cadena
    y el segundo un entry de un map
    """
    actorentry = me.getKey(actor)
    if (keyname == actorentry):
        return 0
    elif (keyname > actorentry):
        return 1
    else:
        return -1


def compareGenresByName(keyname, genre):
    #Requerimiento 4 - Sebastian Peña
    """
    Compara dos nombres de género. El primero es una cadena
    y el segundo un entry de un map
    """
    genreentry = me.getKey(genre)
    if (keyname == genreentry):
        return 0
    elif (keyname > genreentry):
        return 1
    else:
        return -1


def compareCountriesByName(keyname, country):
    """
    Compara dos nombres de país. El primero es una cadena
    y el segundo un entry de un map
    """
    countryentry = me.getKey(country)
    if (keyname == countryentry):
        return 0
    elif (keyname > countryentry):
        return 1
    else:
        return -1