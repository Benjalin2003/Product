import pytest
from Product import Product

@pytest.fixture
def db_product():
    db = Product("Молоко", 200)
    db.save_to_database()
    print("Продукт добавлен")

    yield db

    db.delete_from_database()
    print("Очистка завершена")

def test_set_discount(db_product):
    db_product.set_discount(20)
    assert db_product.discount == 20

def test_get_final_price_with_discount(db_product):
    db_product.set_discount(20)
    final_price = db_product.get_final_price()
    assert final_price == 80

def test_get_final_price_without_discount(db_product):
    final_price = db_product.get_final_price()
    assert final_price == 100

def test_change_price(db_product):
    db_product.change_price(150)
    assert db_product.price == 150
