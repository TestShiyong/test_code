from faker import Faker


fake = Faker(locale='en_US')
name = fake.name()
phone = fake.phone_number()
code = fake.postcode()
address = fake.address()
print(name)
print(phone)
print(code)
print(address)





