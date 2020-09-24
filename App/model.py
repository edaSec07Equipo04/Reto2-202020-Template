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

def nueva_lista(estructura,):
    
    lista = lt.newList(datastructure= 'ARRAY_LIST',cmpfunction= None)
        
    return lista
 
def añanir_pelicula(lista,pelicula):
 
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
    catalog['moviesIds'] = mp.newMap(329999,
                                     maptype= 'PROBING',
                                     loadfactor=0.5,
                                     comparefunction=compareRecordIds)
    catalog['producers'] = mp.newMap(36007,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=compareProducersByName)
    catalog['directors']=mp.newMap(85991,
                                  maptype= 'PROBING',
                                  loadfactor=0.5,
                                  comparefunction=compareDirectorsByName)
    catalog['actors']=mp.newMap(350,
                               maptype= 'PROBING',
                               loadfactor=0.5,
                               comparefunction=compareActorsByName)
    catalog['genres']=mp.newMap(200,
                               maptype= 'PROBING',
                               loadfactor=0.5,
                               comparefunction=compareGenresByName)
    catalog['countries']=mp.newMap(239,
                               maptype= 'PROBING',
                               loadfactor=0.5,
                               comparefunction=compareCountriesByName)
    catalog['directorsIds']=mp.newMap(329999,
                                     maptype= 'PROBING',
                                     loadfactor=0.5,
                                     comparefunction=compareRecordIds)                                                             
    return catalog


def newProducer(company):
    """
    Crea una nueva estructura para modelar las películas de una productora
    y su promedio de calificación
    """
    producer = {'name': '', 'movies':None,'vote_average': 0}
    producer['name'] = company
    producer['movies'] = lt.newList('ARRAY_LIST',compareProducersByName)
    return producer

def newDirector(director_name):
    """
    Crea una nueva estructura para modelar las películas de un director
    y su promedio de calificación
    """
    director = {'name':'','movies':None,'vote_average':0}
    director['name'] = director_name
    director['movies']=lt.newList('ARRAY_LIST',compareDirectorsByName)
    return director

def newCountry(country_name):
    """
    Crea una nueva estructura para modelar las películas de un país
    y el director que dirigió cada película
    """
    country = {'name':'','movies':None}
    country['name']=country_name
    country['movies']=lt.newList('ARRAY_LIST',compareCountriesByName)
    return country

    

# Funciones para agregar informacion al catalogo

def addMovie(catalog,movie):
    """
    Esta funcion adiciona una película a la lista de películas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['movies'],movie)
    mp.put(catalog['moviesIds'],movie['id'],movie)

def addDirectorId(catalog,movie):
    """
    Esta funcion adiciona una película a la lista de películas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    mp.put(catalog['directorsIds'],movie['id'],movie)

def addMovieProducer(catalog,company,movie):
    """
    Crea una nueva estructura para modelar las películas de una productora de cine
    y su promedio de calificación
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


def addMovieDirector(catalog,director,movie):
    """
    Crea una nueva estructura para modelar las películas de un director de cine
    y su promedio de calificación
    """
    directors = catalog['directors']
    existdirector = mp.contains(directors,director)
    if existdirector:
        entry = mp.get(directors,director)
        data = me.getValue(entry)
    else:
        data = newDirector(director)
        mp.put(directors,director,data)
    lt.addLast(data['movies'],movie)

def addCountry(catalog,country,movie):
    """
    Crea una nueva estructura para modelar las películas de un país
    y el director que dirigió cada película
    """
    countries = catalog['countries']
    existcountry = mp.contains(countries,country)
    if existcountry:
        entry = mp.get(countries,country)
        data = me.getValue(entry)
    else:
        data = newCountry(country)
        mp.put(countries,country,data)
    lt.addLast(data['movies'],movie)

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
            añanir_pelicula(lst,movie['title'])
        return lst['elements'],totalMovies,vote_average
    
    return None

def getMoviesByDirector(catalog,director_name): 
    director = mp.get(catalog['directors'],director_name)
    movieavg = 0
    if director:
        result = me.getValue(director)
        for i in range(1, lt.size(result['movies'])+1):
            index = lt.getElement(result['movies'],i)
    
            mapKey = mp.get(catalog['moviesIds'],index)
            if mapKey:
                mapValue = me.getValue(mapKey)
                movieavg += float(mapValue['vote_average'])
                lt.changeInfo(result['movies'],i,mapValue['title'])
        totalMovies = lt.size(result['movies'])
        result['vote_average'] = round((movieavg/totalMovies),5)
        return(result['movies']['elements'],result['vote_average'],totalMovies)
    else:
        return 0

def getMoviesByCountry(catalog,country_name):
    country = mp.get(catalog['countries'],country_name)
    if country:
        result = me.getValue(country)
        for i in range(1,lt.size(result['movies'])+1):
            info = lt.getElement(result['movies'],i)
            mapKey=mp.get(catalog['directorsIds'],info['elements'][2])
            if mapKey:
                mapValue = me.getValue(mapKey)
                lt.changeInfo(info,3,mapValue['director_name'])
        return result        
    else:
        return 0


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

def directorsSize(catalog):
    """
    Número de directores en el catálogo
    """
    return mp.size(catalog['directors'])

def countriesSize(catalog):
    """
    Número de paises en el catálogo
    """
    return mp.size(catalog['countries'])

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
    directorentry = me.getKey(director)
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