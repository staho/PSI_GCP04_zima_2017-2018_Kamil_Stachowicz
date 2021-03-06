#!/usr/bin/python


class TestInput():
    """docstring forTestInput."""
    """
        Test input is a vector which represents capital and small letters like as in
        5x7 table
    """
    #testArguments = []
    availableLetters = ['a', 'A', 'b', 'B', 'o', 'C', 'D', 'I', 'F', 'h', 'U', 'K', 'd', 'H', 'c', 'G', 'w']
    def __init__(self, letter):
        self.__dict__['_testArguments'] = []
        #self.__dict__['_desiredOutputs'] = []
        self.__dict__['_letterOfTest'] = letter

        self.getLetter()
        #print(self._testArguments)


    def getLetter(self):
        if self._letterOfTest == 'a':
            self._testArguments.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  1,  1,  1
                ])
            self._testArguments.append([ 0,  0,  1])
            self._testArguments.append([0])

        elif self._letterOfTest == 'b':
            self._testArguments.append([
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  1,  1,  1,  0,
                1,  0,  0,  1,  0,
                1,  0,  0,  1,  0,
                1,  1,  1,  1,  0
                ])
            self._testArguments.append([1,  0,  0])
            self._testArguments.append([0])
        elif self._letterOfTest == 'o':
            self._testArguments.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  1,  1,  0
                ])
            self._testArguments.append([0,  0,  0])
            self._testArguments.append([0])
        elif self._letterOfTest == 'w':
            self._testArguments.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 1,  0,  0,  0,  1,
                 1,  0,  0,  0,  1,
                 1,  0,  1,  0,  1,
                 0,  1,  0,  1,  0
                ])
            self._testArguments.append([1,  0,  1])
            self._testArguments.append([0])
        elif self._letterOfTest == 'c':
            self._testArguments.append([
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  0,  0,
                 0,  1,  0,  0,  0,
                 0,  1,  1,  1,  0
                ])
            self._testArguments.append([0,  0,  0])
            self._testArguments.append([0])
        elif self._letterOfTest == 'h':
            self._testArguments.append([
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  1,  1,  0,  0,
                1,  0,  1,  0,  0,
                1,  0,  1,  0,  0,
                1,  0,  1,  0,  0
                ])
            self._testArguments.append([1,  0,  0])
            self._testArguments.append([0])
        elif self._letterOfTest == 'd':
            self._testArguments.append([
                 0,  0,  0,  0,  1,
                 0,  0,  0,  0,  1,
                 0,  0,  0,  0,  1,
                 0,  0,  1,  1,  1,
                 0,  1,  0,  0,  1,
                 0,  1,  0,  0,  1,
                 0,  1,  1,  1,  1
                ])
            self._testArguments.append([0,  0,  1])
            self._testArguments.append([0])

        elif self._letterOfTest == 'A':
            self._testArguments.append([
                 0, 1,  1,  1,  0,
                 1,  0,  0,  0,  1,
                 1,  0,  0,  0,  1,
                 1,  1,  1,  1,  1,
                 1,  0,  0,  0, 1,
                 1,  0,  0,  0, 1,
                 1,  0,  0,  0,  1
                 ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])
        elif self._letterOfTest == 'B':
            self._testArguments.append([
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])

        elif self._letterOfTest == 'C':
            self._testArguments.append([
             0, 1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  1,
             0, 1,  1,  1,  0,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])

        elif self._letterOfTest == 'D':
            self._testArguments.append([
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])
        elif self._letterOfTest == 'I':
            self._testArguments.append([
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            0,  0,  1,  0,  0,
            ])
            self._testArguments.append([0,  1,  0])
            self._testArguments.append([1])
        elif self._letterOfTest == 'F':
            self._testArguments.append([
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 0,
            1, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            1, 0, 0, 0, 0,
            ])
            self._testArguments.append([1,  1,  0])
            self._testArguments.append([1])
        elif self._letterOfTest == 'G':
            self._testArguments.append([
            0, 1, 1, 1, 0,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 0,
            1, 0, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            0, 1, 1, 1, 0,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])
        elif self._letterOfTest == 'H':
            self._testArguments.append([
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])
        elif self._letterOfTest == 'K':
            self._testArguments.append([
            1, 0, 0, 0, 1,
            1, 0, 0, 1, 0,
            1, 0, 1, 0, 0,
            1, 1, 0, 0, 0,
            1, 0, 1, 0, 0,
            1, 0, 0, 1, 0,
            1, 0, 0, 0, 1,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])
        elif self._letterOfTest == 'U':
            self._testArguments.append([
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            0, 1, 1, 1, 0,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])

        for test in self._testArguments:
            for x in range(len(test)):
                if test[x] == 0:
                    test[x] = -1

    def makeTestInputs(no_of_tests):
        testInputsArray = []
        x = 0
        for i in range(0, no_of_tests):
            testInputsArray.append(TestInput(TestInput.availableLetters[x]))
            x += 1
            if x == len(TestInput.availableLetters):
                x = 0
        return testInputsArray
