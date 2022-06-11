msecs_start = control.millis()
computer_number = 0
guess_number = 1
button_pressed = False
program_options = ["start","get_input","check_number","end"]
program_state = program_options[0]

led_blank = """
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
"""

led_smile = """
. . . . .
. # . # .
. . . . .
# . . . #
. # # # .
"""

led_higher = """
. . # . .
. # . # .
# . . . #
# . . . #
# . . . #
"""

led_lower = """
# . . . #
# . . . #
# . . . #
. # . # .
. . # . .
"""

led_congratulations = """
. . . . #
. . . . #
. . . # .
# . # . .
. # . . .
"""






def progress_game():
    global program_state
    if program_state == program_options[0]:
        start_game()
    elif program_state == program_options[1]:
        get_input()
    elif program_state == program_options[2]:
        check_number()
    elif program_state == program_options[3]:
        end()


def start_game():
    global program_state
    program_state = program_options[0]
    computer_number = randint(1, 9)
    basic.clear_screen()
    basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
    msecs = control.millis()
    while True:
        msecs_diff = control.millis() - msecs
        if button_pressed or msecs_diff > 1000:
            break

    program_state = program_options[1]
    pass


def get_input():
    global program_state
    basic.clear_screen()
    basic.show_string("guess")
    msecs = control.millis()
    while True:
        basic.show_number(guess_number)
        msecs_diff = control.millis() - msecs
        if msecs_diff > 1000:
            break

    program_state = program_options[2]
    pass


def check_number():
    global program_state
    if guess_number > computer_number:
        basic.show_leds("""
        . . # . .
        . # . . .
        # . . . .
        . # . . .
        . . # . .
        """)
        pause(1000)

    if guess_number < computer_number:
        basic.show_leds("""
        . . # . .
        . . . # .
        . . . . #
        . . . # .
        . . # . .
        """)
        pause(1000)

    if guess_number == computer_number:
        program_state = program_options[3]
    
    pass


def end():
    global program_state
    button_pressed = False
    basic.show_leds("""
    . . . . #
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    """)
    pause(1000)
    program_state = program_options[0]
    pass

def on_button_pressed_a():
    global program_state
    button_pressed = True
    if program_state == program_options[1]:
        guess_number +=1
        if guess_number == 10:
            guess_number = 1
    pass

def on_button_pressed_b():
    global program_state
    button_pressed = True
    if program_state == program_options[1]:
        guess_number -=1
        if guess_number == 0:
                guess_number = 9
    pass


def on_forever():
    progress_game()
    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)

basic.forever(on_forever)