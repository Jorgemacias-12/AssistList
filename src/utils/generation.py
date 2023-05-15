import random
import string


def generate_full_name():

    names = ['Juan', 'Pedro', 'María', 'Laura', 'Carlos', 'Ana', 'Luis']
    last_names = ['García', 'López', 'Martínez', 'Rodríguez', 'Fernández']

    name = random.choice(names)
    last_name = random.choice(last_names)

    return f"{name} {last_name}"


def generate_password():
    
    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(12))

    return password