import os

def populate_client():
    temp = add_user(username="dillonamadeo", email="dillon@gmail.com", password="dillon")
    add_client(user=temp[0], phone="14045", address="Hall 13")
    temp = add_user(username="williamwijaya", email="william@gmail.com", password="william")
    add_client(user=temp[0], phone="14045", address="Hall 11")
    temp = add_user(username="jonathanlie", email="jonathan@gmail.com", password="jonathan")
    add_client(user=temp[0], phone="14045", address="Hall 15")
    temp = add_user(username="iryantojaya", email="iryanto@gmail.com", password="iryanto")
    add_client(user=temp[0], phone="14045", address="Hall 11")
    temp = add_user(username="sutrisnodwi", email="sutrisno@gmail.com", password="sutrisno")
    add_client(user=temp[0], phone="14045", address="Hall 11")
    temp = add_user(username="albertdatui", email="albert@gmail.com", password="albert")
    add_client(user=temp[0], phone="14045", address="Hall 15")

def add_client(user, phone, address):
    p = Client.objects.get_or_create(user=user, phone=phone, address=address)
    return p

def add_user(username, email, password):
    p = User.objects.get_or_create(username=username, email=email, password=password)
    return p
    
if __name__ == '__main__':
    print ("Starting User Population Script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ew_backend.settings')
    from api.models import Client
    from django.contrib.auth.models import User
    import django
    django.setup()
    populate_client()
