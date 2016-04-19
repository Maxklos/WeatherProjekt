dnames = []

def installData(n =[],s):
    dnames = n
    #check if all names are valid
    s.send(str(dnames))

def sendData(s,t, **kwargs):
    #print kwargs
    #print '--------------------------'
    s.send("time: {}".format(t))
    for i in dnames:
        s.send("{}:{}".format(i,kwargs[i]))

    
