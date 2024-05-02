def ripf(fun,x0,err,mit):

    g1=fun(x0)
    gprima1=fun(x0)
    if abs(gprima1)>=1:
        print("No es posible usar el método pues g no converge")
        return None
    
    hx=[]

    for i in range(mit):
        hx.append(x0)

        if abs(g1 - x0)<err:
            print(f"se encontró la raiz y es {x0}, o por lo menos cumple con el error solicitado")
            break
        x0=g1
        g1=fun(x0)

    

    return hx
