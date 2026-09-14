import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "INIT":

        if True:
            state = "DOWN"
            t.setheading(270)  # Разворот вниз
            return state, turn
        return state, turn
    if state == "DOWN":
        t.forward(10)  # Перемещение

        if y <= -5:
            state = "RIGHT_DOWN"
            t.setheading(0)  # Разворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_DOWN":
        t.forward(10)  # Перемещение

        if x >= turn:
            state = "UP"
            turn = turn + 1  # Увеличение номера витка
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn
    if state == "UP":
        t.forward(10)  # Перемещение

        if y >= 5:
            state = "RIGHT_UP"
            t.setheading(0)  # Разворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT_UP":
        t.forward(10)  # Перемещение

        if x >= turn:
            state = "CHECK"
            turn = turn + 1  # Увеличение номера витка
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn
    if state == "CHECK":

        if turn <= 10:
            state = "DOWN"
            t.setheading(270)  # Разворот вниз
            return state, turn
        if turn > 10:
            state = "STOP"
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()
