# -*- coding: utf-8 -*-
import random

#from lecture2, finding mismatches of two pattern
def hammingDistance(st1,st2):
    if(len(st1) != len(st2)):
        raise Exception("Strings should be equal length")
    mismatch = 0
    for i in range(len(st1)):
        if(st1[i] != st2[i]):
            mismatch += 1
    return mismatch

def bruteForceMotiffFinding(text,kmer,maxMismatch,minOccur = 3):
    """
    pattern dict. Key is pattern, value is an array which its first value is amount of time its occurs.
    other values its appearances.
    """
    patterns = {}
    for i in range(len(text)-kmer):
        pattern = text[i:i+kmer]
        isExist = False
        for key in patterns.keys():
            if(hammingDistance(pattern,key) <= maxMismatch):
                isExist = True
                patterns[key][0] += 1
                patterns[key].append(pattern)
        if(not isExist):
            patterns[pattern] = [1]
            patterns[pattern].append(pattern)
    
    for key, arr in patterns.copy().items():
        if(arr[0] < minOccur):
            patterns.pop(key)
            
    return patterns


def getConsensus(motifsList):
    consensusMotif = ""
    for i in range(len(motifsList[0])):
        base = {"a":0,"t":0,"g":0,"c":0}
        for motif in motifsList:
            base[motif[i].lower()] += 1
        maxBase = ""
        __dumbVal = -1
        for key,val in base.items():
            if(val > __dumbVal):
                __dumbVal = val
                maxBase = key
        consensusMotif += maxBase
    
    motifsScore = 0
    for i in range(len(motifsList[0])):
        for motif in motifsList:
            if(motif[i] != consensusMotif[i]):
                motifsScore += 1
        
        
    return consensusMotif,motifsScore

def createProfile(motifs):
    #possibilities array
    poss = {"a":[],"t":[],"g":[],"c":[]}
    for i in range(len(motifs[0])):
        base = {"a":0,"t":0,"g":0,"c":0}
        for motif in motifs:
            base[motif[i].lower()] += 1
        for base,amount in base.items():
            poss[base].append(amount/len(motifs))
    return poss

def mostProbableFinder(sequence,profile):
    bestMotif = 0
    bestProb = 0
    for i in range(len(sequence)-len(profile)):
        motif = sequence[i:i+len(profile["a"])]
        _prob = 1
        for base in range(len(motif)):
            _prob *= profile[motif[base]][base]
        if(_prob>bestProb):
            bestMotif = motif
            bestProb = _prob
        print("--",_prob,"--")
    return bestMotif

class GibbsSampler:
    def __init__(self,Dna,k,t,N):
        """
        Parameters:
            DNA -> An array of sequences that have equal length.
            k -> kmer
            t -> would be used to choose random integer
            N -> times for try to find most accurate motiff
        """
        self.originalDna = Dna
        self.K = k
        self.T = t
        self.N = N

        self.__ignoreSequence()
        self.__findRandomMotiffs()
        
        print(self.dnaWithBestMotiffs)


        self.__processMatrix()
        self.__searchIgnoredSequence()
    
        print(self.dnaWithBestMotiffs)
        
    def __findRandomMotiffs(self):
        self.bestMotiffs = []
        for i in self.originalDna:
            randomPosition = random.randint(0,len(self.originalDna[0])-self.K)
#            print(randomPosition,end= "--")
            self.bestMotiffs.append(i[randomPosition:randomPosition+self.K])
        self.dnaWithBestMotiffs = list(zip(self.originalDna,self.bestMotiffs))
#        print(self.dnaWithBestMotiffs)
        
    def __ignoreSequence(self):
        sequenceNumber = random.randint(0,len(self.originalDna)-1)
        self.__ignoredSequence = self.originalDna[sequenceNumber]
        self.Dna = []
        for i in self.originalDna:
            if(i != self.__ignoredSequence):
                self.Dna.append(i)
        
        
    def __processMatrix(self):
        poss = {"a":[],"t":[],"g":[],"c":[]}
        for i in range(self.K):
            base = {"a":0,"t":0,"g":0,"c":0}
            for motif in self.bestMotiffs:
                base[motif[i].lower()] += 1
            for base,amount in base.items():
                poss[base].append(round((amount+1)/(len(self.bestMotiffs)+4),3))
        
        self.__processedProfile = poss
    
    def __searchIgnoredSequence(self):
        seq = self.__ignoredSequence
        bestMotiff = [0,""] #first is probability and second is motiff
        for i in range(len(self.__ignoredSequence)-self.K+1):
            motiff = seq[i:i+self.K]
#            print("motiff:",motiff,end =":")
            prob = 1
            for idx in range(len(motiff)):
                prob *= self.__processedProfile[motiff[idx]][idx]
            
            print(bestMotiff,"->",motiff,"->",prob)
            if(bestMotiff[0] < prob):
                bestMotiff[0] = prob
                bestMotiff[1] = motiff
                
        
        for elements in range(len(self.dnaWithBestMotiffs)):
            if(self.dnaWithBestMotiffs[elements][0] == self.__ignoredSequence):
#                if(self.dnaWithBestMotiffs[elements][1] != bestMotiff[1]):
#                    print("oldu--------------------------",self.dnaWithBestMotiffs[elements][1],bestMotiff[1])
                self.dnaWithBestMotiffs[elements] = (self.__ignoredSequence,bestMotiff[1])
        
        








































