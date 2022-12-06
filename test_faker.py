from faker import Faker

fake = Faker("fr_FR")
for i in range(1000):
     # Raises a UniquenessExceptio
    fake.unique.street_address()
    fake.city()
    fake.unique.postcode()
