import random
import string
from datetime import date, timedelta

def generate_full_name():

    names = [
        "Juan",
        "María",
        "Carlos",
        "Ana",
        "Luis",
        "Gabriela",
        "José",
        "Laura",
        "Miguel",
        "Sofía",
        "Alejandro",
        "Valentina",
        "Ricardo",
        "Carolina",
        "Eduardo",
        "Andrea",
        "Javier",
        "Natalia",
        "Pedro",
        "Isabella"
    ]



    first_lastnames = [
        "García",
        "Rodríguez",
        "González",
        "Hernández",
        "López",
        "Martínez",
        "Pérez",
        "Fernández",
        "Gómez",
        "Díaz",
        "Torres",
        "Ramírez",
        "Flores",
        "Silva",
        "Vargas",
        "Cruz",
        "Morales",
        "Ortega",
        "Rojas",
        "Sánchez"
    ]

    second_lastnames = [
        "Alvarez",
        "Castro",
        "Chavez",
        "Espinosa",
        "Guerra",
        "Lara",
        "Mendoza",
        "Miranda",
        "Montoya",
        "Navarro",
        "Orozco",
        "Ponce",
        "Quintero",
        "Ramos",
        "Reyes",
        "Salazar",
        "Soto",
        "Valdez",
        "Vega",
        "Zamora"
    ]

    return f"{random.choice(names)} {random.choice(first_lastnames)} {random.choice(second_lastnames)}"

def generate_password():
    
    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(12))

    return password

def generate_birthdate():

    today = date.today()
    eighteen_years_ago = today - timedelta(days=365 * 18)
    twenty_five_years_ago = today - timedelta(days=365 * 25)

    start_date = twenty_five_years_ago.replace(year=twenty_five_years_ago.year + 1)
    end_date = eighteen_years_ago.replace(year=eighteen_years_ago.year - 1)
    

    birthdate = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    return birthdate.strftime("%d/%m/%Y")