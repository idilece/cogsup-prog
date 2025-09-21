# launching_function.py
from expyriment import design, control, stimuli

#Function
def launching_function(speed=1.0, contact_point=-50, temporal_gap=0):

    size  = 50     # px
    step  = 5      # px per frame

    # Squares: 50x50
    red   = stimuli.Rectangle((size, size), (255, 0, 0), position=(-400, 0))
    green = stimuli.Rectangle((size, size), (0, 255, 0), position=(0, 0))

    ##Presentation of static version of stimuli for 1 second
    red.present(clear=True, update=False)
    green.present(clear=False, update=True)
    exp.clock.wait(1000)

    # Move the red square until touching the contact point (-50)
    steps = 0
    while red.position[0] < contact_point:
        remaining = contact_point - red.position[0]
        if remaining > step:
            dist = step  
        else:
            dist = remaining
        red.move((dist, 0))

        red.present(clear=True, update=False)
        green.present(clear=False, update=True)
        steps = steps + 1

    #temporal delay before green square moves
    if temporal_gap > 0:
        exp.clock.wait(temporal_gap)

    ##Green square will move 
    for i in range(steps):
        green.move((step * speed, 0))
        red.present(clear=True, update=False)
        green.present(clear=False, update=True)

    # Brief hold at the end of this event
    exp.clock.wait(1000)

#run the 4 events 
exp = design.Experiment(name="Launching function")
control.initialize(exp)
control.start(subject_id=1)

    # 1) Michottean launching 
launching_function(speed = 1.0, contact_point = -50, temporal_gap = 0)

    # 2) Launching with a temporal gap
launching_function(speed = 1.0, contact_point = -50, temporal_gap = 150)

    # 3) Launching with a spatial gap
launching_function(speed = 1.0, contact_point = -100, temporal_gap = 0)

    # 4) Higher speed
launching_function(speed = 3.0, contact_point = -50, temporal_gap = 0)

control.end()