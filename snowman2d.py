class HeightArray:
    """
    Basic array for storing the height of the snowman.
    Each position in the array is the snowmans height at that point on the x axis.
    """
    def __init__(self, indx, args):
        """ Initialize the array. """
        if int(indx/2.0) == indx/2.0:
            indx += 1
        self.indx = indx
        while len(args) > indx:
            args = args[1:-1]
        while len(args) < indx:
            args.append(0.0)
            args.insert(0, 0.0)
        self.args = args

    def update(self):
        """ Makes a new array. """
        n_height = HeightArray(self.indx, [0])
        for i in range(0,self.indx):
            n_height[i] += self.args[i] * 0.8
            if i > 0:
                n_height[i-1] += self.args[i] * 0.1
            if i < self.indx-1:
                n_height[i+1] += self.args[i] * 0.1
        return n_height

    """ Extra functions used for my convenience. ;) """
    def __str__(self):
        ret = " "
        for i in self.args:
            i = str(int(i*10)/10.0)
            ret += i + (5 - len(i)) * " "
        return ret
    def __repr__(self):
        return self.args
    def __setitem__(self, i, assig):
        self.args[i] = assig
    def __getitem__(self, i):
        return self.args[i]

time = 0
data = {time:HeightArray(7, [0,0,0,10,0,0,0])}
height = data[0]

""" Runs the loop 15 times. """
while time < 15:
    time += 1.0
    height = height.update()
    data[time] = height

""" Display the data. """
print "time  | height"
for t in data:
    ts = str(t)
    hs = str(data[t])
    print " "+ts+(" "*(5-len(ts)))+"| "+hs
