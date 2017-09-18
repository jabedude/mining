#!/usr/bin/env python3

from mining.zerg import Zerg
import mining
from .location import Location

class Drone(Zerg):

    health_points = 40
    carrying_capacity = 10
    move_count = 1

    def __init__(self):
        self.step_count = 0
        self.health = Drone.health_points
        self.capacity = Drone.carrying_capacity
        self.moves = Drone.move_count
        self.current_map = None
        self.position = Location(0, 0)
        self.idle = False
        self.path_queue = None  # TODO: list() of path (actions)

    def action(self, context):
        '''
        Entry point of action for Drone unit. Context information about surrounding tiles.
        '''
        self.step_count += 1
        self.current_map.update(self.position, context)
        ### TEMP ###
        if self.path_queue is None:
            if context.north == ' ' and not self.current_map.is_explored(self.position.north):
                self.position.current = self.position.north
                return 'NORTH'
            elif context.south == ' ' and not self.current_map.is_explored(self.position.south):
                self.position.current = self.position.south
                return 'SOUTH'
            elif context.east == ' ' and not self.current_map.is_explored(self.position.east):
                self.position.current = self.position.east
                return 'EAST'
            elif context.west == ' ' and not self.current_map.is_explored(self.position.west):
                self.position.current = self.position.west
                return 'WEST'
            else:
                # TODO: TELL OVERLORD TO GIVE US A PATH
                self.idle = True
                return 'CENTER'
        else:
            # TODO: EXECUTE PATH HERE
            pass
        ### TEMP ###

    def steps(self):
        '''Return the number of steps taken by drone'''
        return self.step_count

    @classmethod
    def get_init_cost(cls):
        minerals = cls.health_points // 10
        minerals += cls.carrying_capacity // 5
        minerals += cls.move_count * 3
        return minerals


class Scout(Drone):

    health_points = 20
    carrying_capacity = 5
    move_count = 3

    def __init__(self):
        super().__init__()
        self.health = Scout.health_points
        self.capacity = Scout.carrying_capacity
        self.moves = Scout.move_count


class Miner(Drone):

    health_points = 10
    carrying_capacity = 15
    move_count = 1

    def __init__(self):
        super().__init__()
        self.health = Miner.health_points
        self.capacity = Miner.carrying_capacity
        self.moves = Miner.move_count