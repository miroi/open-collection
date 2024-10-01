import tensorflow as tf
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles

# generate 2d classification dataset
x, y = make_circles(n_samples=1000, noise=0.1, random_state=1)

# scatter plot for each class value
for class_value in range(2):
	# select indices of points with the class label
	row_ix = np.where (y == class_value)
	# scatter plot for points with a different color
	pyplot.scatter(x[row_ix, 0], x[row_ix, 1])
# show plot
pyplot.show()


# split into train, test and validation sets in defined portions
train_ratio = 0.75
validation_ratio = 0.15
test_ratio = 0.10

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size= 1-train_ratio)
val_x, test_x, val_y, test_y = train_test_split(test_x, test_y, test_size=test_ratio/(test_ratio + validation_ratio)) 


# define model
model = tf.keras.models.Sequential()

# define activation functions and initialization of weights 
model.add(tf.keras.layers.Dense(50, input_dim=2, activation='relu', kernel_initializer='he_uniform'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))


opt = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())

# fit model
history = model.fit(train_x, train_y, validation_data=(val_x, val_y), epochs=200, verbose=0)

# evaluate the model
_, train_acc = model.evaluate(train_x, train_y, verbose=0)
_, val_acc = model.evaluate(val_x, val_y, verbose=0)
_, test_acc = model.evaluate(test_x, test_y, verbose=0)
print('Train: %.3f, Validation: %.3f, Test: %.3f' % (train_acc, val_acc, test_acc))

# plot loss during training
pyplot.subplot(211)
pyplot.title('Loss')
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='validation')
pyplot.legend()

# plot accuracy during training
pyplot.subplot(212)
pyplot.title('Accuracy')
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='validation')
pyplot.legend()
pyplot.show()

# Delete NN model
tf.keras.backend.clear_session()