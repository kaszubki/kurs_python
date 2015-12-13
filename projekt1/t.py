class TuringMachine(object):
    def read(self):
        self.history = []
        start_state = raw_input()
        
        s = raw_input()
        self.end_states = s.split(" ")
        
        self.transitions = {}
        while True:
            s = raw_input()
            if s == "":
                break
            s = s.split(" ")
            s1 = (s[0], s[1])
            s2 = (s[2], s[3], s[4])
            if self.transitions.get(s1) is None:
                self.transitions[s1] = [s2]
            else:
                self.transitions[s1].append(s2)
        
        tape = raw_input()
        position = 0
        while tape[position] == '-':
            position += 1
        
        self.history.append((start_state, position, tape))
        self.time = 0
        return
    
    def step(self):
        state, pos, tape = self.history[-1]
        
        if state in self.end_states:
            print "My work here is done"
            return False
        
        state2, ple, move = self.transitions[(state, tape[pos])][0]
        tape2 = tape[:pos] + ple + tape[pos+1:]
        
        pos2 = pos
        if move == "R":
            pos2 += 1
        elif move == "L":
            pos2 -= 1
        
        if pos2 == -1:
            tape2 = "-" + tape2
            pos2 = 0
            
        if pos2 == len(tape2):
            tape2 = tape2 + "-"
        
        self.history.append((state2, pos2, tape2))
        self.time += 1
        return True
    
    def forward(self):
        if self.time < len(self.history) - 1:
            self.time += 1
            return True
        return self.step()
    
    def backward(self):
        if self.time == 0:
            print "Already at the beginning, can't go back in time"
            return
        self.time -= 1
        return
    
    def show(self):
        print "Tape: {0}".format(self.history[self.time][2])
        print "Position: {0}".format(self.history[self.time][1])
        print "State: {0}".format(self.history[self.time][0])
        if self.history[self.time][0] in self.end_states:
            print "This is a final state"
        return

maszynka = TuringMachine()
maszynka.read()
maszynka.show()

while maszynka.forward():
    maszynka.show()