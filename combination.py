def gen_combination(previous, a, ra):
    if previous != "":
        ra.append(previous)
    for i in range(len(a)):
        gen_combination(previous + str(a[i]), a[i + 1:], ra)


def gen_duplicate_combination(a):
    unique = []
    not_unique = {}
    for element in a:
        if element not in unique:
            unique.append(element)
        else:
            try:
                not_unique[element] += 1
            except KeyError:
                not_unique[element] = 2
    unique_combination = []
    gen_combination("", a, unique_combination)
    duplicate_combination = []
    for index, element in not_unique.items():
        for i in range(1, element + 1):
            tmp = list(unique)
            tmp.remove(index)
            tmp.append(int(str(index)*i))
            gen_combination("", tmp, duplicate_combination)
            for unique_element in unique_combination:
                if unique_element in duplicate_combination:
                    duplicate_combination.remove(unique_element)
    print(unique_combination + duplicate_combination)

ra = []
gen_combination("", [1,1,2], ra)
print(ra)

gen_duplicate_combination([1,1,3,1,2])
