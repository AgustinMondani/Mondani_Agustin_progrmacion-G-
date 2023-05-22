def reemplazarCaracteres(cadena_caracteres:str, caracter:str, otro_caracter:str):
    contador = cadena_caracteres.count(caracter)
    cadena_nueva = cadena_caracteres.replace(caracter, otro_caracter)
    return contador, cadena_nueva