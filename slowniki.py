przykladowy_slownik = {'klucz' : 'wartosc', 'inny klucz' : 'inna wartość'}
print(przykladowy_slownik)
print(przykladowy_slownik['klucz'])

przykladowy_slownik['kolejnt klucz'] = 'jego wartość'
print(przykladowy_slownik)

#print(przykladowy_slownik['nieistniejący klucz'])
print(przykladowy_slownik.get('nieistniejący klucz', 'Słownik nie zawiera takiego klucza.'))
print(przykladowy_slownik.get('inny klucz', 'Słownik nie zawiera takiego klucza.'))

if 'klucz' in przykladowy_slownik:
    print("Ten klucz znajduje się w słowniku.")
else:
    print("Ten klucz NIE znajduje się w słowniku.")

przykladowy_slownik['klucz'] = 'próba dodania takiego samego klucza'
print(przykladowy_slownik)

przykladowy_slownik['klucz będący słownikiem'] = {'a' : 345, 'b' : 'asdsa'}
print(przykladowy_slownik)
print(przykladowy_slownik['klucz będący słownikiem'])
print(przykladowy_slownik['klucz będący słownikiem']['b'])

przykladowy_slownik['klucz będący listą'] = [234, 'sdfsdf', 324.6, False, {'r' : 345, 'h' : 'dsfsd', 1 : 23423}]
print(przykladowy_slownik)
print(przykladowy_slownik['klucz będący listą'][4][1])