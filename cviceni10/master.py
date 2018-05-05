# Tento soubor nám byl poskytnut pro potřeby testování naší implementace.

import mind
import random
import time
import sys

class master:
    def __init__(self, version):
        """ Initialize master object
        with current version 0-easy,1-normal,2-hard
        """
        if (version==0) :
            self.glob=6
            self.test=4
            self.limit=20 # 8
        elif (version==1):
            self.glob=7
            self.test=5
            self.limit=12
        else:
            self.glob=8
            self.test=6
            self.limit=16

    def generate(self):
        """Prepare random code
        for user guess
        """
        self.orig=[random.randint(0,self.glob-1) for i in range(self.test)]
        print("tajny kod ", self.orig)

    def evaluate(self, g):
        """ Evaluate correctness of guess g
        and return number of black and white points
        """
        error=(len(g)!=self.test)  # if the guess has wrong length
        white = 0  # init black, white points
        black = 0
        mask=[]    # init mask of used positions
        if not error:
            for i in range(self.test):  # count black points and mark used position
               if (int(g[i])==self.orig[i]):
                   black+=1
                   mask.append(1)
               else:
                   mask.append(0)
               if not (int(g[i])>=0 and int(g[i])<self.glob):  #chect the correctness of the guess
                   error=True

            for i in range(self.test):   # count white points
                if (int(g[i])!=self.orig[i]): # not black point can be white
                    for j in range(self.test):
                        if (mask[j]==0 and int(g[i])==self.orig[j]):
                            white+=1
                            mask[j]=1   # mark position as used
                            break
        return not error, black, white  # return detected values


    def run(self, user_mind):
        """ With selected user
        play the game and return
        """
        self.generate()  # generate random hidden code
        user_mind.init(self.glob, self.test)  # init user
        error=True
        self.steps=0 
        for i in range(self.limit):
            self.steps+=1
            g = user_mind.guess();  # read user guess
            ev, black, white = self.evaluate(g)
            print("Guess: ", g, "b", black, "w", white, "ev", ev)
            if ev and black<self.test:  # the guess is correct and not full black points
                user_mind.eval(g,black, white)
            elif black>=self.test:      # the user win
                error=False
                break
            else:
                break                   # error guess, user lost
        return not error                # if user reach limit -> user lost

if __name__=="__main__":
    #run the user mind with random game
    user_mind = mind.mind()
    master = master(int(sys.argv[1]))   # initialize the game
    start = time.time()                 # measure time of game
    if (master.run(user_mind)):         # print result of game
        print("Success:", master.steps)
    else:
        print("Error")
    end =time.time()
    print("Time",end-start)             # print time duration of the game
