#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def verbalise_hour(i):
	if i == 0:
		return "minuit"
	elif i == 1:
		return "une heure"
	elif i == 12:
		return "midi"
	elif i == 21:
		return "vingt et une heures"
	else:
		return "{0} heures".format(str(i)) 

def verbalise_minute(i):
	if i == 0:
		return ""
	elif i == 1:
		return "une"
	elif i == 21:
		return "vingt et une"
	elif i == 31:
		return "trente et une"
	elif i == 41:
		return "quarante et une"
	elif i == 51:
		return "cinquante et une"
	else:
		return "{0}".format(str(i)) 


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()

	slots = intent_message.slots

	print(slots.assistant_name)
	print(len(slots.assistant_name))
	print(intent_message.intent.probability)

	if intent_message.intent.intent_name == 'Joseph:askTime' and len(slots.assistant_name) > 0 and intent_message.intent.probability>0.9:

		sentence = 'Il est actuellement '
		print(intent_message.intent.intent_name)

		now = datetime.now(timezone('Europe/Paris'))

		#sentence += verbalise_hour(now.hour) + " " + verbalise_minute(now.minute)
		print(sentence)

		# hermes.publish_continue_session(intent_message.session_id, sentence, ["Joseph:greetings"])
		hermes.publish_end_session(intent_message.session_id, sentence)

	elif intent_message.intent.intent_name == 'Joseph:greetings':

		hermes.publish_end_session(intent_message.session_id, "De rien!")
		
	elif intent_message.intent.intent_name == 'mathieusayag:AskHello' and len(slots.assistant_name) > 0 and intent_message.intent.probability>0.9:

		sentence = 'Hello you speak english very well !'
		print(intent_message.intent.intent_name)
	
		print(sentence)
	elif intent_message.intent.intent_name == 'mathieusayag:AskBonjour' and len(slots.assistant_name) > 0 and intent_message.intent.probability>0.9:

		sentence = 'Bonjour '
		print(intent_message.intent.intent_name)
		if (now.hour >= 17)
		    sentence = 'A ce moment de la journée il faut dire Bonsoir '
		print(sentence)
	elif intent_message.intent.intent_name == 'mathieusayag:AskBonsoir' and len(slots.assistant_name) > 0 and intent_message.intent.probability>0.9:

		sentence = 'Bonsoir '
		print(intent_message.intent.intent_name)
		if (now.hour <= 17)
		    sentence = 'A ce moment de la journée c\'est plûtot Bonjour '
		print(sentence)

with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
