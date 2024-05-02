def rnewton(fun,x0,err,mit):
    hx=[]
    hf=[]
  
    for i in range(mit):
       f,df=fun(x0)
       if df==0:
           print("la derivada es nula en ese punto, no se puede continuar con el metodo de newton")
           break
       xn=x0-(f/df)
       x0=xn
       hx.append(x0)
       hf.append(f)


       if abs(x0-xn)/abs(x0)<err or abs(f)<err:
           print("Se encontraron las condiciones menores al error solicitado")
           break
    return hx,hf
def fun(x,a):
    f=x
    df=a
    return f,df