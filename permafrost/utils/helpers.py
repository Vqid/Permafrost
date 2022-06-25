import random
import permafrost

def random_color() -> int:
    return random.choice(permafrost.__palette__)