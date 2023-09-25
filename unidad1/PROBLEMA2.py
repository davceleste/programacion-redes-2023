import math

def leer_valor():
    valor = float(input("Ingresa un valor: "))
    return valor

def formula_general(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return None  
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
        
if __name__ == "__main__":
    a = leer_valor()
    b = leer_valor()
    c = leer_valor()
   
    solucion = formula_general(a, b, c)

    if solucion:
        x1, x2 = solucion
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
    else:
        print("No hay soluciones reales.")







