from flask import Flask, jsonify, abort
from Learner import getTweets, openStories, sortTexts, createStory, nearestNeighbor, createJoke, Story
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/done')
def done_world():
    abort('404')
    return 'Hello World!'


@app.route('/standupcom/v1.0/makejoke/<string:term>', methods=['GET'])
def make_joke(term):
    tempStory = Story()
    tempStory.text = " "
    sortTexts(getTweets(term), [tempStory])

    stories = []
    counter = 0
    while counter < 25:
        stories.append(createStory(term, 15))
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

    return jsonify({'joke': finalString})

if __name__ == '__main__':
    app.run()
