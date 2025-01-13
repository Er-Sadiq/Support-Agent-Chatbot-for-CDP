from flask import Flask, render_template, request
from services import response


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    
    user_message = ""
    bot_response = "Hello! How can I help you today?"

    if request.method == "POST":
        # Get the user input from the form
        user_message = request.form['user_message']
        
        # Generate the bot's response based on the user input
        bot_response = response.responser(user_message)  

        # Print for debugging purposes
        print(f"User Message: {user_message}")
        print(f"Bot Response: {bot_response}")
    
    # Render the HTML template with user_message and bot_response passed in
    return render_template("index.html", user_message=user_message, bot_response=bot_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
