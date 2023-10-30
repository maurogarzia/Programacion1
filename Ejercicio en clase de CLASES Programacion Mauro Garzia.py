class Motocycle:
    
    state = "New"
    motor = False

    def __init__(self,color, license_plate, brand, model, manufacture_date, top_speed, weight, fuel_liters = 10, number_of_wheels = 2):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.number_of_wheels = number_of_wheels
        self.brand = brand
        self.model = model
        self.manufacture_date = manufacture_date
        self.top_speed = top_speed
        self.weight = weight
 
    def start_motor(self):
        if not self.motor:
            print("El motor ha arrancado")
            self.motor = True
        else:
            print("El motor ya estaba en marcha")

    def stop_motor(self):
        if self.motor:
            print("El motor se ha detenido")
            self.motor = False
        else:
            print("El motor ya estaba detenido")

    def ask_price(self):
        
        print(f"El precio de la motocicleta {self.brand} {self.model} es de ${self.price}")
        


    