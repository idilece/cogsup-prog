from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_BLUE, C_GREEN, K_r, K_b, K_g, K_o
import random
import itertools

""" Constants """

COLORS = ["red", "blue", "green", "orange"]

KEYMAP = {"red": K_r, "blue": K_b, "green": K_g, "orange": K_o}
KEYS = [KEYMAP[c] for c in COLORS]


TRIAL_TYPES = ["match", "mismatch"]

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate the color of the word.
Press O if it is ORANGE, Press R if it is RED.\n
Press B if it is BLUE,   Press G if it is GREEN.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """That was correct!"""
FEEDBACK_INCORRECT = """That was incorrect! """

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def generate_block_trials():
    combos = list(itertools.product(COLORS, COLORS))
    random.shuffle(combos)
    return combos

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    trial_type = "match" if (word == color) else "mismatch"
    correct = (key == KEYMAP[color])
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, int(correct)])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

control.start(subject_id=1)

present_instructions(INSTR_START)

for block_id in range(1, N_BLOCKS + 1):
    block_trials = generate_block_trials()
    for trial_id, (word, color) in enumerate(block_trials, start=1):
        run_trial(block_id, trial_id, None, word, color)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)


control.end()