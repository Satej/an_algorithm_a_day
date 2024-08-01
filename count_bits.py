# Count the number of bits set to 1 in a positive integer
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1 # Performs bitwise AND operation. Checks the LSB (Least significant bit) of x.
        x >>= 1 # Performs a right bitwise shift effectively dividing x by 2 and discarding the LSB.
    return num_bits

num_bits = count_bits(11)
print(num_bits)