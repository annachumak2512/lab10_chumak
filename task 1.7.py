def process_grades(grades):
    filtered_grades = filter(lambda g: g >= 60, grades)
    converted_grades = map(lambda g: round((g / 100) * 12), filtered_grades)
    return list(converted_grades)

print(process_grades([45, 85, 90, 67, 33, 78, 92, 100, 55]))


