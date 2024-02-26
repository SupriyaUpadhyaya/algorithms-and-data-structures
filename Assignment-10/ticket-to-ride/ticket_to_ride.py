from typing import List


def matrix_multiply(mat_0: List[List[int]], mat_1: List[List[int]]) -> List[List[int]]:
    """Multiplies matrix `mat_0` with `mat_1`."""

    # Check that the matrixes have the right dimensions
    assert all([len(mat_0) == len(mat_0[i]) for i in range(len(mat_0))])
    assert all([len(mat_1) == len(mat_1[i]) for i in range(len(mat_1))])
    assert len(mat_0[0]) == len(mat_1)

    mat_3 = [[0 for _ in range(len(mat_0))] for _ in range(len(mat_1[0]))]

    for i in range(len(mat_3)):
        for j in range(len(mat_3[0])):
            for k in range(len(mat_0[0])):
                mat_3[i][j] += mat_0[i][k] * mat_1[k][j]

    return mat_3


class TicketToRide:
    def __init__(self) -> None:
        self.cities: List[str] = []
        self.adjacency_matrix: List[List[int]] = [[]]
        with open('cities.data') as f:
            next(f)
            data = f.read().splitlines()
        i = 0
        for j in data:
            if j != "":
                self.cities.append(j.split(None, 1)[-1])
            i += 1
        print(self.cities[0])

        with open('connections.data') as connections:
            next(connections)
            connect = connections.read().splitlines()
        print(connect[1])

        for i in range(len(self.cities)):
            temp = []
            for j in range(len(self.cities)):
                temp.append(0)
            self.adjacency_matrix.append

        for item in connect:
            value = item.split(",")
            z = 0
            while z < 3:
                value[z] = value[z].strip()
                z += 1
            temp = []

            y = 0
            print(value)
            while y < len(self.cities):
                x = 0
                while x < len(self.cities):    
                    if (self.cities[x] == value[2] and self.cities[y] == value[1]) or (self.cities[y] == value[2] and self.cities[y] == value[1]):
                        print(str(x) + " " + str(y))
                        self.adjacency_matrix.i[y][x] = int(value[0])
                        print(temp)
                    x += 1
                y += 1
            self.adjacency_matrix.append(temp)
        #print(self.adjacency_matrix)

    def create_city_array(self) -> None:
        raise NotImplementedError()  # TODO: implement

    def city_to_index(self, city: str) -> int:
        raise NotImplementedError()  # TODO: implement

    def index_to_city(self, index: int) -> str:
        raise NotImplementedError()  # TODO: implement

    def create_adjacency_matrix(self) -> None:
        raise NotImplementedError()  # TODO: implement

    def get_connection_length(self, cityA: str, cityB: str) -> int:
        raise NotImplementedError()  # TODO: implement

    def get_connections(self, city: str) -> List[str]:
        raise NotImplementedError()  # TODO: implement

    def get_cycles_count(self, city: str, length: int) -> int:
        raise NotImplementedError()  # TODO: implement

    def get_total_cycles_count(self, length: int) -> int:
        raise NotImplementedError()  # TODO: implement


if __name__ == "__main__":
    ttr = TicketToRide()
