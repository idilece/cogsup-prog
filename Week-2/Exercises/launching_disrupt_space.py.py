from expyriment import design, control, stimuli

size = 50
step = 5              
contact_point = -100 #After 100 pixels, the causality is disrupted. 

# Create an object of class Experiment
exp = design.Experiment(name="Launching")
control.initialize(exp)

# Squares: 50x50
red   = stimuli.Rectangle((size, size), (255, 0, 0), position=(-400, 0))
green = stimuli.Rectangle((size, size), (0, 255, 0), position=(0, 0))

# Start experiment
control.start(subject_id=1)

#Presentation of static version of stimuli for 1 second
red.present(clear=True, update=False)
green.present(clear=False, update=True)
exp.clock.wait(1000)

# Move the red square until touching the contact point (-50)
steps = 0
while red.position[0] < contact_point:
    remaining = contact_point - red.position[0]  # how many pixels from contact point
    if remaining > step:
        dist = step
    else:
        dist = remaining

    # Move red towards green, to the right
    red.move((dist, 0))
    # Redraw both squares
    red.present(clear=True, update=False)
    green.present(clear=False, update=True)
    steps = steps + 1  # how many frames the red moved

#Green square will move with the same spped and duration (the same step number)
for i in range(steps):
    green.move((step, 0))
    red.present(clear=True, update=False)
    green.present(clear=False, update=True)

#Last presentation for 1 second
exp.clock.wait(1000)
control.end()
