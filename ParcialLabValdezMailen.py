#Parcial 1 laboratorio
import matplotlib.pyplot as plt
import math
import numpy as np
#A continuación declaro las funciones necesarias para el desarrollo del programa

#Ejercicio 1
#En el caso de este método hago uso de otra funcion para calcular c debido
def MetodoBiseccion(calC,fun,I,err,mit):
    
    a,b=I[0],I[1]

    fa, fb=fun(a), fun(b)

    if fa*fb>0:
       print("No es posible aplicar el método de biseccion")
   
    hx=[]
    hf=[]

    for i in range (mit):
       c=calC(a,b)
       fc=fun(c)

       hx.append(c)
       hf.append(fc)
       if abs(fc)<err:
           print(f"La raiz es {c}, o por lo menos satisface el error aceptado, con valor {fc}")
           break
       if fa*fc<0:
           b=c
           fb=fc
       else:
           a=c
           fa=fc
    return hx, hf

def CalcularC(a,b):
    m=(3-((5)**(1/2)))/2
    c=(m*a)+((1-m)*b)
    return c

#Ejercicio 2: Metodo de Newton:
#En este caso uso DifFun para calcular la derivada deseada ya que se usa una sola vez
def MetodoNewton(DifFun,fun,x0,err,mit):
    hx=[]
    hf=[]
    df=DifFun(x0)
    if df==0:
        print("la derivada es nula en ese punto, no se puede continuar con el metodo de newton")
    for i in range(mit):
        hx.append(x0)
        f=fun(x0)
        xn=x0-(f/df)
        hf.append(f)
        fxn=fun(xn)

        if (abs(xn-x0)/abs(xn))<err or abs(fxn)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           print(f"La raiz es {xn} y tiene un valor de {fxn}")
           break
        x0=xn
    return hx,hf

#Ejercicio 3:

def Ejercicio3(CalC,Funcion_Ej3,difF):
    i=-2
    hx=[]
    hy=[]
    #Parte a: Desarrollo de los valores para el gráfico
    while i<=2:
        hx.append(i)
        fx=Funcion_Ej3(i)
        hy.append(fx)
        i=i+0.01
    fig, ax = plt.subplots()
    ax.plot(hx,hy)
    plt.show()
    #Interpretando el gráfico entiendo que raices positivas de esta función hay una sola ya que la fúncion tiende a mas infinito en el intervalo [0,+infinito)

    #Parte b raices positivas
    #Como nos referimos a raices positivas, el intervalo puede estar determinado entre 0 y mas infinito, me doy cuenta que el intérvalo ideal es entre 0 y 1


    #Con Bisección:
    BisHx=[]
    BisHy=[]
    I=[0,1]
    BisHx,BisHy = MetodoBiseccion(CalC,Funcion_Ej3,I,10**-7,100)
    k=len(BisHx)-1
    d=BisHx[k]
    RaizBiseccion=d
    print(f"la raiz proporcionada por el metodo de biseccion es {d}")

    #Con Newton:
    NewHx=[]
    NewHy=[]
    NewHx, NewHy= MetodoNewton(difF,Funcion_Ej3,1,10**-7,100)
    g=len(NewHx)-1
    h=NewHx[g]
    RaizNewton=h
    print(f"la raiz proporcionada por el metodo de newton es {h}")

    #Parte c: polinomio interpolante Metodo de Lagrange:
    x=[-1,-0.5,0.2]
    y=[Funcion_Ej3(-1),Funcion_Ej3(-0.5),Funcion_Ej3(0.2)]
    
    z = [-1 + (1*(l/100)) for l in range(201)]
    w = ilag(x,y,z)

    plt.plot(x,y,'o')
    plt.plot(z,w,'.',label='polinomio interpolante')
    plt.legend()
    plt.show()

#La funcion que determina el ejercicio 3
def Funcion_Ej3(x):
    e=math.exp(x)
    pi=math.pi
    sen=math.sin(x+pi/2)
    fx=((1/2)*e)-(sen)
    return fx

#La derivada usada para el método de newton
def difF(x0):
    e=math.exp(x0)
    pi=math.pi
    cos=math.cos(x0+pi/2)
    df=((1/2)*e)-(cos)
    return df

#Inciso c: Polinomio interpolante de Lagrange
def ilag(x, y, z):
    if len(x) != len(y):
        print("No coincide la cantidad de puntos")
        return None
    w = []
    for z_i in z:
        # sumatoria de los polinomios basicos por y_i
        w_i = 0.0
        for idx in range(len(y)):
            # productoria para generar el polinomio base l_i evaluado en z_i
            l_i = 1.
            for jdx in range(len(x)):
                if jdx != idx:
                    l_i = l_i * (z_i - x[jdx]) / (x[idx] - x[jdx])
            w_i = w_i + y[idx] * l_i
        w.append(w_i)
    return w
#Declaración del main a cargo de ejecutar el programa
def main():

    print("El siguiente programa ejecuta el punto 3:")
    print("Presione 1, si desea ejecutarlo")
    print("Presione 2 en caso de querer terminar el programa")
    bandera=False

    while bandera==False:
        a=int(input("Ingrese el punto a ejecutar: "))
        if a==1:
            Ejercicio3(CalcularC,Funcion_Ej3,difF)
            bandera=False
        elif a==2:
            print("Fin del programa")
            bandera=True
        else:
            print("Por favor ejecute un numero permitido")
            bandera=False

main()
 