from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import TensorBoard
from keras import optimizers
from prettytable import PrettyTable
from testinput import *


"""Making test points for probes"""
testData = TestInput()
testData.makeTestInputsRandom(1000)
testDataInput = testData.getInputData()
testDataExpectedOutput = testData.getOutputData()

"""Validation data creation"""
validationData = TestInput()
validationData.makeTestInputs(0.5)
valDataInput = validationData.getInputData()
valDataOutput = validationData.getOutputData()


"""Network params"""
layers = [30, 30, 10, 1]
lr = 0.01
decay = 0

log_dir = "./logs-lr" + str(lr) + "-lay"
for lay in layers:
    log_dir += "-" + str(lay)

"""Initiation of tensorBoard"""
tensorBoard = TensorBoard(  log_dir=log_dir,
                            histogram_freq=5,
                            batch_size=20,
                            write_graph=True,
                            write_grads=False,
                            write_images=False,
                            embeddings_freq=0,
                            embeddings_layer_names=None,
                            embeddings_metadata=None
                            )

"""Model creation"""
model=Sequential()

for i in range(len(layers)):
    if i==0:
        model.add(Dense(layers[i], input_dim=2,activation='sigmoid'))
    elif i==len(layers)-1:
        model.add(Dense(layers[i],activation='linear'))
    else:
        model.add(Dense(layers[i],activation='sigmoid'))

adam = optimizers.Adam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=decay)

model.compile(loss='mean_squared_error', optimizer=adam, metrics=['accuracy'])

"""Training network"""
model.fit(  testDataInput,
            testDataExpectedOutput,
            epochs=100000,
            batch_size=20,
            validation_data=(valDataInput, valDataOutput),
            callbacks=[tensorBoard]
            )

"""Evaluating network"""
scores=model.evaluate(valDataInput, valDataOutput)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print(model.summary())
print("LR", lr)

yhat = model.predict(valDataInput, verbose=0)
t = PrettyTable()
t.field_names = ['x1', 'x2', 'PREDICTED', 'EXPECTED']
for i in range(0, len(yhat)):
    t.add_row([valDataInput[i][0], valDataInput[i][1], yhat[i][0], valDataOutput[i]])
print(t)

model.save('model_sieci-'+str(layers)+'-lr-'+str(lr)+'-decay-'+str(decay)+'.h5')
