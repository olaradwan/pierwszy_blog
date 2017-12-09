#imie = 'Ala'
#if imie == 'Ania':
#    print('Czesc, Aniu!')
#elif imie == 'Ola':
#    print == ('Czesc, Ola!')
#else:
#    print('czesc, nieznajomy')

# odleglosc = 7
# if odleglosc < 5:
#     print('wow ale blisko')
# elif 5 <= odleglosc < 10:
#     print('dosyc blisko')
# elif 10 <= odleglosc < 20:
#     print('zaczyna sie robic daleko')
# else:
#     print('o matko, jak daleko!')

# def hej(imie):
#     print('Hello '+ imie)

# imiona = ['Ania', 'Kasia', 'Tomek']

# for imie in imiona:
#     hej(imie)

def jak_daleko(odleglosc):
    if odleglosc < 5:
        print('wow ale blisko')
    elif 5 <= odleglosc < 10:
        print('dosyc blisko')
    elif 10 <= odleglosc < 20:
        print('zaczyna sie robic daleko')
    else:
        print('o matko, jak daleko!')

odleglosci = [11, 7, 166]
for odleglosc in odleglosci:
    jak_daleko(odleglosc)

for i in range(1, 10):
    print(i)

# jak_daleko(11)
# jak_daleko(7)
# jak_daleko(166)