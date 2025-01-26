# python type / dict / associative array / literal object
# * dict = ordered 3.5= keyad collection (collection of key= value pairs)
# formula
# indexed (list) -> homogenous [10, 20, 30], [0.25, 0.50, ...]
# keyed (dict) -> mixt      {"name" : "John", "age": 30 }

todo = {
    # key        :    value
    "2021-01-01" :   "Start a New Happy year! :)",
    "2021-01-02" :   "Learn python basics",
    "2021-01-03" :   "Get a job",
}
todo["2021-01-03"] = " Get an internship"

print(todo)
