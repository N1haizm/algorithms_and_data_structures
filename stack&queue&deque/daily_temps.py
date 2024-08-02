temps = [73,74,75,71,69,72,76,73]
output = []
result = [0] * len(temps)

def dailytemps(temperatures):
    for index, temp in enumerate(temperatures):
        while output and temp > output[-1][1]:
            ix, tem = output.pop()
            result[ix] = index - ix
        output.append([index, temp])

dailytemps(temps)
print(result)

