seq1 = (1, 3, 5, 7, 9)
seq = (1, 1, 1, 1, 1, 1)
def mean (sequence) :
    sum = 0
    for i in sequence:
        sum = sum + i
    mean = sum / len(sequence)
    return mean

meanValue = mean(seq)
print(meanValue)

def variance (sequence, mean) :
    z = 0
    for i in sequence:
        z = z + ((i - mean) ** 2)
    var = z / (len(sequence) - 1)
    return var

varianceValue = variance(seq, meanValue)
print(varianceValue)

print("an".join("foo"))
