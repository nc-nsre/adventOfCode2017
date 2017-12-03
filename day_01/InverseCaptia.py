

def captia(sequence, step=1):
    step = int(step)
    length = len(sequence)
    result = 0
    for i in range(len(sequence)):
        cur = sequence[i % length]
        prev = sequence[i - step % length]
        if cur == prev:
            result += int(cur)

    return str(result)
