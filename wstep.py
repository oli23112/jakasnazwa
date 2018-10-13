#to jest komentarz
"""
to jest string ,lae mozna go uzyc
jako komentarz
"""
#podstawowe typy w Pythonie
#string
owca = 'Ala ma kota'
owca1 = "Ala ma kota ,kot ma Ale i koze krowe"
#fajne operacje na napisach
owca[0] #wybierze pierwszy znak z napisu
owca[0:4] #wyciąga znaki od indeksu 0 do indeksu 3
owca[3:7]
#print wyświetla w konsoli dana rzecz
print(owca[:7])
#sprawdzanie dlugosci napisow
len("napis")
#liczby
#sa dwa typy liczbowe w pythonie int i float
owcaInt = -5
owcaFloat = 7.5
#ciekawe zapisy
2**5 #32 -> 2 do 5
2e2 # 2* (10 do 2)
2e-2 # 2 * (10 do -2)
7%5 #zwraca reszte z dzielenia
#boolean
prawda = True
falsz = False
#uwaga róznice
#1 + "7" zwraca error
str(1) + "7"
print(1,"7",owca )
#formatowanie napisow
print(f'Ala ma {17} kotow : {prawda}')
