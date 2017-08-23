import numpy as np
import sklearn
import matplotlib
import tweepy
import copy

metaDict = {}
counters = {}
storiesString = []

class Story(object):
    text = ""

def getTweets(term):

    api = tweepy.OAuthHandler("1AP3nNg1X43KEhWM0xCxpxPzS", "rfCjzontc2zBhmrVkzPBl2DrjLdhaaGb9dY8OQGBbFGpMcVJNA")
    api.set_access_token("884147672629874688-WFL3T77gbfYQfvGfD33WsWZTf2fMRxb", "N9U5ERdiDfLodFU2wXjS87QyuULLYcSVVZRwkj6p2eNHv")
    getter = tweepy.API(api)
    print("before results")
    results = getter.search(q=term, count=100)
    print("after results")
    return results

def openStories():
    story = Story()
    alices = Story()
    sherlock = Story()
    twoc = Story()
    grimm = Story()
    empty = Story()
    empty.text = " "

    with open("queenlucia.txt") as stortext:
        story.text = stortext.read()
    with open("alice.txt") as alice:
        alices.text = alice.read()
    with open("sherlock.txt") as sher:
        sherlock.text = sher.read()
    with open("twocities.txt") as twocities:
        twoc.text = twocities.read()
    with open("grimm.txt") as grimmtext:
        grimm.text = grimmtext.read()
    #return [story, alices, sherlock, twoc, grimm]
    return [empty]

def sortTexts(tweets, stories):
    results = []
    #results.append(stories)
    #results.append(tweets)
    for itemer in tweets:
        results.append(itemer)
    for numer in stories:
        results.append(numer)

    count = 0
    print("working")
    #print(results)
    for item in results:
        searchedTerm = ""
        searchedTerm = item.text.lower()

        searcharray = searchedTerm.split(" ")
        storiesString.append(searcharray)
        searcharray.append(" ")

        for temper in searcharray:
            if temper == " ":
                break
            if temper in metaDict:
                if not (temper.__contains__("#") and temper.__contains__("http")):
                     if searcharray[count + 1] in metaDict[temper]:
                         metaDict[temper][searcharray[count + 1]] += 1
                     else:
                         metaDict[temper][searcharray[count + 1]] = 1
                     counters[temper] += 1
            else:
                if not (temper.__contains__("#") and temper.__contains__("http")):
                    metaDict[temper] = {}
                    metaDict[temper][searcharray[count + 1]] = 1
                    counters[temper] = 1
            count += 1
        count = 0
    print("finished getting tweets")




def createStory(starting, length):
    print("Create story")

    #print(storyDict)
    #print(metaDict)
    storyArray = [starting]
    length = length + 0
    i = 0
    while True:
        nextWord = nearestNeighbor(storyArray[i], metaDict)
        metaDict[storyArray[i]][nextWord] = -1
        if nextWord == " ":
            break
        else:
            storyArray.append(nextWord)
            if nextWord.__contains__("."):
                break
        i = i + 1
    #print(storyArray)
    return storyArray


def nearestNeighbor(word, localDict):
    #print(localDict)
    tempDict = localDict[word]

    max = -1
    worded = " "
    #print(type(tempDict))
    #print(tempDict.keys())
    for key in tempDict.keys():
        value = tempDict[key]
        if value > max:
            max = value
            worded = key
    return worded

def createJoke(pastStory):

    #print("paststory")
    #print(pastStory)
    temperStory = []
    for numer in pastStory:
        temperStory.append(numer)
    temperStory.remove(pastStory[0])
    sortedStory = []
    finals = []
    while len(temperStory) != 0:
        print(len(temperStory))
        min = counters[temperStory[0]]
        minKey = temperStory[0]
        for item in temperStory:
            if counters[item] < min:
                min = counters[item]
                minKey = item
        sortedStory.append(minKey)
        temperStory.remove(minKey)

    for temper in sortedStory:
        arr = createStory(temper, 15)
        if len(arr) > 1:
            finals = arr
            break
    print("still there?")
   # print(pastStory)
    #pastStory.append("bloop")
    for iter in finals:
        pastStory.append(iter)
    print("new paststory")
    print(pastStory)
    return pastStory


if __name__ == "__main__":

    sortTexts(getTweets("obama"), openStories())

    stories = []
    counter = 0
    while counter < 25:

        stories.append(createStory("obama", 15))
        counter += 1

    temp = stories[0]
    min = len(stories[0])

    for items in stories:
        if len(items) < min and len(items) > 2:
            temp = items
            min = len(temp)
    print("Joking around")
    print(temp)
    finalJoke = createJoke(temp)

    finalString = ""
    print(finalJoke)
    for strings in finalJoke:
        finalString += strings + " "
    print("All i do is win")
    print(finalString)
