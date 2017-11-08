#!/usr/bin/python


class TestInput():
    """docstring forTestInput."""
    """
        Test input is a vector which represents capital and small letters like as in
        5x7 table
    """
    #testArguments = []
    availableLetters = ['a', 'b', 'o', 'A', 'B', 'C', 'D']
    def __init__(self, letter):
        self.__dict__['_testArguments'] = []
        #self.__dict__['_desiredOutputs'] = []
        self.__dict__['_letterOfTest'] = letter

        self.getLetter()
        #print(self._testArguments)


    def getLetter(self):
        if self._letterOfTest == 'a':
            self._testArguments.append([
                 -1,  -1,  -1,  -1,  -1,
                 -1,  -1,  -1,  -1,  -1,
                 -1,  -1,  -1,  -1,  -1,
                 -1,  -1,  1,  1,  -1,
                 -1,  1,  -1,  1,  -1,
                 -1,  1,  -1,  1,  -1,
                 -1,  1,  1,  1,  1
                ])
            self._testArguments.append([ -1,  -1,  1])
            self._testArguments.append([-1])

        elif self._letterOfTest == 'b':
            self._testArguments.append([
                1,  -1,  -1,  -1,  -1,
                1,  -1,  -1,  -1,  -1,
                1,  -1,  -1,  -1,  -1,
                1,  1,  1,  1,  -1,
                1,  -1,  -1,  1,  -1,
                1,  -1,  -1,  1,  -1,
                1,  1,  1,  1,  -1
                ])
            self._testArguments.append([1,  -1,  -1])
            self._testArguments.append([-1])
        elif self._letterOfTest == 'o':
            self._testArguments.append([
                 -1,  -1,  -1,  -1,  -1,
                 -1,  -1,  -1,  -1,  -1,
                 -1,  -1,  -1,  -1,  -1,
                 -1,  1,  1,  1,  -1,
                 -1,  1,  -1,  1,  -1,
                 -1,  1,  -1,  1,  -1,
                 -1,  1,  1,  1,  -1
                ])
            self._testArguments.append([-1,  -1,  -1])
            self._testArguments.append([-1])
        elif self._letterOfTest == 'A':
            self._testArguments.append([
                 -1, 1,  1,  1,  -1,
                 1,  -1,  -1,  -1,  1,
                 1,  -1,  -1,  -1,  1,
                 1,  1,  1,  1,  1,
                 1,  -1,  -1,  -1, 1,
                 1,  -1,  -1,  -1, 1,
                 1,  -1,  -1,  -1,  1
                 ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])
        elif self._letterOfTest == 'B':
            self._testArguments.append([
            1,  1,  1,  1,  -1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  1,
            1,  1,  1,  1,  -1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  1,
            1,  1,  1,  1,  -1
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])

        elif self._letterOfTest == 'C':
            self._testArguments.append([
             -1, 1,  1,  1,  -1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  -1,
            1,  -1,  -1,  -1,  -1,
            1,  -1,  -1,  -1,  -1,
            1,  -1,  -1,  -1,  1,
             -1, 1,  1,  1,  -1,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])

        elif self._letterOfTest == 'D':
            self._testArguments.append([
            1,  1,  1,  1,  -1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  1,
            1,  -1,  -1,  -1,  1,
            1,  1,  1,  1,  -1,
            ])
            self._testArguments.append([1,  1,  1])
            self._testArguments.append([1])

    def makeTestInputs(no_of_tests):
        testInputsArray = []
        x = 0
        for i in range(0, no_of_tests):
            testInputsArray.append(TestInput(TestInput.availableLetters[x]))
            x += 1
            if x == len(TestInput.availableLetters):
                x = 0
        return testInputsArray
