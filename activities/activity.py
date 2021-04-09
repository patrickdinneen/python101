from dataclasses import dataclass, field
from enum import Enum
from typing import Set, List
import random


class LocationType(Enum):
    POOL = 1
    OPEN_BODY_OF_WATER = 2
    HIKING_TRAIL = 3
    FOOTPATH = 4
    CYCLE_PATH = 5


@dataclass
class Location:
    name: str
    types: Set[LocationType] = field(default_factory=set)


@dataclass
class Activity:
    name: str
    supported_location_types: Set[LocationType] = field(default_factory=set)

    def can_be_done_at_location(self, location: Location) -> bool:
        return self.supported_location_types.intersection(location.types)

    def select_random_location(self, locations: List[Location]) -> Location:
        supported_locations = [l for l in locations
                               if self.can_be_done_at_location(l)]

        if not supported_locations:
            raise ValueError(
                f'No locations with types in {self.supported_location_types}')

        return random.choice(supported_locations)


def create_activities() -> List[Activity]:
    return [
        Activity('Cycle', supported_location_types={LocationType.CYCLE_PATH}),
        Activity('Run', supported_location_types={LocationType.FOOTPATH,
                                                  LocationType.HIKING_TRAIL}),
        Activity('Hike', supported_location_types={LocationType.HIKING_TRAIL}),
        Activity('Kayak', supported_location_types={
                 LocationType.OPEN_BODY_OF_WATER}),
        Activity('Dive', supported_location_types={
                 LocationType.OPEN_BODY_OF_WATER}),
        Activity('Swim', supported_location_types={LocationType.OPEN_BODY_OF_WATER,
                                                   LocationType.POOL}),
    ]


def create_locations() -> List[Location]:
    return [
        Location('Pipe Track', types={LocationType.HIKING_TRAIL,
                                      LocationType.CYCLE_PATH}),
        Location('Camps Bay Tide Pool', types={LocationType.POOL}),
        Location('Sea Point Pool', types={LocationType.POOL}),
        Location('Three Anchor Bay', types={LocationType.OPEN_BODY_OF_WATER}),
        Location('Hout Bay Harbour', types={LocationType.OPEN_BODY_OF_WATER}),
        Location('Secret Cthulu Beach', types={LocationType.OPEN_BODY_OF_WATER}),
        Location('Sea Point Promenade', types={LocationType.FOOTPATH,
                                               LocationType.CYCLE_PATH}),
        Location('Newlands Forest', types={LocationType.HIKING_TRAIL}),
    ]


if __name__ == '__main__':
    locations = create_locations()
    activities = create_activities()

    activity = random.choice(activities)
    location = activity.select_random_location(locations)

    print(f'Why not try {activity.name} at {location.name}?')
