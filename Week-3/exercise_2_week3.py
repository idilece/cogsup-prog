# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_BLACK, C_WHITE

control.set_develop_mode(True)


# Create an object of class Experiment
exp = design.Experiment(name = "Kanizsa Square", background_colour = C_GREY)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

width, height = exp.screen.size

#lengths of cirecle and square
length = width // 4
radius_c = width // 20

# Start running the experiment
control.start(subject_id=1)
exp.screen.clear()

positions = []
colors = []

for x in (-length, length):
    for y in (-length, length):
        positions.append((x//2, y//2))
        colors.append(C_WHITE if y<0 else C_BLACK)
        
for i in range(len(positions)):
    position_c = positions[i]
    color = colors[i]
    
    #drawing circle
    circle = stimuli.Circle(radius = radius_c, colour = color, position = position_c,)
    circle.present(clear=False, update=False)
    
square = stimuli.Rectangle( size = (length,length), colour = C_GREY, position = (0,0))
square.present(clear=False, update=False)
        
    
exp.screen.update() 

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
