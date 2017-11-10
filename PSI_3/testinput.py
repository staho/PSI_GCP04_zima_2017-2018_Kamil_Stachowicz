#!/usr/bin/python


class TestInput():
    """docstring forTestInput."""
    """
        Test input is a vector which represents emojis like as in
        8x8 table
    """
    availableEmojis = []
    def __init__(self):
        self.__dict__['_testArguments'] = []

    def makeTestInputs(no_of_tests):
        testInputsArray = []
        x = 0
        for i in range(0, no_of_tests):
            testInputsArray.append(TestInput(TestInput.availableEmojis[x]))
            x += 1
            if x == len(TestInput.availableEmojis):
                x = 0
        return testInputsArray
