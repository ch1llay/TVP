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
run = True

for i in range(len(input_string)):
    symbol = input_string[i]
    print(chain)
    if current_state == "S":
        run = processing(symbol, {"1": "B", "3": "A"})
    elif current_state == "A":
        run = processing(symbol, {"2": "A", "4": "Z"})
    elif current_state == "B":
        run = processing(symbol, {"1": "Z", "3": "B"})
    elif current_state == "Z":
        run = processing(symbol, {"2": "A", "4": "B"})
    if not run:
        print("не подходит")
        exit(0)

print("подходит")

