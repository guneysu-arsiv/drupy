

default:
	echo "No action"

all: services actions targeted_actions  relations fields node_types entities drupy

services:
	pyreverse ../services.py -p services -o png 

actions:
	pyreverse ../actions.py -p actions -o png 

targeted_actions:
	pyreverse ../targeted_actions.py -p targeted_actions -o png 

relations:
	pyreverse ../relations.py -p relations -o png 

fields:
	pyreverse ../fields.py -p fields -o png 

node_types:
	pyreverse ../node_types.py -p node_types -o png 

entities:
	pyreverse ../entities.py -p entities -o png 

open:
	xdg-open .