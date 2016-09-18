from flask import *
from models import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
@app.route("/list", methods=['POST'])
def list_data():
    query = User_story.select()
    return render_template('list.html', user_stories=query)


# Story page, default
@app.route("/story", methods=['GET'])
def story():
    empty_story = User_story(story_title="", content="", acceptance_criteria="", business_value="100",
                             estimation="0.5", status="")
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
    return redirect(url_for('list_data'), code=302)

# Update a story by story_id
@app.route("/story/<story_id>", methods=['POST','GET'])
def update_story(story_id):
    if request.method == 'POST':
        User_story.update(story_title=request.form['story_title'],
                                 content=request.form['content'],
                                 acceptance_criteria=request.form['acceptance_criteria'],
                                 business_value=request.form['business_value'],
                                 estimation=request.form['estimation'],
                                 status=request.form['status']).where(User_story.id == story_id).execute()
        return redirect(url_for('list_data'))
    else:
        user_story = User_story.get(User_story.id == story_id)
        return render_template('form.html', user_story=user_story)



# Delete a story, by story_id
@app.route("/delete/<story_id>/", methods=['GET'])
def delete_story(story_id):
    User_story.delete().where(User_story.id == story_id).execute()
    return redirect(url_for('list_data'))

if __name__ == "__main__":
    app.run(debug=True)
