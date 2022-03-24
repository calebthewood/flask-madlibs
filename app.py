from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story,excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


#get route for questions, story
@app.get("/questions")
def get_questions():
    """Generate questions form """

    prompt_list = excited_story.prompts
    print("prompt list", prompt_list)
    return render_template("questions.html", prompts=prompt_list)

@app.get("/story")
def get_story():
    """Generate story from user inputs"""

    prompt_response = dict(request.args)
    text = excited_story.generate(prompt_response)      # could just pass in request.args here

    return render_template("story.html", story=text)
