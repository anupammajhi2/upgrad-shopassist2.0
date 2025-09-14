from flask import Flask, redirect, url_for, render_template, request
from functions import initialize_conversation, get_chat_completions, moderation_check, intent_confirmation_layer, dictionary_present, compare_laptops_with_user, recommendation_validation, initialize_conv_reco, get_chat_completions_func_calling
import openai

app = Flask(__name__)

openai.api_key = open('OPENAI_API_Key.txt', 'r').read().strip()

conversation_bot = []

conversation = initialize_conversation()
introduction = get_chat_completions(conversation)
conversation_bot.append({'bot': introduction})

top_3_laptops = None

@app.route("/")
def default_func():
    global conversation_bot, conversation, top_3_laptops
    return render_template("index.html", conv_bot = conversation_bot)

@app.route("/end_conversation", methods = ['POST', 'GET'])
def end_conversation():
    global conversation_bot, conversation, top_3_laptops
    conversation_bot = []
    conversation = initialize_conversation()
    introduction = get_chat_completions(conversation)
    conversation_bot.append({'bot': introduction})
    top_3_laptops = None
    return redirect(url_for('default_func'))

@app.route("/conversation", methods=['POST'])
def conversation_route():
    global conversation_bot, conversation, top_3_laptops, conversation_reco
    user_input = request.form["user_input_message"]
    conversation_bot.append({'user': user_input})
    prompt = 'Remember that you are a intelligent laptop shopping assistant. You should help and answer only with the queries related to laptops. If the queries are not related to laptops, just say something like you can help only with queries related to laptops etc.'
    moderation = moderation_check(user_input)
    if moderation == 'Flagged':
        conversation_bot.append({'bot': "Sorry, this message has been flagged. Please restart your conversation."})
        return redirect(url_for('default_func') + '?flagged=true')

    if top_3_laptops is None:
        conversation.append({"role": "user", "content": user_input + prompt})

        response_assistant = get_chat_completions(conversation)
        moderation = moderation_check(response_assistant)

        if moderation == 'Flagged':
            conversation_bot.append({'bot': "Sorry, this message has been flagged. Please restart your conversation."})
            return redirect(url_for('default_func') + '?flagged=true')

        confirmation = intent_confirmation_layer(response_assistant)

        print("Intent Confirmation Yes/No:",confirmation.get('result'))

        if "No" in confirmation.get('result'):
            conversation.append({"role": "assistant", "content": str(response_assistant)})
            conversation_bot.append({'bot': response_assistant})
        else:
            response = dictionary_present(response_assistant)
            result = get_chat_completions_func_calling(response, True)
            # conversation_bot.append({'bot': "Thank you for providing all the information. Kindly wait, while I fetch the products: \n"})

            top_3_laptops = compare_laptops_with_user(result)

            print("top 3 laptops are", top_3_laptops)

            validated_reco = recommendation_validation(top_3_laptops)
            if len(validated_reco) == 0:
                conversation_bot.append({'bot': "Sorry, we do not have laptops that match your requirements."})

            conversation_reco = initialize_conv_reco(validated_reco)
            conversation_reco.append({"role": "user", "content": "This is my user profile" + str(validated_reco)})
            recommendation = get_chat_completions(conversation_reco)

            moderation = moderation_check(recommendation)
            if moderation == 'Flagged':
                conversation_bot.append({'bot': "Sorry, this message has been flagged. Please restart your conversation."})
                return redirect(url_for('default_func') + '?flagged=true')

            conversation_reco.append({"role": "assistant", "content": recommendation})
            conversation_bot.append({'bot': recommendation})

    else:
        conversation_reco.append({"role": "user", "content": user_input})

        response_asst_reco = get_chat_completions(conversation_reco)

        moderation = moderation_check(response_asst_reco)
        if moderation == 'Flagged':
            print("Sorry, this message has been flagged. Please restart your conversation.")
            return redirect(url_for('default_func') + '?flagged=true')

        conversation.append({"role": "assistant", "content": response_asst_reco})
        conversation_bot.append({'bot': response_asst_reco})

    return redirect(url_for('default_func'))

if __name__ == "__main__":
    app.run(debug=True)