"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def read_data():
    
    import csv
    
    with open ("data.csv") as filecsv:
        file = csv.reader(filecsv, delimiter = "\t")
        list=[]
        for row in file:
            list.append(row)
    return list
    

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    list = read_data()
    sum =0
    for item in list:
        sum +=int(item[1])
    return sum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista = read_data()
    letters = {}
    for item in lista:
        letter = item[0]
        if (letter in letters):
            letters[letter] +=1
        else:
            letters[letter] =1
    
    #print (letters)
    letters = dict(sorted(letters.items()))
    
    #list_of_tuplas = []
    #for key in letters:
    #    list_of_tuplas.append((key,letters[key]))
    #    #print(key,letters[key])
    #return list_of_tuplas
    return list(letters.items())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista = read_data()
    letters = {}
    for item in lista:
        letter = item[0]
        if (letter in letters):
            letters[letter] +=int(item[1])
        else:
            letters[letter] =int(item[1])
    
    letters = dict(sorted(letters.items()))
    
    #list_of_tuplas = []
    #for key in letters:
    #    list_of_tuplas.append((key,letters[key]))
    #    #print(key,letters[key])
    #return list_of_tuplas    
    return list(letters.items())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from datetime import date
    lista = read_data()
    months = {}
    for item in lista:
        year =(item[2][0:4])
        month = (item[2][5:7])
        day = (item[2][8:9])
        
        if (month in months):
            months[month] +=1
        else:
            months[month] =1
           
    months = dict(sorted(months.items()))
    
    #list_of_tuplas = []
    #for key in months:
    #    list_of_tuplas.append((key,months[key]))
    #return list_of_tuplas 
    return list(months.items())
    

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    list = read_data()
    letters = {}
    for item in list:
        letter = item[0]
        if (letter in letters):
            curr_min = letters[letter][0]
            
            curr_max = letters[letter][1]
            letters[letter][0] = min(curr_min, int(item[1]))
            letters[letter][1] = max(curr_max, int(item[1]))
        else:
            l=[]
            l.append(int(item[1]))
            l.append(int(item[1]))
            letters[letter] =l[:]
    
    letters = dict(sorted(letters.items()))
    
    list_of_tuplas = []
    for key in letters:
        list_of_tuplas.append((key,letters[key][1],letters[key][0]))
        #print(key,letters[key])
    return list_of_tuplas


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    list = read_data()
    letters = {}
    for item in list:
        dict_items = item[4].split(",")
        
        for it in dict_items:
            key = it [0:3]
            value = int(it[4:])
            if (key in letters):
                curr_min = letters[key][0]
                
                curr_max = letters[key][1]
                letters[key][0] = min(curr_min, value)
                letters[key][1] = max(curr_max, value)
            else:
                l=[]
                l.append(value)
                l.append(value)
                letters[key] =l[:]
    
    letters = dict(sorted(letters.items()))
    
    list_of_tuplas = []
    for key in letters:
        list_of_tuplas.append((key,letters[key][0],letters[key][1]))
        #print(key,letters[key])
        
    return list_of_tuplas


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista = read_data()
    numbers = {}
    for item in lista:
        letter = item[0]
        number = item[1]
        
        if (number in numbers):
            numbers[number].append(letter)
        else:
            l=[]
            l.append(letter)
            numbers[number] =l[:]

    numbers = dict(sorted(numbers.items()))
    
    #tuples_list=[]
    #for key, value in numbers.items():
    #    tuples_list.append((key,value))
    #return tuples_list
    return list(numbers.items())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    tuple_list_in = pregunta_07()
    new_tuple_list =[]
    for item in tuple_list_in:
        num, letters = item
        
        # Eliminacion de elementos repetidos
        dict_1 = dict.fromkeys(letters)
        # Organizaion de elementos de dict_!
        dict_1 = dict(sorted(dict_1.items()))
        #conversion nuevamente a lista
        letters_2 = list(dict_1)
        new_tuple_list.append((num, letters_2))
    
    return new_tuple_list


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista = read_data()
    letters = {}
    for item in lista:
        dict_items = item[4].split(",")
        
        for it in dict_items:
            key = it [0:3]
            value = int(it[4:])
            
            if (key in letters):
                letters[key] += 1
            else:
                letters[key]  = 1
            
    letters = dict(sorted(letters.items()))
    return list(letters.items())


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    
    lista = read_data()
    tuples_list=[]
    for item in lista:
        letter = item[0]
        str1 = item[3]
        str2 = item[4]
        tuples_list.append((letter,len(str1.split(",")),len(str2.split(","))))
        
        
    return tuples_list


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    lista = read_data()
    dictionary={}
    for item in lista:
        number = int(item[1])
        elem_list = item[3].split(",")
        
        for el  in elem_list:
            if (el in dictionary):
                
                dictionary[el]+=number
            else:
                dictionary[el]=number
        
    return dict(sorted(dictionary.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    
    lista = read_data()
    dictionary = {}
    for item in lista:
        letter = item[0]
        dict_items = item[4].split(",")
        sum = 0
        for it in dict_items:
            key = it [0:3]
            value = int(it[4:])
            sum+=value
        
        if (letter in dictionary) :
        
            dictionary[letter] += sum
        else:
            dictionary[letter] = sum
            
        
            
    return dict(sorted(dictionary.items()))
