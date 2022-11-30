
# input untuk parameter celcius dan fahrenheit
celc = float(input('Masukan derajat Celcius: '))
fahr = float(input('Masukan derajat Fahrenheit: '))

# function untuk konversi temperatur
def CelctoKelv (celc):
    return celc + 273.15

def CelctoFahr (celc):
    return (celc * (9/5)) + 32

def FahrtoCelc (fahr):
    return (fahr - 32) * 5/9 

def FahrtoKelv (fahr):
    return ((fahr - 32)/1.8) + 273.15

# function untuk memanggil
KelvinC = CelctoKelv(celc)
Farenheit = CelctoFahr(celc)
Celcius = FahrtoCelc(fahr)
KelvinF = FahrtoKelv(fahr)

#print untuk statment
print('Celcius to Kelvin = ', KelvinC, ' K')
print('Celcius to Fahrenheit = ', Farenheit, ' F')
print('Fahrenheit to Celcius = ', Celcius, ' C')
print('Fahrenheit to Kelvin = ', KelvinF, ' K')