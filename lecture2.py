# -*- coding: utf-8 -*-

def patternCount(pattern,text):
    count = 0
    k = len(pattern)
    n = len(text)
    
    for i in range(n-k):
        if(text[i:i+k] == pattern):
            count += 1
    return count
    
def findAllKmer(k,text):
    counts = dict()
    
    for i in range(len(text)-k):
        if(text[i:i+k] in counts.keys()):
            counts[text[i:i+k]] += 1
        else:
            counts[text[i:i+k]] = 1
    return counts

def getComplementaryReverse(text):
    return "".join(["a" if i == "t" else "t" if i == "a" else "g" if i == "c" else "c" for i in text])[::-1]
    
def findClumps(text, k, L , t):
    patterns = []
    n = len(text)
    for i in range(n-L):
        window = text[i:i+L]
        freqMap = findAllKmer(k,window)
        for key,val in freqMap.copy().items():
            if(val >= t and key not in patterns):
                patterns.append(key)
    return patterns

def hammingDistance(st1 : str,st2 : str):
    if(len(st1) != len(st2)):
        raise Exception("Strings should be equal length")
    mismatch = 0
    for i in range(len(st1)):
        if(st1[i] != st2[i]):
            mismatch += 1
    return mismatch

        
def ApproximatePatternCount(Text, Pattern : str, d = None):
    if(d == None):
        d = len(Pattern)
    count = 0
    for i in range(len(Text) - len(Pattern)):
        _pattern = Text[i:i+len(Pattern)]
        try:
            if(hammingDistance(Pattern,_pattern) <= d):
                count += 1
        except:
            pass
    return count
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        