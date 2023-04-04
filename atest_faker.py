from faker import Faker


fake = Faker(locale='it_IT')
name = fake.name()
phone = fake.phone_number()
code = fake.postcode()
print(name)
print(phone)
print(code)





