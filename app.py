from flask import Flask, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(
    "Gaetan Jonathan",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
)

trainer = ListTrainer(chatbot)

trainer.train([
    "Qui est tu?",
    "C'est Gaetan Jonathan"
])

trainer.train('chatterbot.corpus.french.greetings')
trainer.train('chatterbot.corpus.french.conversations')
trainer.train('botprofile')

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def listen():
    text = request.form.get('text')
    #print(text)
    text = chatbot.get_response(text.strip()[1:-1])
    #print(text)
    return str(text)

    #  return str(chatbot.get_response(request.form.get('text')))


@app.route('/', methods=['GET'])
def test():
    return "Test Reussi Gaetan"


if __name__ == '__main__':
    app.run()

