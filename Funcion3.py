def ordenarCaracteres(cadena:str)->str:
   cadena_ordenada = sorted(cadena)
   cadena_ordenada = ("").join(cadena_ordenada)
   return cadena_ordenada