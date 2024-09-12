def filter_names_by_length(names, length):
    return [name for name in names if len(name) >= length]

names = ["Ana", "Carlos", "Jorge", "Beatriz", "Lucía"]
min_length = int(input("Ingrese una cantidad de caracteres deseada: "))
filtered_names = filter_names_by_length(names, min_length)
print(filtered_names)
