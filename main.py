from pip._internal import main as pip
import magic
import json
from datetime import date
from pprint import pprint

##Prova ad importare wikipedia, se non c'è allora installala da pip
try:
    import wikipedia
except ImportError:
    pip(['install', 'wikipedia'])

from googleapiclient.discovery import build
import wikipedia

##Costanti + setting di wikipedia
wikipedia.set_lang('it')
API_key = ""
CSE_id = ""


def search(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=API_key)
    res = service.cse().list(q=search_term, cx=CSE_id, **kwargs).execute()
    return res['items']


def Question():
    return "Qual è la capitale dell'Italia?"

def Answers():
    return ["Roma", "Parigi", "Berlino"]


##Prendi la domanda, somehow
question = Question()

##Togli le robe inutili, lascia i sostantivi e kwords
question_strip = magic.Magic(question)

##Prendi le risposte
answers = Answers()

##Prendi i primi num risultati di Google
results = search(question_strip, num=3)

##Crea set risposte
correct_ans = set()


##Considera ogni risposta disponibile, prendi i risultati di ricerca
##Se trovi le risposte nei risultati di ricerca prob è quella giusta
##I risultati sono dict (JSON) con title, body etc quindi serve element in res.values()
##Aggiungo le risposte in un set
for ans in answers:
    for res in results:
        for tag in res.values():
            if ans in tag:
                correct_ans.add(ans)


##Se il set è di dimensione 1, vuol dire che ha trovato solo una risposta
if len(correct_ans)==1:
    right = list(correct_ans)[0]
else:
    right = "BAD"

print("{0}\n\n{1}\n\nLa risposta è: {2}".format(question, answers, right))



# results = search("Età obama")
#
#
# for result in results:
#     if "wikipedia" in result['title'].lower():
#         print(result['title'])
#         valid.append(wikipedia.search(result['title'].lower().replace("- wikipedia", ""), results=1))
#         break
#
# for title in valid:
#     print(title)
#     print(wikipedia.page(title).content[:300])


