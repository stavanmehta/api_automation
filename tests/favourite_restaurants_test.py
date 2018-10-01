import pytest as pytest

from main.features.login import Login
from main.features.favorite_restaurants import FavouriteRestaurants


@pytest.fixture(scope="module")
def favourite_restaurants():
    login = Login()
    login.login("AdventurousEater", "1234")
    fav_rest = FavouriteRestaurants(login.get_token())
    return fav_rest


@pytest.mark.smoketest
def test_get_favourite_restaurants(favourite_restaurants):
    restaurants = favourite_restaurants.get_favourite_restaurants()

    assert "Tocaya" in restaurants.keys(), \
        "Tocaya, not found favourite restaurants"
    assert restaurants.get("Tocaya") == 4, \
        "Expected rating for Tocaya is: 4 but found {rating}".format(rating=restaurants.get("Tocaya"))
    assert "Hash" in restaurants.keys(), \
        "Hash, not found favourite restaurants"
    assert restaurants.get("Hash") == 3, \
        "Expected rating for Hash is: 3 but found {rating}".format(rating=restaurants.get("Hash"))
    assert "Homestate" in restaurants.keys(), \
        "Homestate, not found favourite restaurants"
    assert restaurants.get("Homestate") == 5, \
        "Expected rating for Homestate is: 5 but found {rating}".format(rating=restaurants.get("Homestate"))


@pytest.mark.smoketest
def test_add_favourite_restaurants(favourite_restaurants):
    favourite_restaurants.add_favourite_restaurants('myrest', 5)
    restaurants = favourite_restaurants.get_favourite_restaurants()

    assert "myrest" in restaurants.keys(), \
        "myrest, not found favourite restaurants"
    assert restaurants.get("myrest") == 5, \
        "Expected rating for myrest is: 5 but found {rating}".format(rating=restaurants.get("myrest"))


def test_add_existing_restaurant(favourite_restaurants):
    response = favourite_restaurants.add_favourite_restaurants('Tocaya', 4)
    assert response.get("status_code") == 409
    assert response.get("text").get("error") == "Restaurant is already in the list. Choose a new restaurant."


def test_add_existing_restaurant_with_different_rating(favourite_restaurants):
    response = favourite_restaurants.add_favourite_restaurants('Tocaya', 5)
    assert response.get("status_code") == 409
    assert response.get("text").get("error") == "Restaurant is already in the list. Choose a new restaurant."


@pytest.mark.smoketest
def test_update_favourite_restaurants(favourite_restaurants):
    favourite_restaurants.update_favourite_restaurants('myrest', 4)
    restaurants = favourite_restaurants.get_favourite_restaurants()

    assert "myrest" in restaurants.keys(), \
        "myrest, not found favourite restaurants"
    assert restaurants.get("myrest") == 4, \
        "Expected rating for myrest is: 4 but found {rating}".format(rating=restaurants.get("myrest"))


def test_update_not_available_restaurant(favourite_restaurants):
    response = favourite_restaurants.update_favourite_restaurants("random-restaurant", 4)
    assert response.get("status_code") == 409
    assert response.get("text").get("error") == "Invalid restaurant selected."

    restaurants = favourite_restaurants.get_favourite_restaurants()
    assert "random-restaurant" not in restaurants.keys(), "random-restaurant, found in favourite restaurants"


@pytest.mark.smoketest
def test_delete_favourite_restaurants(favourite_restaurants):
    favourite_restaurants.delete_favourite_restaurants('myrest')
    restaurants = favourite_restaurants.get_favourite_restaurants()

    assert "myrest" not in restaurants.keys(), \
        "myrest, found in favourite restaurants"


@pytest.mark.smoketest
def test_delete_not_available_restaurant(favourite_restaurants):
    response = favourite_restaurants.delete_favourite_restaurants('myrest')
    assert response.get("status_code") == 409
    assert response.get("text").get("error") == "Invalid restaurant selected."
