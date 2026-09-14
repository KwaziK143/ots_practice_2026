import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)

   
    if state == "DOWN1":
        t.forward(10)

        if y <= -turn:
            state = "RIGHT1"
            t.setheading(0)  # Разворот вправо
            return state, turn

        return state, turn

   
    if state == "RIGHT1":
        t.forward(10)

        if x >= turn:
            state = "UP1"
            t.setheading(90)  # Разворот вверх
            return state, turn

        return state, turn

    
    if state == "UP1":
        t.forward(10)  # Перемещение

        if y >= turn:
            state = "RIGHT2"
            t.setheading(0)  # Разворот вправо
            return state, turn

        return state, turn

  
    if state == "RIGHT2":
        t.forward(10)  # Перемещение

        if x >= 2 * turn:
            state = "DOWN2"
            t.setheading(270)  # Разворот вниз
            return state, turn

        return state, turn

   
    if state == "DOWN2":
        t.forward(10)  # Перемещение

        if y <= -turn:
            state = "RIGHT3"
            t.setheading(0)  # Разворот вправо
            return state, turn

        return state, turn

   
    if state == "RIGHT3":
        t.forward(10)   # Перемещение

        if x >= 3 * turn:
            state = "UP2"
            t.setheading(90)  # Разворот вверх
            return state, turn

        return state, turn

    
    if state == "UP2":
        t.forward(10)  # Перемещение

        if y >= turn:
            state = "RIGHT4"
            t.setheading(0)
            return state, turn

        return state, turn

   
    if state == "RIGHT4":
        t.forward(10)  # Перемещение

        if x >= 4 * turn:
            state = "DOWN3"
            t.setheading(270)  # Разворот вниз
            return state, turn

        return state, turn

    
    if state == "DOWN3":
        t.forward(10)  # Перемещение

        if y <= -turn:
            state = "RIGHT5"
            t.setheading(0))  # Разворот вправо
            return state, turn

        return state, turn

    
    if state == "RIGHT5":
        t.forward(10)  # Перемещение

        if x >= 5 * turn:
            state = "UP3"
            t.setheading(90)   # Разворот вверх
            return state, turn

        return state, turn

  
    if state == "UP3":
        t.forward(10)  # Перемещение

        if y >= turn:
            state = "STOP"
            return state, turn

        return state, turn


    if state == "INIT":
        state = "DOWN1"
        t.setheading(270)  # Разворот вниз
        return state, turn

    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state

    t = turtle.Turtle()
    t.speed(0)

  
    turn = 5

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(
            curr_state, t, turn
        )

    turtle.done()


if __name__ == "__main__":
    draw()
