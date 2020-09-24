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

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

ar = "ARRAY_LIST"

def initCatalog():
    """
    Llama la función de inicialización del catálogo del modelo.
    """
    # catalog es utilizado para interactuar con el mdoelo
    catalog = model.newCatalog()
    return catalog

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1 

# ___________________________________________________
#  Funciones para la la obtención de datos requeridos
# ___________________________________________________
def moviesSize(catalog):
    """
    Número de películas leidas
    """
    return model.moviesSize(catalog)

def producersSize(catalog):
    """
    Número de productoras leídas
    """
    return model.producersSize(catalog)

def directorsSize(catalog):
    """
    Número de directores leídos
    """
    return model.directorsSize(catalog)

def countriesSize(catalog):
    """
    Número de paises leídos
    """
    return model.countriesSize(catalog)

def getMoviesByProdutionCompany(catalog,producer):
    return model.getGoviesByProductionCompany(catalog,producer)

def getMoviesByDirector(catalog,director):
    return model.getMoviesByDirector(catalog,director)

def getMoviesByCountry(catalog,country):
    return model.getMoviesByCountry(catalog,country)

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadCSVFile (file, cmpfunction):
   
    lst = model.nueva_lista(ar)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8-sig") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                
                model.añanir_pelicula(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies(catalog,moviesfile):
    """
    Carga cada una de las lineas del archivo de películas.
    - Se agrega cada película al catalogo de películas
    """
    moviesfile = cf.data_dir + moviesfile
    dialect = csv.excel()
    dialect.delimiter=';'
    try:
        with open(moviesfile,encoding="utf-8-sig") as csvfile:
            row = csv.DictReader(csvfile,dialect=dialect)
            for movie in row:
                lst = model.nueva_lista(ar)
                model.addMovie(catalog,movie)
                producers = movie['production_companies'] # Se obtienen las productoras
                countries = movie['production_countries'] # Se obtienen los países
                release_date = movie['release_date']
                year = release_date.split("/")
                model.addMovieProducer(catalog,producers,movie)
                model.añanir_pelicula(lst,movie['title'])
                model.añanir_pelicula(lst,year[-1])
                model.añanir_pelicula(lst,movie['id'])
                model.addCountry(catalog,countries,lst)
    except:
        print("Hubo un error en la carga de archivos")


def loadCasting(catalog,castingfile):
    """
    Carga cada una de las lineas del archivo de películas.
    - Se agrega cada película al catalogo de películas
    """
    castingfile = cf.data_dir + castingfile
    dialect = csv.excel()
    dialect.delimiter=';'
    try:
        with open(castingfile,encoding="utf-8-sig") as csvfile:
            row = csv.DictReader(csvfile,dialect=dialect)
            for movie in row:
                model.addDirectorId(catalog,movie)
                directors = movie['director_name'] # Se obtienen los productores               
                model.addMovieDirector(catalog,directors,movie['id'])
    except:
        print("Hubo un error en la carga de archivos")
    

def loadData(catalog,moviesfile,castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadMovies(catalog,moviesfile)
    loadCasting(catalog,castingfile)