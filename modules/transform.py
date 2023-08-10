"""
Author: Muhammad Zaki Fuadi
Date: 11/05/2023
This is the transform.py module.
Usage:
- Transform feature and label data
"""

import tensorflow as tf
import tensorflow_transform as tft

CATEGORICAL_FEATURES = {
    "job": 12,
    "marital": 4,
    "education": 8,
    "default": 3,
    "housing": 3,
    "loan": 3,
    "contact": 2,
    "month": 10,
    "day_of_week": 5,
    "poutcome" : 3
}

NUMERICAL_FEATURES = [
    "age",
    "duration",
    "campaign",
    "pdays",
    "previous",
    "emp.var.rate",
    "cons.price.idx",
    "cons.conf.idx",
    "euribor3m",
    "nr.employed"
]

LABEL_KEY = "y"


def transformed_name(key):
    """Transform feature key

    Args:
        key (str): the key to be transformed

    Returns:
        str: transformed key
    """

    return f"{key}_xf"


def convert_num_to_one_hot(label_tensor, num_labels=2):
    """Convert a label (0 or 1) into a one-hot vector

    Args:
        label_tensor (int): label tensor (0 or 1)
        num_labels (int, optional): num of label. Defaults to 2.

    Returns:
        tf.Tensor: label tensor
    """

    one_hot_tensor = tf.one_hot(label_tensor, num_labels)
    return tf.reshape(one_hot_tensor, [-1, num_labels])


def replace_nan(tensor):
    """Replace nan value with zero number

    Args:
        tensor (list): list data with na data that want to replace

    Returns:
        list with replaced nan value
    """
    tensor = tf.cast(tensor, tf.float64)
    return tf.where(
        tf.math.is_nan(tensor),
        tft.mean(tensor),
        tensor
    )


def preprocessing_fn(inputs):
    """Preprocess input features into transformed features

    Args:
        inputs (dict): map from feature keys to raw features

    Returns:
        dict: map from features keys to transformed features
    """

    outputs = {}

    for key in CATEGORICAL_FEATURES:
        dim = CATEGORICAL_FEATURES[key]
        int_value = tft.compute_and_apply_vocabulary(
            inputs[key], top_k=dim + 1
        )
        outputs[transformed_name(key)] = convert_num_to_one_hot(
            int_value, num_labels=dim + 1
        )

    for feature in NUMERICAL_FEATURES:
        outputs[transformed_name(feature)] = tft.scale_to_0_1(inputs[feature])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs
