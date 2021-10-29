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
    if symbol not in "1234":
        print("не подходит, так как введен недопустимый символ")
        exit(0)
    if current_state == "S":
        run = processing(symbol, {"1": "B", "3": "A"})
    elif current_state == "A":
        run = processing(symbol, {"2": "A", "4": "Z"})
    elif current_state == "B":
        run = processing(symbol, {"1": "Z", "3": "B"})
    elif current_state == "Z":
        run = processing(symbol, {"2": "A", "4": "B"})
        global_complete = True
    if not run:
        print("не подходит, так как нет перехода")
        exit(0)
if not global_complete:
    print("не подходит, так как не достигнуто конечное состояние")
    exit(0)

print("подходит")

