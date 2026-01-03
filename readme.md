# Weather Forecast App 🌤️

Une application de prévisions météorologiques pour Alger avec analyse de données historiques et prédictions.

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- **Python 3.8+** ([Télécharger Python](https://www.python.org/downloads/))
- **Node.js 14+** ([Télécharger Node.js](https://nodejs.org/))
- **Git** ([Télécharger Git](https://git-scm.com/))

## 🚀 Installation

### 1️⃣ Cloner le repository

```bash
git clone https://github.com/HyacineD/Weather-Forecast-App.git
cd Weather-Forecast-App
```

### 2️⃣ Créer un environnement virtuel Python

**Sur Windows :**
```bash
python -m venv env
env\Scripts\activate
```

**Sur macOS/Linux :**
```bash
python3 -m venv env
source env/bin/activate
```

💡 **Important** : Vous devez activer l'environnement virtuel à chaque fois que vous ouvrez un nouveau terminal !

### 3️⃣ Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 4️⃣ Installer les dépendances Node.js (si nécessaire)

```bash
npm install
```

### 5️⃣ Configurer les variables d'environnement

**Créez votre fichier `.env` :**

```bash
# Copiez le template
cp .env.example .env
```

**Éditez le fichier `.env` et ajoutez vos clés API :**

```env
FORECAST_API_KEY=votre_cle_api_forecast_ici
ARCHIVE_API_KEY=votre_cle_api_archive_ici
```

#### 🔑 Comment obtenir les clés API ?

1. **Clé Forecast/Archive** : Inscrivez-vous sur [WeatherAPI.com](https://www.weatherapi.com/)
   - Créez un compte gratuit
   - Allez dans votre tableau de bord
   - Copiez votre clé API
   - Collez-la dans `.env`

⚠️ **IMPORTANT** : Ne partagez JAMAIS votre fichier `.env` ! Il contient vos clés secrètes.

### 6️⃣ Tester la configuration

```bash
# Vérifiez que les variables d'environnement sont bien chargées
python config.py
```

Vous devriez voir :
```
==================================================
📋 CONFIGURATION DE L'APPLICATION
==================================================
🌐 Serveur: localhost:5000
🐛 Debug: True
🏙️  Ville par défaut: Algiers
🗣️  Langue: fr
🔑 Forecast API Key: ✅ Définie
🔑 Archive API Key: ✅ Définie
==================================================
```

### 7️⃣ Lancer l'application

```bash
python run.py
```

L'application devrait démarrer sur `http://localhost:5000`

## 📁 Structure du projet

```
Weather-Forecast-App/
├── .env                      # ⚠️ Vos clés API (local uniquement)
├── .env.example              # Template des variables d'environnement
├── .gitignore                # Fichiers ignorés par Git
├── config.py                 # Configuration centralisée
├── api.py                    # Appels API météo
├── run.py                    # Point d'entrée de l'application
├── dataframe.py              # Manipulation de données
├── prediction.py             # Modèle de prédiction
├── requirements.txt          # Dépendances Python
├── package.json              # Dépendances Node.js
├── my_app/                   # Frontend
└── data/                     # Données météo (générées)
```

## 🔧 Commandes utiles

```bash
# Activer l'environnement virtuel
source env/bin/activate         # macOS/Linux
env\Scripts\activate            # Windows

# Désactiver l'environnement virtuel
deactivate

# Mettre à jour les dépendances
pip install -r requirements.txt

# Lancer l'application
python run.py

# Tester la configuration
python config.py
```

## 🐛 Résolution de problèmes

### ❌ Erreur : "FORECAST_API_KEY n'est pas définie"
➡️ **Solution** : Vous n'avez pas créé le fichier `.env` ou il est vide
```bash
cp .env.example .env
# Puis éditez .env et ajoutez vos clés
```

### ❌ Erreur : "No module named 'dotenv'"
➡️ **Solution** : Installez les dépendances
```bash
pip install -r requirements.txt
```

### ❌ Erreur : "python: command not found"
➡️ **Solution** : Utilisez `python3` au lieu de `python`
```bash
python3 run.py
```

### ❌ L'application ne démarre pas
➡️ **Solution** : Vérifiez que :
1. L'environnement virtuel est activé
2. Le fichier `.env` existe et contient vos clés
3. Toutes les dépendances sont installées
4. Le port 5000 n'est pas déjà utilisé

### ❌ Erreur : "Port 5000 already in use"
➡️ **Solution** : Changez le port dans `.env`
```env
PORT=8000
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Veuillez :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Technologies utilisées

- **Backend** : Python 3.8+, Flask
- **Data Science** : Pandas, NumPy, Scikit-learn
- **API** : WeatherAPI.com
- **Frontend** : JavaScript, HTML/CSS
- **Autres** : python-dotenv, requests

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**HyacineD**
- GitHub : [@HyacineD](https://github.com/HyacineD)

## 🙏 Remerciements

- [WeatherAPI.com](https://www.weatherapi.com/) pour l'API météo
- La communauté open source

---

## ⚡ Quick Start (pour les développeurs expérimentés)

```bash
git clone https://github.com/HyacineD/Weather-Forecast-App.git
cd Weather-Forecast-App
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sur Windows
pip install -r requirements.txt
cp .env.example .env
# Éditez .env et ajoutez vos clés API
python run.py
```

🌐 Ouvrez `http://localhost:5000`