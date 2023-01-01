import random


class University:
    def __init__(self, name: str, founding_year: int, country: str) -> None:
        # TODO: Add the missing properties
        self.name = name
        self.founding_year = founding_year
        self.country = country

    def __repr__(self) -> str:
        return repr((self.name, self.founding_year, self.country))


if __name__ == "__main__":
    tmp_list = list(range(10))
    random.shuffle(tmp_list)
    # TODO: Get familiar with pythons `sort` and `sorted`. Play around a bit
    # with list `tmp_list` and print the results.

    print(tmp_list)
    print(sorted(tmp_list))
    print(tmp_list)
    print(tmp_list.sort())
    print(tmp_list)

    # Stores universities in the format (name, founding year, country)
    universities = [
        ("Otto-von-Guericke-Universität Magdeburg", 1993, "Germany"),
        ("Harvard University", 1636, "USA"),
        ("Technische Universität München", 1868, "Germany"),
        ("RWTH Aachen", 1870, "Germany")
    ]

    # TODO: Sort universities by age
    universities_list_sorted_by_age = sorted(universities, key=lambda uni: uni[1])
    print(universities_list_sorted_by_age)

    # TODO: Sort universities by name
    universities_list_sorted_by_name = sorted(universities, key=lambda uni: uni[0])
    print(universities_list_sorted_by_name)

    # Stores the universities as `University` objects
    university_objects = [University(name=u[0], founding_year=u[1], country=u[2]) for u in universities]
    print(university_objects)

    # TODO: Sort university_objects by age
    university_objects_sorted_by_age = sorted(university_objects, key=lambda uni: uni.founding_year)
    print(university_objects_sorted_by_age)

    # TODO: Sort university_objects by name
    university_objects_sorted_by_age = sorted(university_objects, key=lambda uni: uni.name)
    print(university_objects_sorted_by_age)

    print(university_objects)
