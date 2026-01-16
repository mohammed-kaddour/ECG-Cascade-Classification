from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, LeakyReLU

def build_base_cnn(num_classes, input_shape=(224, 224, 1)):
    model = Sequential([
        Conv2D(32, (3, 3), input_shape=input_shape),
        LeakyReLU(alpha=0.1),
        MaxPooling2D(2, 2),

        Conv2D(64, (3, 3)),
        LeakyReLU(alpha=0.1),
        MaxPooling2D(2, 2),

        Conv2D(128, (3, 3)),
        LeakyReLU(alpha=0.1),
        MaxPooling2D(2, 2),

        Flatten(),
        Dense(256),
        LeakyReLU(alpha=0.1),
        Dropout(0.4),
        Dense(num_classes, activation='softmax')
    ])
    return model
