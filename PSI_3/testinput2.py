#!/usr/bin/python


class TestInput2():
    """docstring forTestInput."""
    """
        Test input is a vector which represents capital and small letters like as in
        5x7 table
    """
    #testArguments = []
    availableLetters = ['a', 'A', 'b', 'B', 'o', 'C', 'D', 'I', 'F', 'h', 'U', 'K', 'd', 'H', 'c', 'G', 'w']
    def __init__(self, letter):
        self.__dict__['_inputData'] = []
        self.__dict__['_outputData'] = []
        self._letterOfTest = letter
        self.getLetter()
        #print(self._testArguments)


    def getLetter(self):
        if self._letterOfTest == 'a':
            self._inputData.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  1,  1,  1
                ])
            self._outputData.append([0])

        elif self._letterOfTest == 'b':
            self._inputData.append([
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  1,  1,  1,  0,
                1,  0,  0,  1,  0,
                1,  0,  0,  1,  0,
                1,  1,  1,  1,  0
                ])
            self._outputData.append([0])
        elif self._letterOfTest == 'o':
            self._inputData.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  1,  1,  0
                ])
            self._outputData.append([0])
        elif self._letterOfTest == 'w':
            self._inputData.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 1,  0,  0,  0,  1,
                 1,  0,  0,  0,  1,
                 1,  0,  1,  0,  1,
                 0,  1,  0,  1,  0
                ])
            self._inputData.append([0])
        elif self._letterOfTest == 'c':
            self._inputData.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  0,  0,
                 0,  1,  0,  0,  0,
                 0,  1,  1,  1,  0
                ])
            self._outputData.append([0])
        elif self._letterOfTest == 'h':
            self._inputData.append([
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  1,  1,  0,  0,
                1,  0,  1,  0,  0,
                1,  0,  1,  0,  0,
                1,  0,  1,  0,  0
                ])
            self._outputData.append([0])
        elif self._letterOfTest == 'd':
            self._inputData.append([
                 0,  0,  0,  0,  1,
                 0,  0,  0,  0,  1,
                 0,  0,  0,  0,  1,
                 0,  0,  1,  1,  1,
                 0,  1,  0,  0,  1,
                 0,  1,  0,  0,  1,
                 0,  1,  1,  1,  1
                ])
            self._outputData.append([0])

        elif self._letterOfTest == 'A':
            self._inputData.append([
                 0, 1,  1,  1,  0,
                 1,  0,  0,  0,  1,
                 1,  0,  0,  0,  1,
                 1,  1,  1,  1,  1,
                 1,  0,  0,  0, 1,
                 1,  0,  0,  0, 1,
                 1,  0,  0,  0,  1
                 ])
            self._outputData.append([1])
        elif self._letterOfTest == 'B':
            self._inputData.append([
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0
            ])
            self._outputData.append([1])

        elif self._letterOfTest == 'C':
            self._inputData.append([
             0, 1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  1,
             0, 1,  1,  1,  0,
            ])
            self._outputData.append([1])

        elif self._letterOfTest == 'D':
            self._inputData.append([
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0,
            ])
            self._outputData.append([1])
        elif self._letterOfTest == 'I':
            self._inputData.append([
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            ])
            self._outputData.append([1])
        elif self._letterOfTest == 'F':
            self._inputData.append([
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 0,
            1, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            ])
            self._outputData.append([1])
        elif self._letterOfTest == 'G':
            self._inputData.append([
            0, 1, 1, 1, 0,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 0,
            1, 0, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            0, 1, 1, 1, 0,
            ])
            self._outputData.append([1])
        elif self._letterOfTest == 'H':
            self._inputData.append([
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            ])
            self._outputData.append([1])
        elif self._letterOfTest == 'K':
            self._inputData.append([
            1, 0, 0, 0, 1,
            1, 0, 0, 1, 0,
            1, 0, 1, 0, 0,
            1, 1, 0, 0, 0,
            1, 0, 1, 0, 0,
            1, 0, 0, 1, 0,
            1, 0, 0, 0, 1,
            ])
            self._outputData.append([1])
        elif self._letterOfTest == 'U':
            self._inputData.append([
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            0, 1, 1, 1, 0,
            ])
            self._outputData.append([1])

    def makeTestInputs(no_of_tests):
        testInputsArray = []
        outputArray = []
        outputLetter = []

        x = 0
        for i in range(0, no_of_tests):
            tmpletter = TestInput2.availableLetters[x]
            tmpData = TestInput2(tmpletter)
            testInputsArray.append(tmpData.getInputData())
            outputArray.append(tmpData.getOutputData())
            outputLetter.append(tmpletter)
            x += 1
            if x == len(TestInput2.availableLetters):
                x = 0
        return (testInputsArray, outputArray, outputLetter)

    def getInputData(self):
        return self._inputData

    def getOutputData(self):
        return self._outputData

    def getLetterOfTest(self):
        return self._letterOfTest
