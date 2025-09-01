from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(user_input):
  user_input = user_input.lower()

  if "Hello" in user_input or "Hi" in user_input:
      return "Hi, how can I help you?"
  elif "budget" in user_input or "saving" in user_input:
    return "A good rule of thumb is to save at least 20% of your income each month"
  elif "invest" in user_input or "stocks" in user_input:
    return "Investing in diversified ETFs is generally safer than picking individual stocks."
  elif "credit card" in user_input:
        return "Pay your credit card balance in full each month to avoid interest."
  elif "loan" in user_input:
        return "Try to pay off high-interest loans first."
  else:
        return "I’m not sure about that. Can you ask something about budgeting, investing, or credit?"

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint for chat
@app.route("/get_response", methods=["POST"])
def respond():
    user_input = request.json.get("message")
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
