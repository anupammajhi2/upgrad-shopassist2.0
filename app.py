from flask import Flask, render_template

app = Flask(__name__)

conversation_bot = []

conversation_bot.append({'bot': "Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. Hi, I am Bot. "})
conversation_bot.append({'user': "Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. Hi, I am USER. "})

@app.route("/")
def default_func():
    global conversation_bot, conversation, top_3_laptops
    return render_template("index.html", conv_bot = conversation_bot)


if __name__ == "__main__":
    app.run(debug=True)