from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


#get route for questions, story
@app.get("/questions")
def get_questions():

    prompt_list = silly_story.prompts
    print("prompt list", prompt_list)
    return render_template("questions.html", prompts=prompt_list)

@app.get("/story")
def get_story():
    return render_template("story.html", text=silly_story.template)




