criar o venv: python3 -m venv .venv
ativar o venv: source .venv/bin/activate
instalar dependencias via pip: pip install {dependencia}
gerar arquivo requirements.txt com as dependencias do projeto: pip freeze > requirements.txt
instalar dependencias via requirements.txt: pip install -r requirements.txt

rodar projeto: fastapi dev main.py
