import pandas as pd
from sklearn.ensemble import IsolationForest
from .models import Equipo


def detectar_anomalias():

    datos = list(
        Equipo.objects.values(
            'id',
            'estado'
        )
    )

    if len(datos) < 3:
        return []

    df = pd.DataFrame(datos)

    # Convertir estado a número
    mapa = {
        'activo': 0,
        'reparacion': 1,
        'baja': 2
    }

    df['estado_num'] = df['estado'].map(mapa)

    modelo = IsolationForest(contamination=0.2)
    df['anomalia'] = modelo.fit_predict(df[['estado_num']])

    sospechosos = df[df['anomalia'] == -1]

    return sospechosos['id'].tolist()
