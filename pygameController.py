import pygame
import config

pygame.init()

# Initialize the joysticks.
pygame.joystick.init()

class struct: pass
inputs = struct()

# -------- Main Program Loop -----------
def getInputs():
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    if joystick_count > 1:
        config.telemetry["controller"] = "Error: more than one controller is connected"
        print(config.telemetry)
        quit()
    elif joystick_count < 1:
        config.telemetry["controller"] = "Error: no controller connected"
        print(config.telemetry)
        quit()
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    try:
        jid = joystick.get_instance_id()
    except AttributeError:
        # get_instance_id() is an SDL2 method
        jid = joystick.get_id()

    # Get the name from the OS for the controller/joystick.
    name = joystick.get_name()
    
    try:
        guid = joystick.get_guid()
    except AttributeError:
        # get_guid() is an SDL2 method
        pass
    #else:
        #textPrint.tprint(screen, "GUID: {}".format(guid))

    # Usually axis run in pairs, up/down for one, and left/right for the other.
    axes = joystick.get_numaxes()
    
    inputs.left_stick_x = round(joystick.get_axis(0), 2)
    inputs.left_stick_y = round(joystick.get_axis(1), 2)
    inputs.left_trigger = round(joystick.get_axis(2), 2)
    inputs.right_stick_x = round(joystick.get_axis(3), 2)
    inputs.right_stick_y = round(joystick.get_axis(4), 2)
    inputs.right_trigger = round(joystick.get_axis(5), 2)

    inputs.buttons = joystick.get_numbuttons()
    
    #print(name)
    
    if name == "Sony Computer Entertainment Wireless Controller":
        inputs.a = joystick.get_button(0)
        inputs.b = joystick.get_button(1)
        inputs.x = joystick.get_button(3)
        inputs.y = joystick.get_button(2)
        inputs.left_bumper = joystick.get_button(4)
        inputs.right_bumper = joystick.get_button(5)
        inputs.view = joystick.get_button(8)
        inputs.menu = joystick.get_button(9)
        inputs.guide = joystick.get_button(10)
        inputs.left_stick_button = joystick.get_button(11)
        inputs.right_stick_button = joystick.get_button(12)
        config.telemetry["controller"] = "PlayStation Controller"
    elif name == "Microsoft X-Box One S pad":
        inputs.a = joystick.get_button(0)
        inputs.b = joystick.get_button(1)
        inputs.x = joystick.get_button(2)
        inputs.y = joystick.get_button(3)
        inputs.left_bumper = joystick.get_button(4)
        inputs.right_bumper = joystick.get_button(5)
        inputs.view = joystick.get_button(6)
        inputs.menu = joystick.get_button(7)
        inputs.guide = joystick.get_button(8)
        inputs.right_stick_button = joystick.get_button(9)
        inputs.left_stick_button = joystick.get_button(10)
        config.telemetry["controller"] = "Xbox Controller"
    else:
        config.telemetry["controller"] = "Unknown Controller"
    
    # the below line of code is temporary
    inputs.test = joystick

    hats = joystick.get_numhats()
    
    inputs.dpad_left = 0
    inputs.dpad_right = 0
    inputs.dpad_down = 0
    inputs.dpad_up = 0
    
    # Hat position. All or nothing for direction, not a float like get_axis(). Position is a tuple of int values (x, y).
    inputs.dpad = joystick.get_hat(0)
    
    # Split the single dpad touple into 4 variables representing each button on the dpad
    if inputs.dpad[0] == -1:
        inputs.dpad_left = 1
    elif inputs.dpad[0] == 1:
        inputs.dpad_right = 1
    elif inputs.dpad[1] == -1:
        inputs.dpad_down = 1
    elif inputs.dpad[1] == 1:
        inputs.dpad_up = 1
