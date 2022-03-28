import logging
logging.basicConfig(level=logging.DEBUG)

intro = input ("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
calc_result = None
num_1 = float(input("Podaj składnik 1. "))
num_2 = float(input("Podaj składnik 2. "))

if intro == '1':
    logging.info(f"Dodaję {num_1} i {num_2}")
    calc_result = num_1 + num_2 
elif intro == '2':
    logging.info(f'Od {num_2} odejmuję {num_2}')
    calc_result = num_1 - num_2
elif intro == '3':
    logging.info(f'{num_1} mnożę przez {num_2}')
    calc_result = num_1 * num_2
elif intro == '4':
    logging.info(f'{num_1} dzielę przez {num_2}')
    calc_result = num_1/num_2 
else:
    logging.info ("Podana liczba poza zakresem - nie ma przypisanego działania")

