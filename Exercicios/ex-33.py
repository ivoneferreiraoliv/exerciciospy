ladoTriangulo1 = float(input('Digite o primeiro lado do triângulo: '))
ladoTriangulo2 = float(input('Digite o segundo lado do triângulo: '))
ladoTriangulo3 = float(input('Digite o terceiro lado do triângulo: '))
if ladoTriangulo1 + ladoTriangulo2 > ladoTriangulo3 and ladoTriangulo1 + ladoTriangulo3 > ladoTriangulo2 and ladoTriangulo2 + ladoTriangulo3 > ladoTriangulo1:
    print('Os lados {}, {} e {} formam um triângulo'.format(ladoTriangulo1, ladoTriangulo2, ladoTriangulo3))
if ladoTriangulo1 == ladoTriangulo2 and ladoTriangulo1 == ladoTriangulo3:
    print('O triângulo é equilátero')
elif ladoTriangulo1 == ladoTriangulo2 or ladoTriangulo1 == ladoTriangulo3 or ladoTriangulo2 == ladoTriangulo3:
    print('O triângulo é isósceles')
elif ladoTriangulo1 != ladoTriangulo2 and ladoTriangulo1 != ladoTriangulo3 and ladoTriangulo2 != ladoTriangulo3:
    print('O triângulo é escaleno')
else:
    print('Os lados {}, {} e {} não formam um triângulo'.format(ladoTriangulo1, ladoTriangulo2, ladoTriangulo3))
    
























