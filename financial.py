def get_response(user_input):
  user_input = user_input.lower()

  if "budget" in user_input or "saving" in user_input:
    return "A good rule of thumb is to save at least 20% of your income each month"
  elif "invest" in user_input or "stocks" in user_input:
    return "Investing in diversified ETFs is generally safer than picking individual stocks."
  elif "credit card" in user_input:
        return "Pay your credit card balance in full each month to avoid interest."
  elif "loan" in user_input:
        return "Try to pay off high-interest loans first."
  else:
        return "I’m not sure about that. Can you ask something about budgeting, investing, or credit?"

print("Welcome to FinBot! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Robo Advisor: Goodbye! Stay financially healthy!")
        break
    response = get_response(user_input)
    print(f"Robo Advisor: {response}")