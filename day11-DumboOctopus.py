class DumboOctopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self._energy = energy
        self._flashing = False

    def energy_increase(self):
        self._energy += 1

    def attempt_flash(self):
        if self._energy == 10 and not self._flashing:
            self._flashing = True
            return True
        return False

    def step_complete(self):
        if self._flashing:
            self._energy = 0
            self._flashing = False


class OctopusGrid:
    def __init__(self, octopus_map):
        self._grid = []
        for y in range(len(octopus_map)):
            row = []
            for x in range(len(octopus_map[y].strip())):
                row.append(DumboOctopus(x, y, int(octopus_map[y][x])))
            self._grid.append(row)
        self.flash_counter = 0

    def _get_neighbors(self, x, y):
        if x == 0 and y == 0:
            return [(x + 1, y), (x, y + 1), (x + 1, y + 1)]
        elif x == 0 and y == len(self._grid) - 1:
            return [(x, y - 1), (x + 1, y), (x + 1, y - 1)]
        elif x == len(self._grid[0]) - 1 and y == 0:
            return [(x - 1, y), (x, y + 1), (x - 1, y + 1)]
        elif x == len(self._grid[0]) - 1 and y == len(self._grid) - 1:
            return [(x - 1, y), (x, y - 1), (x - 1, y - 1)]
        elif y == 0:
            return [(x - 1, y), (x + 1, y), (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        elif x == 0:
            return [(x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y - 1), (x + 1, y + 1)]
        elif y == len(self._grid) - 1:
            return [(x - 1, y), (x + 1, y), (x, y - 1), (x - 1, y - 1), (x + 1, y - 1)]
        elif x == len(self._grid[0]) - 1:
            return [(x, y - 1), (x, y + 1), (x - 1, y), (x - 1, y - 1), (x - 1, y + 1)]
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]

    def step(self):
        step_flash_counter = 0
        flashers = set()
        for row in self._grid:
            for octopus in row:
                octopus.energy_increase()
                if octopus.attempt_flash():
                    flashers.add(octopus)
                    step_flash_counter += 1

        while len(flashers) != 0:
            flashers_list = list(flashers)
            flashers = set()
            for current_flasher in flashers_list:
                neighbors = [self._grid[neighbor[1]][neighbor[0]] for neighbor
                             in self._get_neighbors(current_flasher.x, current_flasher.y)]
                for octopus in neighbors:
                    octopus.energy_increase()
                    if octopus.attempt_flash():
                        flashers.add(octopus)
                        step_flash_counter += 1

        for row in self._grid:
            for octopus in row:
                octopus.step_complete()
        self.flash_counter += step_flash_counter


def main():
    f = open("day11.txt")
    lines = f.readlines()

    og = OctopusGrid(lines)
    for i in range(100):
        og.step()
    print(og.flash_counter)


if __name__ == '__main__':
    main()
