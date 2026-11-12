import pytest
from api.controllers import Delivery, Tax, Total
from django_mock_queries.query import MockSet, MockModel

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

def test_LittleItems():
  #Arrange
    order = MockSet()
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    delivery_distance = 3
  #Act
    cost = Delivery.calculate(order,delivery_distance)
  #Assert
    assert cost == 3.50


@pytest.mark.parametrize('quantity,distance,expected', [
  (0, 0, 3.50),
  (5, 4, 3.50),
  (6, 3, 3.50),
  (6, 4, 5),
  (10, 6, 5),
  (11, 5, 5),
  (11, 6, 7.50),
])
def test_DeliveryTierBoundaries(quantity, distance, expected):
  order = MockSet(MockModel(quantity=quantity))
  assert Delivery.calculate(order, distance) == expected


def test_DefaultDeliveryIncludedInTaxAndTotal():
  order = MockSet(MockModel(quantity=1, item=MockModel(price=15)))
  delivery_fee = Delivery.calculate(order, 0)
  assert Tax.calculate(15, delivery_fee) == 1.53
  assert Total.calculate(order, delivery_fee) == 20.03
