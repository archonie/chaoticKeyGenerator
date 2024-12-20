import numpy as np

def logistic_map(x, r=3.99):
    
    return r * x * (1 - x)

def chaotic_key_generator(seed, length, r=3.99):

    if not (0 < seed < 1):
        raise ValueError("Seed must be in the range (0, 1).")
    
    key = []
    state = seed
    
    for _ in range(length):
        state = logistic_map(state, r)
        # Convert chaotic value to an integer (0-255)
        key.append(int(state * 255))
    
    return key

# Example Usage
seed = 0.1234  # Initial seed for the chaotic map
key_length = 16  # Desired key length
chaotic_key = chaotic_key_generator(seed, key_length)

print("Generated Chaotic Key:", chaotic_key)
