# Clicker Box Starting Pos
POSX = 310
POSY = 80
# The amount the score increases initially
STEP = 1
# The amount the step increases each upgrade
STEP_INCREASE = 1
# The amount upgrading the step costs
def cost(step):
    return round((step/0.4)*(step/0.4))
# The initial size of the click button
WIDTH = 100
HEIGHT = 100
# The minimum size of the click button
MIN = 10
# The amount the width and height decrease by each time
DECREASE = 3