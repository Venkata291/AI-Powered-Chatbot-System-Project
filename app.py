from flask import Flask, render_template, request, session
from chatbot import chatbot_reply

app = Flask(__name__)
app.secret_key = "SaiAIChatbot123"

@app.route("/", methods=["GET", "POST"])
def home():

    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":

        message = request.form["message"]
        reply = chatbot_reply(message)

        history = session["chat_history"]
        history.append({
            "user": message,
            "bot": reply
        })

        session["chat_history"] = history

    return render_template(
        "index.html",
        history=session["chat_history"]
    )


@app.route("/clear")
def clear():
    session.clear()
    return render_template("index.html", history=[])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

