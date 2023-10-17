# En el acuario se tienen solo dos especies de peces. El 40% de los peces son de especie
# azul y el 60% de los peces son de especie roja. De la especie azul 30% son machos
# mientras el 40% de la especie roja son hembras.
# a) si se selecciona un pez hembra ¿cual es la probabilidad de que sea de la especie
# azul ?
probabilidadAzul = 0.4
probabilidadRojo = 0.6

pMachoAzul = 0.3
pHembraRoja = 0.4

pHembraAzul = 1 - pMachoAzul
pMachoRojo = 1 - pHembraRoja

pHembra = (probabilidadAzul * pHembraAzul) + (probabilidadRojo * pHembraRoja)
PMacho = (probabilidadAzul * pMachoAzul) + (probabilidadRojo * pMachoRojo)

# Probabilidad de que sea Hembra azul
def CalcularProbabilidad(probabilidadUno, probabilidadDos, probabilidadTres):
    p = (probabilidadUno * probabilidadDos)/probabilidadTres
    return round(p,2)

CalcularProbabilidad(probabilidadAzul, pMachoAzul, PMacho)
