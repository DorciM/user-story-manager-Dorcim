from flask import *
from models import *

app = Flask(__name__)


# Index page and List page
@app.route("/")
@app.route("/list")
def list_data():
    query = User_story.select()
    return render_template('list.html', user_stories=query, web2='http://127.0.0.1:5000/delete',
                           web='http://127.0.0.1:5000/story')


# Story page, default
@app.route("/story", methods=['GET'])
def story():
    empty_story = User_story(story_title="", content="", acceptance_criteria="", business_value="",
                             estimation="", status="")
    return render_template("form.html", user_story=empty_story)


# Add a new User story, upload it to the database
@app.route("/story", methods=['POST'])
def add_story():
    User_story.create(story_title=request.form['story_title'],
                      content=request.form['content'],
                      acceptance_criteria=request.form['acceptance_criteria'],
                      business_value=request.form['business_value'],
                      estimation=request.form['estimation'],
                      status=request.form['status'])
    return "Database uploaded!"


# Update a story by story_id
@app.route("/story/<story_id>", methods=['POST'])
def update_story(story_id):
    data = User_story.get(User_story.id == story_id)
    q = data.update(story_title=request.form['story_title'],
                    content=request.form['content'],
                    acceptance_criteria=request.form['acceptance_criteria'],
                    business_value=request.form['business_value'],
                    estimation=request.form['estimation'],
                    status=request.form['status'])
    q.execute()
    return "Story updated!"


# View a story, by story_id
@app.route("/story/<story_id>", methods=['GET'])
def show_story(story_id):
    data = User_story.get(User_story.id == story_id)
    return render_template('form.html', user_story=data)


# Delete a story, by story_id
@app.route("/delete/<story_id>", methods=['GET'])
def delete_story(story_id):
    data = User_story.get(User_story.id == story_id)
    data.delete_instance()
    return redirect('http://127.0.0.1:5000/list')

if __name__ == "__main__":
    app.run()
