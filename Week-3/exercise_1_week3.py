# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode(True)


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "4 squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

width, height = exp.screen.size
stim_length = width // 10
stim_size = (stim_length, stim_length)

positions = [(-width//2 + stim_length//2,  height//2 - stim_length//2), 
             (width//2 - stim_length//2,  height//2 - stim_length//2),
             (-width//2 + stim_length//2, -height//2 + stim_length//2),
             (width//2 - stim_length//2, -height//2 + stim_length//2)]
        
squares = [stimuli.Rectangle(size =stim_size, position = pos, colour = (255, 0, 0), line_width = 1) for pos in positions]

# Create a 50px-radius circle
#square1 = stimuli.Rectangle(size=(80, 80), colour=(255, 0, 0), line_width=5, position=(-width //2, height//2))
#square2 = stimuli.Rectangle(size=(80, 80), colour=(255, 0, 0), line_width=5, position=(-width //2, -height//2))  
#square3 = stimuli.Rectangle(size=(80, 80), colour=(255, 0, 0), line_width=5, position=(width //2, -height//2))  
#square4 = stimuli.Rectangle(size=(80, 80), colour=(255, 0, 0), line_width=5, position=(width //2, height//2))     

# Start running the experiment
control.start(subject_id=1)

for square in squares:
    square.present(clear=False, update=False)

exp.screen.update()

# Leave it on-screen for 1,000 ms
exp.clock.wait(1000)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()