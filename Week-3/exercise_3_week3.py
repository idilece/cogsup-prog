# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE


def kanizsa_square(aspect_ratio, scaling_factor_rectangle, scaling_factor_circle):
    
    control.set_develop_mode(True)
    
    # Create an object of class Experiment
    exp = design.Experiment(name = "Kanizsa Square", background_colour = C_GREY)

    # Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)

    width, height = exp.screen.size

    #lengths of cirecle and square
    rect_height = height * scaling_factor_rectangle
    rect_width =  rect_height * aspect_ratio
    radius_c   =  (rect_height * scaling_factor_circle) / 2

    # Start running the experiment
    control.start(subject_id=1)
    exp.screen.clear()

    positions = []
    colors = []

    for x in (-rect_width, rect_width):
        for y in (-rect_height, rect_height):
            positions.append((x//2, y//2))
            colors.append(C_WHITE if y<0 else C_BLACK)
        
    for i in range(len(positions)):
        position_c = positions[i]
        color = colors[i]
    
        #drawing circle
        circle = stimuli.Circle(radius = int(radius_c), colour = color, position = position_c,)
        circle.present(clear=False, update=False)
    
    rectangle = stimuli.Rectangle(size=(int(rect_width), int(rect_height)),
                              colour=C_GREY, 
                              position=(0,0))

    rectangle.present(clear=False, update=False)
        
    
    exp.screen.update() 

    # Leave it on-screen until a key is pressed
    exp.keyboard.wait()

    # End the current session and quit expyriment
    control.end()
    
kanizsa_square(0.5,0.5,0.5)

