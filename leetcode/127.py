# -*- coding: utf-8 -*-

beginWord = 'hit'
endWord = 'cog'

wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

if beginWord not in wordList:
    wordList.append(beginWord)
if endWord not in wordList:
    wordList.append(endWord)

connectMap = {}
for word in wordList:
    connectMap[word] = []
    for targetWord in wordList:
        if targetWord == beginWord:
            continue
        if word == targetWord:
            continue
        diffCount = 0
        for i in range(0, len(word)):
            char = word[i]
            tc   = targetWord[i]
            if char != tc:
                diffCount+=1
            if diffCount > 1:
                break
        if diffCount == 1:  # connect!
            connectMap[word].append(targetWord)

print connectMap

prev = {}
for word in wordList:
    prev[word] = word
dist = {}
for word in wordList:
    dist[word] = len(wordList)*2

dist[beginWord] = 0

nonVisitList = wordList[:]

while len(nonVisitList) > 0:
    min_v = len(wordList)*3
    min_w = nonVisitList[0]
    for word in nonVisitList:
        if dist[word] < min_v:
            min_v = dist[word]
            min_w = word
    word = min_w
    nonVisitList.remove(word)

    for connectedWord in connectMap[word]:
        if dist[word] + 1 < dist[connectedWord]:
            dist[connectedWord] = dist[word] + 1
            prev[connectedWord] = word

    print dist
    
print dist[endWord]

word = endWord
while prev[word] != word:
    print word,'->',prev[word]
    word = prev[word]
