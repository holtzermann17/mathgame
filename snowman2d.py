# Initial snowman example by Daniel Chiquito

height = 10.0
time = 0.0

data = {time:height}

# This is the function. To be changed.
def update(h,t):
    h -= 3.0/(t+1.0)                
    data[t] = h
    return h

while time < 15:
    time += 1.0
    height = update(height, time)

print "time  | height"
for t in data:
    ts = str(t)
    hs = str(data[t])
    print " "+ts+(" "*(5-len(ts)))+"| "+hs     

# (don't bother decrypting the print line, just for display.)
