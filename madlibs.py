from random import choice
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    return render_template("compliment.html", person=player)
#     AWESOMENESS = [
#         'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
#         'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

#     compliment = choice(AWESOMENESS)



@app.route('/game', methods=['GET', 'POST'])
def show_game_form():
    if request.args.get("play_game") == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route("/madlib", methods=['GET', 'POST'])
def show_madlib():
    p_person = request.args.get("person_answer")
    p_color = request.args.get("color_answer")
    p_noun = request.args.get("noun_answer")
    p_adjective = request.args.get("adj_answer")
    p_verb = request.args.get("verb_answer")
    p_pet = request.args.get("pet_answer")
    p_adverb = request.args.get("adv_answer")

    AWESOMENESS = ["madlib.html", "madlib2.html", "madlib3.html", "madlib4.html"]

    rand_madlib = choice(AWESOMENESS)


    return render_template(rand_madlib, person=p_person, 
        color=p_color, noun=p_noun , adjective=p_adjective, 
        verb=p_verb, pet=p_pet, adverb=p_adverb)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
