current_state = "S"


def processing(symbol, data: dict):
    global current_state, chain
    for smbl, _state in data.items():
        if smbl == symbol:
            current_state = _state
            chain += smbl
            print(current_state, chain)


chain = ""
while True:
    symbol = input()
    print(current_state, end="->")
    match current_state:
        case "S":
            processing(symbol, {"1": "B", "3": "A"})
        case "A":
            processing(symbol, {"2": "A", "4": "Z"})
        case "B":
            processing(symbol, {"1": "Z", "3": "B"})
        case "Z":
            processing(symbol, {"2": "A", "4": "B"})
