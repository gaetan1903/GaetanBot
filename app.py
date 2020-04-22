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

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.french.greetings')
trainer.train('chatterbot.corpus.french.conversations')

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def listen():
    text = request.form.get('text')
    text = chatbot.get_response(text.strip())
    return str(text)



@app.route('/', methods=['GET'])
def test():
    return "Test Reussi Gaetan"


if __name__ == '__main__':
    app.run()

