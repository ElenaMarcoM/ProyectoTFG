import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, regularizers
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle
import bz2


def load_data(filename):
    """Carga los datos desde un archivo comprimido en formato pickle.
    Args:
        filename (str): File with the finguerprints used.

    Returns:
        X: All binary information attach to each pid
        Y: Contains the column rt
    """
    with bz2.BZ2File(filename, "rb") as f:
        data = pickle.load(f, encoding='latin1')[:1000]
    X = data.drop(columns=['pid', 'rt']).values  # Características
    y = data['rt'].values  # Variable objetivo
    return X, y

def create_conv_block(filters, kernel_size):
    """
    -> Creates a 1D convolution block.
    Args:
        filters (int): Number of filters (exits) that will be used
        kernel_size (int): Filter size (number of steps taken).
        l2_reg:
    Returns:
         (layer): 1D convolution layer with define filters, RELU activated and same padding.
         (layer): MaxPooling 1D layer to reduce the dimensions of the convolution.
    """
    return keras.Sequential([
        layers.Conv1D(filters, kernel_size, activation='relu', padding='same'),
        layers.MaxPooling1D(pool_size=2)
    ])

def create_dense_block(units, dropout_rate=0.5, l2_reg=0.01):
    """
    -> Create a dense layer with L2 regularization.
    Args:
        units (str): File with the finguerprints used.
        dropout_rate (float): Dropout rate (prevent overadjustment).
        l2_reg (float): L2 regularization factor.
    Returns:
        (layer): Dense layer.
        (layer): Dropout layer.
    """
    return keras.Sequential([
        layers.Dense(units, activation='relu', kernel_regularizer=regularizers.l2(l2_reg)),
        layers.Dropout(dropout_rate)
    ])


def build_model(input_shape):
    """
    -> Creates the model ued for the sequential regression model.
    Args:
        input_shape (tupla): Form of the data indicating the dimenions.
    Returns:
        model (model): Compiled Keras model.
    """
    model = models.Sequential()
    model.add(layers.Input(shape=input_shape))
    model.add(create_conv_block(32, 3))
    model.add(create_conv_block(64, 3))
    model.add(layers.Flatten())
    model.add(create_dense_block(128))
    model.add(layers.Dense(1, activation='linear'))  # Salida escalar para regresión

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# def training...s
  #xtrainval = scipy.plit
# Cargar datos
filename = 'fingerprints.pklz'
X, y = load_data(filename)

# Normalizar datos
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Redimensionar para convoluciones 1D (agregando dimensión de canal)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Dividir datos en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir y entrenar modelo
model = build_model((X.shape[1], 1))
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=32)

# Resumen del modelo
model.summary()