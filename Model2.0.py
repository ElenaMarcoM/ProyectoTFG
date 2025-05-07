from scr_training.Descarga_enlace import  *
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import (
    Input, Conv1D, Lambda, Dense, Concatenate, Reshape,
    BatchNormalization, ReLU, Add, Flatten
)
from tensorflow.keras.models import Model, Sequential

# ----- CARGA Y PREPARACIÓN DE DATOS -----
compressed_path = os.path.join("resources", "fingerprints_og.pklz")
with bz2.BZ2File(compressed_path, "rb") as f:
    fingerprints = pickle.load(f, encoding='latin1')

feature_cols = [col for col in fingerprints.columns if col.startswith('V')]
X = fingerprints[feature_cols].values.astype(np.float32)
y = fingerprints['rt'].values.astype(np.float32)

# Normalizar la salida (si no está ya normalizada)
# y = (y - y.mean()) / y.std()

X = X.reshape(-1, len(feature_cols), 1)

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# ----- BLOQUE RESNET PERSONALIZADO -----
def resnet_block(x, filters, kernel_size=3):
    shortcut = x
    x = Conv1D(filters, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)
    x = ReLU()(x)
    x = Conv1D(filters, kernel_size, padding='same')(x)
    x = BatchNormalization()(x)
    if shortcut.shape[-1] != filters:
        shortcut = Conv1D(filters, 1, padding='same')(shortcut)
    x = Add()([x, shortcut])
    return ReLU()(x)

# ----- DEFINICIÓN DEL MODELO -----
NUM_SUBGROUPS = 4
TOTAL_LENGTH = X.shape[1]
SUBGROUP_SIZE = TOTAL_LENGTH // NUM_SUBGROUPS

input_layer = Input(shape=(TOTAL_LENGTH, 1))

x = Conv1D(filters=16, kernel_size=7, padding='same', activation='relu')(input_layer)

subgroup_outputs = []
for i in range(NUM_SUBGROUPS):
    segment = Lambda(lambda t: t[:, i * SUBGROUP_SIZE:(i + 1) * SUBGROUP_SIZE, :])(x)

    resnet_out = resnet_block(segment, filters=32)

    # ResNet de Keras:
    # reshaped = Reshape((32, 32, 1))(segment)
    # resnet_out = ResNet50(include_top=False, weights=None, input_shape=(32, 32, 1), pooling='avg')(reshaped)

    reduced = Dense(64, activation='relu')(Flatten()(resnet_out))
    subgroup_outputs.append(reduced)

concatenated = Concatenate()(subgroup_outputs)

final_block = Sequential([
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])
output = final_block(concatenated)

model = Model(inputs=input_layer, outputs=output)
model.compile(optimizer='adam', loss='mae', metrics=['mae'])
model.summary()

# ----- TRAIN -----
early_stop = EarlyStopping(
    monitor='val_mae',
    patience=10,
    restore_best_weights=True,
    verbose=1
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=128,
    callbacks=[early_stop]
)


# ----- VISUALIZAR MAE/VAL_MAE Y LOSS/VAL_LOSS -----
plt.figure(figsize=(12, 5))

# MAE
plt.subplot(1, 2, 1)
plt.plot(history.history['mae'], label='Entrenamiento MAE')
plt.plot(history.history['val_mae'], label='Validación MAE')
plt.axhline(y=10.0, color='r', linestyle='--', label='Objetivo MAE < 10')
plt.xlabel('Épocas')
plt.ylabel('MAE')
plt.title('Evolución del MAE')
plt.legend()
plt.grid(True)

# Loss (es MAE en este caso, pero puede separarse si se cambia la loss)
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Entrenamiento Loss')
plt.plot(history.history['val_loss'], label='Validación Loss')
plt.xlabel('Épocas')
plt.ylabel('Loss (MAE)')
plt.title('Evolución de la función de pérdida')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()