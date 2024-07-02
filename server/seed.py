from models import db, Customer, Item, Review

def seed():
    db.drop_all()
    db.create_all()

    customer1 = Customer(name="Tal Yuri")
    customer2 = Customer(name="Alex Doe")

    item1 = Item(name="Laptop Backpack", price=49.99)
    item2 = Item(name="Insulated Coffee Mug", price=9.99)

    review1 = Review(comment="Great backpack!", customer=customer1, item=item1)
    review2 = Review(comment="Keeps coffee hot!", customer=customer1, item=item2)

    db.session.add_all([customer1, customer2, item1, item2, review1, review2])
    db.session.commit()

if __name__ == "__main__":
    seed()
