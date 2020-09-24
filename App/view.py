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
#moviesfile = "theMoviesdb/Prueba.csv"
castingfile = 'theMoviesdb/MoviesCastingRaw-small.csv'
#castingfile = 'theMoviesdb/AllMoviesCastingRaw.csv'



# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________






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
        print('Promedio de calificación de las películas de esta productora: '+str(round(vote_average,4)))
        

def printMoviesByDirector(director):
    '''
    Imprime los datos del director
    '''
    data = controller.getMoviesByDirector(cont,director)
    if data== 0:
        print("No se halló el director ingresado")
        return -1
    else:       
        titles,vote_average,quantity=data
        print('Películas dirigidas por el director:')
        print(titles)
        print('Cantidad de películas dirigidas por el director: '+str(quantity))
        print('Promedio de calificación de las películas de este director: '+str(vote_average))


def printMoviesByActor(actor):
    '''
    Imprime los datos del actor
    '''
    return 0


def printMoviesByGenre(genre):
    #Requerimiento 4 - Sebastian Peña
    '''
    Imprime los datos del género
    '''
    if controller.getMoviesByGenres(cont,genre)== None:
        print("No se halló el genero ingresado")
        return -1
    else: 
        titles,quantity,vote_count = controller.getMoviesByGenres(cont,genre)
        print('Peliculas con el genero ingresado : ')
        print(titles)
        print('Cantidad de peliculas con el genero ingresado: ' + str(quantity))
        print('Promedio de votos con el genero ingresado es: ' + str(round(vote_count,4)))




def printMoviesByCountry(country):
    '''
    Imprime los datos del país
    '''
    result = controller.getMoviesByCountry(cont,country)
    for i in range(1,lt.size(result['movies'])+1):
        a = lt.getElement(result['movies'],i)
        print(a['elements'])
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

#---------------------------------------------------
#   Menú principal
#---------------------------------------------------


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0])==1:
        print("Inicializando catálogo...")
        try:
            cont = controller.initCatalog()
            print("Catálogo inicializado exitosamente!")
        except:
            ("Se ha producido un error inicializando el catálogo")

    elif int(inputs[0]) == 2:
        print("Cargando información...")
        controller.loadData(cont,moviesfile,castingfile)
        print('Películas cargadas: '+ str(controller.moviesSize(cont)))
        print('Productoras cargadas: '+ str(controller.producersSize(cont)))
        print('Generos cargados: '+ str(controller.genresSize(cont)))
        print('Directores cargados: ' + str(controller.directorsSize(cont)))
        print('Paises cargados: '+str(controller.countriesSize(cont)))
        print('Información cargada con éxito')

    elif int(inputs[0]) == 3:
        producer = input("Buscando las películas de la productora?: ")
        producer = producer.title()
        printMoviesByProductionCompany(producer)
    
    elif int(inputs[0]) == 4:
        director = input("Buscando las películas del director?: ")
        director=director.title()
        printMoviesByDirector(director)

    elif int(inputs[0]) == 5:
        actor = input("Buscando las películas del actor?: ")

    elif int(inputs[0]) == 6:
        genero = input("Buscando las películas del género?: ")
        genero = genero.title()
        printMoviesByGenre(genero)

    elif int(inputs[0]) == 7:
        pais = input("Buscando las películas del país?: ")
        pais = pais.title()
        printMoviesByCountry(pais)
    else:
        sys.exit(0)
sys.exit(0)

        
