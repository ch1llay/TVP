current_state = "S"
chain = ""
input_string = input()

i = 0
while i < len(input_string):
    symbol = input_string[i]
    if symbol not in "1234":
        print("не подходит")
        exit()
    if current_state == "S":
        c