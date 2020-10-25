from vehicle import Vehicle


class Car(Vehicle):  # ereditarietà

    def brag(self):
        print('Look how cool my car is!')


car1 = Car()
car1.drive()

car1.add_warning('ciao')
# car1.__warnings.append([])

#  stampa l'oggetto come un dictionary (oppure possiamo aggiungere un dunder method repr nella classe)
print(car1.__dict__)

print(car1)  # usando __repr__ ora stampiamo qualcosa di leggibile anche così

car2 = Car(200)
car2.drive()

car3 = Car(200)
car3.drive()
