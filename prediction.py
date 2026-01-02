from sklearn.ensemble import RandomForestRegressor

class Model:
    def __init__(self):
        self.model = RandomForestRegressor(
                n_estimators=300,          # Plus d'arbres = meilleure performance
                max_depth=15,              # Plus profond pour capturer plus de patterns
                min_samples_split=5,       # Évite l'overfitting
                min_samples_leaf=2,        # Évite l'overfitting
                max_features='sqrt',       # Meilleure généralisation
                bootstrap=True,
                oob_score=True,            # Score out-of-bag pour validation
                random_state=42,
                n_jobs=-1                  # Utilise tous les CPU
            )

    def train(self,df, X_train, y_train):
        X_train = X_train.drop(columns=['date'])
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        X_test = X_test.drop(columns=['date'])
        return self.model.predict(X_test)
