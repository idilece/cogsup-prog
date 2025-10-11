from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_1, K_2

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)
exp.add_data_variable_names(["eye","key","radius","x_coord","y_coord"])

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

key_labels = {
    K_LEFT:  "left",
    K_RIGHT: "right",
    K_UP:    "up",
    K_DOWN:  "down",
    K_1:     "1",
    K_2:     "2",
    K_SPACE: "space",
}

""" Experiment """
def run_trial(side):
    if side == "left":
        which_eye = "Cover your left eye."
        fixation_pos = [300, 0]  
    elif side == "right":
        which_eye = "Cover your right eye."
        fixation_pos = [-300, 0]
    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_pos)
    fixation.preload()

    # --- Instruction screen updates dynamically ---
    instruction = stimuli.TextScreen(
        "Instructions",
        f"{which_eye}\n"
        "Fixate the + sign.\n\n"
        "Use arrow keys (<-, ->) to move the circle.\n"
        "Press '1' to make it smaller, '2' to make it larger.\n\n"
        "When the circle disappears for you, press space\n\n"
        "Press space to start."
    )
    instruction.present()
    exp.keyboard.wait(keys=[K_SPACE])
    
    instruction.present()
    exp.keyboard.wait(keys=[K_SPACE])

    radius = 75
    pos = [0, 0]
    circle = make_circle(radius, pos)

    while True:
        fixation.present(True, False)
        circle.present(False, True)

        key = exp.keyboard.check()
        
        # --- Sadece tuşa basıldığında log yaz ---
        if key:
            exp.data.add([side, key_labels.get(key, str(key)), radius, pos[0], pos[1]])
        
        if key == K_SPACE:
            exp.data.add([side, radius, pos[0], pos[1]])
            break
        
        if key:
            #Position
            if key == K_LEFT:
                pos[0] -= 10
            elif key == K_RIGHT:
                pos[0] += 10
            elif key == K_UP:
                pos[1] += 10
            elif key == K_DOWN:
                pos[1] -= 10

            #Size
            elif key == K_1:
                radius = max(5, radius - 5)
            elif key == K_2:
                radius += 5

            #Update circle
            circle = make_circle(radius, pos)

        if key not in [K_LEFT, K_RIGHT, K_UP, K_DOWN, K_1, K_2, None]:
            break
        
        if key == K_SPACE:
            exp.data.add([side, radius, pos[0], pos[1]])
            break

control.start(subject_id=1)

run_trial("left")
run_trial("right")

control.end()