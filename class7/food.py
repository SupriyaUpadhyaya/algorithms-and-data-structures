class Food:
    weight: int = -1
    amount: int = -1
    
    def __init__(self, qualifier: int) -> None:
        raise NotImplementedError()

    def calories(self) -> int:
        raise NotImplementedError()
    
    def get_weight(self) -> int:
        raise NotImplementedError()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Food):
            return False
        elif self.calories() == other.calories():
            return True
        else:
            return False

    def __lt__(self, other: object) -> int:
        if not isinstance(other, Food):
            return False
        elif self.calories() < other.calories():
            return True
        else:
            return False


class Apples(Food):
    def __init__(self, qualifier: int) -> None:
        self.amount = qualifier

    def calories(self) -> int:
        return (102 * self.amount)
    
    def get_weight(self) -> int:
        return (200 * self.amount)


class Oranges(Food):
    def __init__(self, qualifier: int) -> None:
        self.amount = qualifier

    def calories(self) -> int:
        return (94 * self.amount)
    
    def get_weight(self) -> int:
        return (200 * self.amount)


class CookieDough(Food):
    def __init__(self, qualifier: int) -> None:
        self.weight = qualifier

    def calories(self) -> int:
        return int(2.44 * self.weight)
    
    def get_weight(self) -> int:
        return (self.weight)


class cake(Food):
    def __init__(self, qualifier: int) -> None:
        self.weight = qualifier

    def calories(self) -> int:
        return (5 * self.weight)
    
    def get_weight(self) -> int:
        return (300 * self.weight)


class chocolate(Food):
    def __init__(self, qualifier: int) -> None:
        self.amount = qualifier

    def calories(self) -> int:
        return (17 * self.amount)
    
    def get_weight(self) -> int:
        return (300 * self.amount)


if __name__ == "__main__":
    app1 = Apples(5)
    print(app1.calories())
    app2 = Apples(10)
    print(app2.calories())
    print(app1.calories())
