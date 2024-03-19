# use mypy to actually word the type annotationS
def upper_everything(elements: list[str])-> list[str]:
    return [element.upper() for element in elements]


loud_list: list[str] = upper_everything(["abir", "abit", "apon", "aditto"])
sample : list [int] = ['a', 2, 'b', 3] # This sould show wrong