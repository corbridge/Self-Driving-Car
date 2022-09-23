from random import randint

color = {

    'rojo':1,
    'verde':2,
    'blanco':3,
    'naranja':4,
    'morado':5
}

n = randint(1,5)

if n == color['blanco']:
    print('blanco')
elif n == color['morado']:
    print('morado')
elif n == color['naranja']:
    print('naranja')
elif n == color['rojo']:
    print('verde')
else:
    print('rojo')
