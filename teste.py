avrg = []
def inputGrades():
    i = 0
    while i < 3:
        grade = int(input(f"Digite a {i + 1}° Nota: "))
        i += 1
        avrg.append(grade)
    Average()

def Average():
    result = (sum(avrg)/3)
    print(result)

inputGrades()