from models.restaurant import Restaurant

restaurant_praca = Restaurant('praça', 'Gourmet')
restaurant_praca.get_avaluation('Gui', 10)
restaurant_praca.get_avaluation('Fe', 8)
restaurant_praca.get_avaluation('Lais', 2)

restaurant_mexican = Restaurant('Tacobell', 'Mexicano')
restaurant_japan = Restaurant('Japa', 'Japonesa')
restaurant_praca.update_status()

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()