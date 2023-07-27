'''
Ce POC utilise scikit-learn pour entraîner un modèle de 
classification SVM sur le célèbre jeu de données iris et évalue sa précision.
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Chargement du jeu de données iris
iris = load_iris()
X, y = iris.data, iris.target

# Division des données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement d'un modèle SVM
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = model.predict(X_test)

# Calcul de la précision
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle :", accuracy)
