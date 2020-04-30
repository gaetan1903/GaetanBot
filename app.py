from flask import Flask, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(
    "Gaetan Jonathan",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "maximum_similarity_threshold" : 0.8,
            "default_response" : "Vous chercher peut être de l'aide\nTaper: gaetan help"
        } 
    ],
)


trainer0 = ChatterBotCorpusTrainer(chatbot)
trainer1 = ListTrainer(chatbot)

trainer0.train('chatterbot.corpus.french.greetings')
trainer1.train([
    "Gaetan",
    "Vous voulez dire 'gaetan'?, \n Tapez gaetan help pour plus d'info sur la commande",
    "Merci",
    "Je vous en prie"
])
trainer1.train([
    "search",
    "Vous vous êtes trompez? \n  taper gaetan help pour plus d'info",
    "Merci beaucoup",
    "De rien"
])

trainer1.train([
    "Pouvez-vous m’en dire plus au sujet de votre entreprise ?",
    "Eh bien, Ceci est un bot qui va recuperer Music/Video/apk/ et plus pour vous ur le web"
])

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

