#Pobieranie danych od uzytkownika

ileKotow = input("podaj jak wysokie schody z kotow chcesz miec: ")
#print('ileKotow jest:', type(ileKotow) )
#zamiana napisu na liczbe
try:
    ileKotow = int(ileKotow)
except ValueError as owcaError:
    #tutaj piszecie instrukcje ktore sie wykonaja kiedy zdarzy sei error
    print(f'Wystąpil {owcaError},program przyjmuje tylko liczby naturalne')

