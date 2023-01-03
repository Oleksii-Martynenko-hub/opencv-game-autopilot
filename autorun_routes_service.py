from typing import TypedDict

from json_data_service import JSONService


class RouteType(TypedDict):
    location: str
    from_: str
    to: str
    scale: float
    points: list[tuple[int, int]]


class RoutesService:
    path = 'routes/'
    divider = '__'

    def __init__(self):
        self.data = JSONService()

    def add_route(self, route: RouteType):
        filename = self.path + route['location'] + self.divider + route['from_'] + self.divider + route['to']
        self.data.create_data(filename, dict(route))

    def get_route(self, filename) -> RouteType:
        return self.data.read_data(filename=self.path + filename)

    @staticmethod
    def reverse_route(route: RouteType):
        reversed_points = route['points'].copy()
        reversed_points.reverse()

        reversed_route: RouteType = {
            'location': route['location'],
            'from_': route['to'],
            'to': route['from_'],
            'scale': float(route['scale']),
            'points': reversed_points
        }

        return reversed_route
