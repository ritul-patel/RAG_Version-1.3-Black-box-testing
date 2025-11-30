# PERFORMANCE_TEST: intentionally inefficient
def compute(n):
    result = []
    for i in range(n):
        for j in range(n):
            # expensive repeated work inside loops
            result.append(i * j)
    return result

def repeated_io(n):
    # calling expensive operation inside loop
    out = []
    for i in range(n):
        open("temp.txt","a").write(str(i)+"\n")
    return out
