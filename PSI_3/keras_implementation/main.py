from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from testinput import *

testData = TestInput()
testData.makeTestInputsRandom(1000)
testDataInput = testData.getInputData()
testDataExpectedOutput = testData.getOutputData()

layers = [30, 1]
lr = 0.05
decay = 0

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

model.fit(testDataInput, testDataExpectedOutput, epochs=1000, batch_size=20)

validationData = TestInput()
validationData.makeTestInputs(0.5)
valDataInput = validationData.getInputData()
valDataOutput = validationData.getOutputData()

scores=model.evaluate(valDataInput, valDataOutput)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print(model.summary())

yhat = model.predict(valDataInput, verbose=0)
for i in range(0, len(yhat)):
    print("x1:", valDataInput[i][0], "x2:", valDataInput[i][1], "y from network:", yhat[i], "from data:", valDataOutput[i])
