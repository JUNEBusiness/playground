"""Dictionaries provide a much roburst usage and organisation of data and retrieval of data"""

# fruit_catalog = {
#     "round fruits":  ["orange","star apple"],
#     "other_shapes" : ["banana", "pineapple"]
# }


# print(fruit_catalog["other_shapes"])

students = {
    "Aloba" : {
        "height" : "6 ft 9'",
        "complexion": "Caramel"
    },

    "Precious": {
        "height" : "5 t 9'",
        "complexion": "Caramel"
    },

    "Elot": {
        "height" : "6 ft 2'",
        "complexion": "Fair"
    },
}

# print(students["Precious"]["height"])

"""we can also use loops with dictionaries"""

for student in students:
    print(students[student]["height"])


