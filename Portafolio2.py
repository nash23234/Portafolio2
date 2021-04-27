"""
Nombre: Invertir lista
Entrada: Lista
Salida: Lista invertida
Restricciones: Si la lista esta vacia retonar 0
"""
def invertirLista(lista):
    if (isinstance(lista,list)):
        if lista==[]:
            return 0
        else:
             return invertirLista_aux(lista,[])
    
def invertirLista_aux(lista,res):
    if lista==[]:
        return res
    else:
        return invertirLista_aux(lista[:-1],res+[lista[-1]])

"""
Nombre: Extremo Lista
Entrada: Lista
Salida: Mostrar el número menor y mayor de la lista
Restricciones: La lista no puede estar vacia
"""
def  extremoLista(lista):
    if (isinstance(lista,list)):
        if lista==[]:
            return "ERROR"
        else:
            return extremoLista_aux(lista)
    else:
         print("Debe ser una lista")
        

def extremoLista_aux(lista):
    if(validarint(lista)==True):
        return acomodarLista(lista,[])
    else:
        return "Error"

def acomodarLista(lista,res):
    if lista ==[]:
        return res
    else:
        menor=ubicarmenor(lista,lista[0])
        mayor=ubicarmayor(lista,lista[0])
        return [menor]+[mayor]
  

def ubicarmenor(lista,res):
    if lista==[]:
        return res
    elif lista[0]<res:
        return ubicarmenor(lista[1:],lista[0])
    else:
        return ubicarmenor(lista[1:],res)

def ubicarmayor(lista,res):
    if lista==[]:
        return res
    elif lista[0]>res:
        return ubicarmayor(lista[1:],lista[0])
    else:
        return ubicarmayor(lista[1:],res)

def validarint(lista):
    if lista ==[] :
        return True 
    else:
        if (isinstance(lista[0],int)): 
            return validarint(lista[1:])
        else:
            False
"""
Nombre: Eliminar Digitos
Entrada: lista1, lista2
Salida: La lista nueva sin el número que se eliminó
Restricciones: La lista no debe estar vacía
"""

def eliminarDigito(numero,numero1):
    if (isinstance(numero,int) and isinstance(numero1,int)):
        if numero ==0 and numero1==0:
            return "Error"
        else:
            numero=str(numero)
            numero1=str(numero1)
            return eliminarDigitoaux(numero,numero1,"")

def eliminarDigitoaux(numero,numero1,res):
    if numero=="":
        return int (res)
    elif numero[0] ==numero1:
        return eliminarDigitoaux(numero[1:],numero1,res)
    else:
        return eliminarDigitoaux(numero[1:],numero1,res+numero[0])#12,3,12,34,2 [-1].[1:]
        
    
"""
Nombre: niveles lista
Entrada: lista
Salida: Cantidad de lista existentes en una sublista
Restricciones: Que sea lista
"""

def niveleslista(lista):
    if (isinstance(lista,list)):
        return niveleslista_aux(lista,[])
    else:
        return "Debe ser una lista"

def niveleslista_aux(lista,res):
    if lista ==[]:
        return res
    elif(isinstance(lista[0],list)):
       cont=contarlistas(lista[0],1)
       return niveleslista_aux(lista[1:],res+[cont])
    else:
        return niveleslista_aux(lista[1:],res+[0])

def contarlistas(lista,res):
    if lista ==[]:
        return res
    else:
        if (isinstance(lista[0],list)):
            return contarlistas(lista[0],res+1)
        else:
            return 1

"""
Nombre: obtener Indices Lista Vectores
Entrada: v1,v2,v3
Salida: Una lista con los 3 vectores con los indices que marcaban cero y negativos
Restricciones: Debe ser una lista
"""
def obtenerIndiceslistaVectores(v1,v2,v3):
    if(isinstance(v1,list) and isinstance(v2,list) and isinstance(v3,list)):
        if (tamañodelista(v1) == tamañodelista(v2) == tamañodelista(v3)):
            if (validarint1(v1,v2,v3)):
                v4=indince(v1,0,[])
                v5=indince(v2,0,[])
                v6=indince(v3,0,[])
                v7=[v4]+[v5]+[v6]
                return v7
            else:
                return -1
        else:
            return -1
    else:
        return "Debe ser una lista"
            
           
def indince(vector,cont,lista):
    if vector== []:
        return lista
    elif vector[0]<=0:
        return indince (vector[1:],cont+1,lista+[cont])
    else:
        return indince(vector[1:],cont+1,lista)

def tamañodelista(v1):
    if v1 == 0:
        print ("La lista no puede estar vacia")
    else:
        return tamañodelistaA(v1,0)

def tamañodelistaA(vector,resultado):
    if vector==[]:
        return resultado
    else:
        return tamañodelistaA(vector[1:],resultado+1)

def validarint1(vector1,vector2,vector3):
    if vector1 ==[] and vector2== [] and vector3==[]:
        return "La lista no debe estar vacia"
    else:
        if (isinstance(vector1[0],int) and isinstance(vector2[0],int) and isinstance(vector3[0],int)):
            return validarint1(vector1[1:],vector2[1:],vector3[1:])
        else:
            return False
