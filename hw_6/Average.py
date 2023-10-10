class Average:
    def average(lst: list[int | float]) -> float:
        if len(lst):
            return sum(lst) / len(lst)
        return 0.0
        