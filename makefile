build:
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	deactivate
	rm whatsapp-bot-venv

venv:
	python3 -m venv whatsapp-bot-venv

venv-mac-linux: venv
	source whatsapp-bot-venv/bin/activate

venv windows: venv
	whatsapp-bot-venvScripts\activate

start: build
	python src/bot.py