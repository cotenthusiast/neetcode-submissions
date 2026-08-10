class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = 0
        fleet_time = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if fleet_time == 0:
                fleets = 1
                fleet_time = time
            elif time > fleet_time:
                fleet_time = time
                fleets += 1
        return fleets