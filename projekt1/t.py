class TuringMachine(object):
    def __init__(self):
        self.historia = []
        
    def read(self):
        stan_s = raw_input()
        
        self.stan_k = raw_input()
        self.stan_k = self.stan_k.split(" ")
        
        self.przejscia = {}
        while True:
            s = raw_input()
            if s == "":
                break
            s = s.split(" ")
            s1 = (s[0], s[1])
            s2 = (s[2], s[3], s[4])
            if self.przejscia.get(s1) is None:
                self.przejscia[s1] = [s2]
            else:
                self.przejscia[s1].append(s2)
        
        tasma = raw_input()
        pozycja = 0
        while tasma[pozycja] == '-':
            pozycja += 1
        
        self.historia.append((stan_s, pozycja, tasma))
        self.czas = 0
        return
    
    def step(self):
        stan, pos, tasma = self.historia[-1]
        
        if stan in self.stan_k:
            print "My work here is done"
            return False
        
        stan2, nast_k, ruch = self.przejscia[(stan, tasma[pos])][0]
        tasma2 = tasma[:pos] + nast_k + tasma[pos+1:]
        
        pos2 = pos
        if ruch == "R":
            pos2 += 1
        elif ruch == "L":
            pos2 -= 1
        
        if pos2 == -1:
            tasma2 = "-" + tasma2
            pos2 = 0
            
        if pos2 == len(tasma2):
            tasma2 = tasma2 + "-"
        
        self.historia.append((stan2, pos2, tasma2))
        self.czas += 1
        return True
    
    def forward(self):
        if self.czas < len(self.historia) - 1:
            self.czas += 1
            return True
        return self.step()
    
    def backward(self):
        if self.czas == 0:
            print "Already at the beginning, can't go back in time"
            return
        self.czas -= 1
        return
    
    def show(self):
        print "Tape: {0}".format(self.historia[self.czas][2])
        print "Position: {0}".format(self.historia[self.czas][1])
        print "State: {0}".format(self.historia[self.czas][0])
        if self.historia[self.czas][0] in self.stan_k:
            print "This is a final state"
        return

maszynka = TuringMachine()
maszynka.read()
maszynka.show()

while maszynka.forward():
    maszynka.show()