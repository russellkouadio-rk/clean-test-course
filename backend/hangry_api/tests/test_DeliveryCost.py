import pytest
from api.controllers import Delivery
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


@pytest.mark.parametrize("quantity,distance", [(0, 0), (5, 6), (6, 3), (11, 3)])
def test_DefaultFeeAtTierBoundaries(quantity, distance):
  order = MockSet(MockModel(quantity=quantity))
  assert Delivery.calculate(order, distance) == 3.50


@pytest.mark.parametrize("quantity,distance", [(6, 4), (10, 6), (11, 5)])
def test_MiddleFeeAtTierBoundaries(quantity, distance):
  order = MockSet(MockModel(quantity=quantity))
  assert Delivery.calculate(order, distance) == 5
