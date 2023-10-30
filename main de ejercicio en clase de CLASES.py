from Motocycle import Motocycle 

mi_moto = Motocycle(
    color="Azul",
    license_plate="AC879CD",
    brand="BMW",
    model="Mostrosidad",
    manufacture_date="2022-01-15",
    top_speed=150,
    weight=200
)

mi_moto2 = Motocycle(
    color="Verde",
    license_plate="ACB423",
    brand="Honda",
    model="Estrellita",
    manufacture_date="2002-01-15",
    top_speed=450,
    weight=250
)

mi_moto.start_motor()
mi_moto.start_motor()
mi_moto.stop_motor()
mi_moto.stop_motor()

mi_moto.price = 20000
mi_moto2.price = 50000
mi_moto.ask_price()
mi_moto2.ask_price()






