import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj1.settings')
django.setup()

from app1.models import *
from faker import Faker
from random import *
fake=Faker()

def phone_num():
    f = str(randint(6,9))
    for i in range(10):
        f = f + str(randint(0,9))
    return int(f)

def gen_data(n):
    for i in range(n):
        eid = fake.random_int(min=1,max=100)
        efnm = fake.first_name()
        elnm = fake.last_name()
        edob = fake.date()
        email = fake.email()
        eaddr = fake.address()
        epn = phone_num()
        obj = Employee.objects.get_or_create(eid=eid,efnm=efnm,elnm=elnm,edob=edob,email=email,eaddr=eaddr,epn=epn)

gen_data(10)