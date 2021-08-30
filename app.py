from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'practice12345'
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    title = "New Story"
    prompts = stories.story.prompts
    return render_template('home.html', story_title = title, prompts = prompts)

@app.route('/story')
def story_display():
    title = "New Story"
    prompts = stories.story.prompts
    answers = stories.story.generate(request.args)
    template = stories.story.template
    return render_template('story.html', story_title = title, answers = answers)