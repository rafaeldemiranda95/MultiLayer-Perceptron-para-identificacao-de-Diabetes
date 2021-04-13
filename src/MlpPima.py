import pandas
import numpy as np
from sklearn.neural_network import MLPClassifier
import pickle

filename = 'model.sav'


def saveModel(mlp):
    tmp = pickle.dump(mlp, open(filename, 'wb'))
    print(f'value of tmp: {tmp}')


def loadModel():
    mlpModel = None
    try:
        mlpModel = pickle.load(open(filename, 'rb'))
    finally:
        return mlpModel


def createModel():
    dados = pandas.read_csv('../training/pima-indians-diabetes.data.csv')
    objetivo = dados.Outcome
    dados_treinamento = dados.drop(['Outcome'], axis=1)
    dados_tr = np.asarray(dados_treinamento)
    mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(32, 26), random_state=1, max_iter=10000)
    x = dados_tr
    y = objetivo
    mlp.fit(x, y)
    saveModel(mlp)

    return mlp


def ModelPredict(x):
    mlp = loadModel()

    if mlp is None:
        mlp = createModel()

    return mlp.predict(x)
