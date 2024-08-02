# Parity of a binary word is 1 if the number of 1s in the word is odd else 0.
def parity(x):
    result = 0
    while x:
        result ^= x & 1 # Isolates the LSB (Least Significant Bit) of x and updates the result with the XOR of itself.
        x >>= 1 # Right shift to discard the LSB bit which was just processed.
    return result

print(parity(3))

# Input => 3 => Binary Representation => 11
# Output => 0