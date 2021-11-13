def processing(symbol, data: dict) -> bool:
    global current_state, chain
    print(current_state, end="->")
    is_complete = False
    for smbl, _state in data.items():
        if smbl == symbol:
            is_complete = True
            current_state = _state
            chain += smbl
            print(current_state, chain)
    if not is_complete:
        return False
    else:
        return True


current_state = "S"
chain = ""
input_string = input()
if len(input_string) == 0:
    print("введена пустая строка")
    exit(0)
run = True
global_complete = False
for i in range(len(input_string)):
    symbol = input_string[i]
    if symbol not in "56":
        print("не подходит, так как введен недопустимый символ")
        exit(0)
    if current_state == "S":
        run = processing(symbol, {"5": "A"})
    elif current_state == "A":
        run = processing(symbol, {"5":"B"})
    elif current_state == "B":
        run = processing(symbol, {"6":"C"})
    elif current_state == "C":
        run = processing(symbol, {"6":"GD"})
        global_complete = True
    elif current_state == "GD":
        run = processing(symbol, {"5":"MF"})
        global_complete = False
    elif current_state == "MF":
        run = processing(symbol, {"6":"K", "5":"E"})
    elif current_state == "K":
        run = processing(symbol, {"5":"C"})
    elif current_state == "E":
        run = processing(symbol, {"6":"E"})
    if not run:
        print("не подходит, так как нет перехода")
        exit(0)
if not global_complete:
    print("не подходит, так как не достигнуто конечное состояние")
    exit(0)

print("подходит")

