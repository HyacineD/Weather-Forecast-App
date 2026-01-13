Application Météo pour Alger
Une petite appli qui te donne la météo à Alger avec un historique des données et des prédictions.
Ce qu'il te faut avant de commencer
Tu vas avoir besoin d'installer quelques trucs sur ton ordi :

Python 3.8 ou plus récent – Tu peux le télécharger sur python.org
Node.js 14 ou plus – Disponible sur nodejs.org
Git – Pour récupérer le code depuis GitHub

Comment installer tout ça
Récupérer le projet
Ouvre ton terminal et tape :
bashgit clone https://github.com/HyacineD/Weather-Forecast-App.git
cd Weather-Forecast-App
Créer un environnement virtuel Python
C'est une bonne pratique pour éviter les conflits entre projets.
Si tu es sur Windows :
bashpython -m venv env
env\Scripts\activate
Si tu es sur macOS ou Linux :
bashpython3 -m venv env
source env/bin/activate

Note importante : Tu devras réactiver cet environnement à chaque fois que tu ouvres un nouveau terminal pour bosser sur le projet.

Installer les dépendances Python
Une fois l'environnement activé :
bashpip install -r requirements.txt
Installer les dépendances Node.js
Si t'en as besoin (pour le frontend) :
bashnpm install
Lancer l'application
Dans ton terminal :
bashpython __init__.py
Puis ouvre un autre terminal, va dans le dossier m_app et lance :
bashcd m_app
npm run dev
Normalement, l'appli devrait tourner sur http://localhost:5000
Organisation des fichiers
Voici comment le projet est organisé :
Weather-Forecast-App/
├── .env                 # Tes clés API (à ne jamais partager !)
├── .env.example         # Un modèle pour créer ton .env
├── .gitignore          # Les fichiers que Git ignore
├── config.py           # La config de l'appli
├── api.py              # Tout ce qui touche aux appels API
├── run.py              # Le fichier principal pour démarrer
├── dataframe.py        # Manipulation des données
├── prediction.py       # Le modèle de prédiction météo
├── requirements.txt    # Les bibliothèques Python nécessaires
├── package.json        # Les dépendances JavaScript
├── my_app/             # Le frontend de l'appli
└── data/               # Les données météo stockées
Commandes pratiques
Voici quelques commandes qui peuvent te servir :
bash# Activer l'environnement virtuel
source env/bin/activate          # sur macOS/Linux
env\Scripts\activate             # sur Windows

# Désactiver l'environnement
deactivate

# Réinstaller les dépendances si besoin
pip install -r requirements.txt

# Lancer l'application
python run.py

# Vérifier que la config est bonne
python config.py
Problèmes courants et solutions
"FORECAST_API_KEY n'est pas définie"
Tu n'as pas créé ton fichier .env. Fais comme ça :
bashcp .env.example .env
Ensuite, ouvre le fichier .env et ajoute tes clés API.
"No module named 'dotenv'"
Les dépendances ne sont pas installées. Lance :
bashpip install -r requirements.txt
"python: command not found"
Essaie avec python3 à la place :
bashpython3 run.py
L'application refuse de démarrer
Vérifie ces points dans l'ordre :

L'environnement virtuel est bien activé ?
Le fichier .env existe et contient tes clés API ?
Toutes les dépendances sont installées ?
Le port 5000 n'est pas déjà utilisé par une autre appli ?

"Port 5000 already in use"
Change le port dans ton fichier .env :
envPORT=8000
Tu veux contribuer ?
C'est cool ! Voici comment faire :

Fais un fork du projet
Crée une branche pour ta fonctionnalité (git checkout -b ma-super-feature)
Fais tes modifications et commit (git commit -m 'Ajout de ma super feature')
Push sur ta branche (git push origin ma-super-feature)
Ouvre une Pull Request

Technologies utilisées

Backend : Python avec Flask
Analyse de données : Pandas, NumPy, Scikit-learn
API météo : WeatherAPI.com
Frontend : JavaScript classique avec HTML/CSS
Outils : python-dotenv, requests

Licence
Projet sous licence MIT – tu peux faire ce que tu veux avec, ou presque.
Auteur
Créé par HyacineD – @HyacineD sur GitHub
Remerciements
Merci à WeatherAPI.com pour leur API gratuite et à toute la communauté open source.

Version rapide (si tu connais déjà tout ça)
bashgit clone https://github.com/HyacineD/Weather-Forecast-App.git
cd Weather-Forecast-App
python -m venv env
source env/bin/activate              # Windows : env\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # N'oublie pas d'ajouter tes clés API !
python run.py
Puis va sur http://localhost:5000 dans ton navigateur.
