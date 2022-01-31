def solution(args):
    return formatOutput(rangeExtraction(tuple(args)))
    
def rangeExtraction(seq):
    argsSorted = sorted(set(seq))
    high = low = argsSorted[0]
    step = None
    for num in argsSorted[1:]:
        if step == None or num - high == step:
            # Increase range
            step = num - high
            high = num
        elif high - low == step:
            # current range only contains two numbers and should be separated by a ","
            yield low, low, None
            step = num - high
            low = high
            high = num
        else:
            # give the range and start the next
            yield low, high, step
            low = high = num
            step = None
        if high - low == step:
            yield low, low, None
            low = high
            step = None
        yield low, high, step
    
def formatRanges(low, high, step):
    if step is None:
        assert low == high
        return "%s" % (low,)
    else:
        return "%s-%s" % (low, high)

def formatOutput(seq):
    return ",".join(formatRanges(*e) for e in seq)
