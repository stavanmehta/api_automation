from main.apiclient import APIClient
from main.uris import FAVOURITE_RESTAURANTS


class FavouriteRestaurants(APIClient):
    def __init__(self, auth_token):
        """
        Initialize FavouriteRestaurants with auth_token and invoke parent APIClient constructor
        :param auth_token: <str> sha256() key
        """
        super(FavouriteRestaurants, self).__init__()
        self.headers = {'x-chownow-auth-token': auth_token}

    def get_favourite_restaurants(self):
        """
        Get list of favourite restaurants
        :return: <list> favourite restaurants
        """
        response = self.get(FAVOURITE_RESTAURANTS)
        if response["status_code"] == 200:
            return response["text"]
        return []

    def add_favourite_restaurants(self, name, rating):
        """
        Add favourite restaurant to database
        :param name:<str> restaurant name
        :param rating: <int> restaurant rating
        :return: <dict>
        """
        payload = {"restaurant": name, "rating": rating}
        return self.post(FAVOURITE_RESTAURANTS, request_payload=payload, request_headers=self.headers)

    def update_favourite_restaurants(self, name, rating):
        """
        Update favourite restaurant
        :param name:<str> restaurant name
        :param rating: <int> restaurant rating
        :return: <dict>
        """
        payload = {"restaurant": name, "rating": rating}
        return self.put(FAVOURITE_RESTAURANTS, request_payload=payload, request_headers=self.headers)

    def delete_favourite_restaurants(self, name):
        """
        Delete favourite restaurant to database
        :param name:<str> restaurant name
        :return: <dict>
        """
        uri = "{feature_uri}?restaurant={restaurant}".format(feature_uri=FAVOURITE_RESTAURANTS, restaurant=name)
        return self.delete(uri, request_headers=self.headers)
