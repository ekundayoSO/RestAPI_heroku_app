from faker import Faker

fake = Faker()


def generateLastName():
    lastName = fake.last_name()
    return lastName


# def generateCheckoutDate():
#     checkout = fake.date()
#     return checkout
