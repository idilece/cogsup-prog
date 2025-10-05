from expyriment import design, control, stimuli

def draw(stims):
    if len(stims) == 1:
        stims[0].present(clear=True, update=True)
    else:
        stims[0].present(clear=True, update=False)
    for stim in stims[1:-1]:
        stim.present(clear=False, update= False)
    stims[-1].present(clear=False, update=True)
    
    
exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

draw([square, fixation])

exp.clock.wait(500)


exp.keyboard.wait()

control.end()
