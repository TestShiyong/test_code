from faker import Faker


fake = Faker(locale='de_DE')
name = fake.name()
phone = fake.phone_number()
code = fake.postcode()
address = fake.address()
city = fake.city()
print(name)
print(phone)
print(code)
print(address)
print(city)





