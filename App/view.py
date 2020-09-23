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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

#moviesfile = "theMoviesdb/SmallMoviesDetailsCleaned.csv"
moviesfile = "theMoviesdb/AllMoviesDetailsCleaned.csv"
castingfile = 'theMoviesdb/MoviesCastingRaw-small.csv'

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
'''
def printLoadingData(data):
    """
    Imprime la información de los datos cargados
    """
    if data:
        print('Total de películas cargadas:',lt.size(data))
        print("-------- Información de la primer película del archivo --------")
        print('Título:',data['elements'][0]['title'])
        print('Fecha de lanzamiento:',data['elements'][0]['release_date'])
        print('Promedio de votación:',data['elements'][0]['vote_average'])
        print('Total de votos:',data['elements'][0]['vote_count'])
        print('Idioma de la película:',data['elements'][0]['original_language'])
        print("-------- Información de la última película del archivo --------")
        print('Título:',data['elements'][lt.size(data)-1]['title'])
        print('Fecha de lanzamiento:',data['elements'][lt.size(data)-1]['release_date'])
        print('Promedio de votación:',data['elements'][lt.size(data)-1]['vote_average'])
        print('Total de votos:',data['elements'][lt.size(data)-1]['vote_count'])
        print('Idioma de la película:',data['elements'][lt.size(data)-1]['original_language'])
    else:
        print('No se ha logrado cargar los archivos')
'''


def printMoviesByProductionCompany(producer):
    """
    Imprime los datos de la productora de cine
    """
    if controller.getMoviesByProdutionCompany(cont,producer) == None:
        print("No se halló la productora ingresada")
        return -1
    else:
        titles,quantity,vote_average = controller.getMoviesByProdutionCompany(cont,producer)
        print('Películas producidas por la compañía:')
        print(titles)
        print('Cantidad de películas producidas por la compañía: ' + str(quantity))
        print('Promedio de calificación de las películas de esta productora: '+str(round(vote_average,2)))


def printMoviesByDirector(director):
    '''
    Imprime los datos del director
    '''
    
    return 0


def printMoviesByActor(actor):
    '''
    Imprime los datos del actor
    '''
    if controller.moviesbyactor(cont,actor) == None:
        print("No se encontró el actor ingresado")
        return -1
    else:
        
        peliculas,total,voto = controller.moviesbyactor(cont,actor)
        print("Las peliculas en las que participo " + actor + " fueron :")
        print(peliculas)
        print("El actor ha participado en " + str(total))
        print("El promedio de votación de las películas en las que participó este actor fué: " + str(voto))

    return 0


def printMoviesByGenre(genre):
    '''
    Imprime los datos del género
    '''
    return 0


def printMoviesByCountry(country):
    '''
    Imprime los datos del país
    '''
    return 0


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información")
    print("3- Consultar las películas de una productora")
    print("4- Consultar las películas de un director")
    print("5- Consultar las películas de un actor")
    print("6- Consultar las películas de un género")
    print("7- Consultar las películas de un país")
    print("0- Salir")

'''
Menú principal
'''
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    '''
    if int(inputs[0])==1:
        print("Cargando datos...")
        data = controller.loadCSVFile(moviesfile,controller.compareRecordIds)
        printLoadingData(data)
        print("Información cargada exitosamente!")
    '''
    if int(inputs[0])==1:
        print("Inicializando catálogo...")
        try:
            cont = controller.initCatalog()
            print("Catálogo inicializado exitosamente!")
        except:
            ("Se ha producido un error inicializando el catálogo")

    # elif int(inputs[0]) == 2:
     #   print("Cargando información de los archivos ....")
      #  print('Información cargada exitosamente!') 

    elif int(inputs[0]) == 2:
        print("Cargando información...")
        controller.loadData(cont,moviesfile)
        
        print('Películas cargadas: '+ str(controller.moviesSize(cont)))
        print('Productoras cargadas: '+ str(controller.producersSize(cont)))
        print('Información cargada con éxito')
        

    elif int(inputs[0]) == 3:
        producer = input("Buscando las películas de la productora?: ")
        producer = producer.title()
        printMoviesByProductionCompany(producer)

    elif int(inputs[0]) == 4:
        director = input("Buscando las películas del director?: ")

    elif int(inputs[0]) == 5:
        actor = input("Buscando las películas del actor?: ")
        actor = actor.title()
        printMoviesByActor(actor)


    elif int(inputs[0]) == 6:
        genero = input("Buscando las películas del genero?: ")

    elif int(input[0]) == 7:
        pais = input("Buscando peliculas del pais?")

    else:
        sys.exit(0)
sys.exit(0)

        
