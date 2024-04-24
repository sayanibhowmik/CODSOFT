from flask import Flask, render_template, request

app = Flask(__name__)

def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = simple_chatbot(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
