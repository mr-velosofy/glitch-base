from flask import Flask, request

app = Flask(__name__)
        
@app.route("/")
def home():
    return "Contact <a href='https://discordapp.com/users/311519176655241217/' target='_blank'>@mr.velosofy</a> on discord (will add ReadMe soon)"
