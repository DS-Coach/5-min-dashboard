# 5-min-dashboard
Créer un tableau de bord Pandas Profiling en 5 minutes chrono.

Voilà un *screenshot* du résultat:

![alt text1](assets/dashboard.png "")



## Ingrédients nécessaires
* Python 3 installé sur son poste.
[Voici le lien de téléchargement](https://www.python.org/downloads/)


* 5 minutes de ton temps

* Ta bonne humeur


## Démarrage 

1- Télécharger le répertoire

![alt text1](assets/download.png "")

2- Ouvrir le terminal et se rendre dans le dossier

```
cd 5-min-dashboard
```

3- Charger les *packages*

```
pip install -r requirements.txt
```

4- Rouler le script Python

```python
python src/dashboard_5min.py
```

**Le résultat se trouve dans le dossier sous le format: 5min_dashboard_TITRE_YYYY-MM-DD.html**

## Les options

### Ton propre fichier de données:

```python
python src/dashboard_5min.py -f data/INSERER_TON_FICHIER.csv

python src/dashboard_5min.py -f data/retail_sales_data.csv
```

### Ton propre titre

```python
python src/dashboard_5min.py -t CECI_EST_UN_TITRE_COOL
```

### Ne pas calculer les corrélations
```python
python src/dashboard_5min.py --minimal
```

### Échantillon de données 

Exemple prendre 50 % des lignes aléatoirement.

```python
python src/dashboard_5min.py -s 0.5
```

