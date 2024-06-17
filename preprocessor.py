import tensorflow as tf
import keras


def preprocess_image(path, size=(128, 128), mask=False):
    img = keras.preprocessing.image.load_img(path)
    img = tf.convert_to_tensor(img)
    img = tf.cast(img, tf.float32)
    img = tf.image.resize(img, size)
    img = img / 255
    img = tf.expand_dims(img, axis=0)
    if mask:
        img = tf.image.rgb_to_grayscale(img)
    return img