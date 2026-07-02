from intents import chat_data

def chatbot_reply(user_message):

    message = user_message.lower()

    for intent in chat_data.values():

        for keyword in intent["keywords"]:

            if keyword in message:

                return intent["response"]

    return "Sorry, I couldn't understand your question."

