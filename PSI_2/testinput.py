#!/usr/bin/python

class TestInput():
    """docstring forTestInput."""
    """
        Test input is a vector which represents capital and small letters like as in
        5x7 table
    """
    #testArguments = []
    def __init__(self, letter):
        self.__dict__['_testArguments'] = []
        self.__dict__['_desiredOutputs'] = []
        self.__dict__['_desiredForLast'] = None
        self.__dict__['_letterOfTest'] = letter

        self.getLetter()


    def getLetter(self):
        if self._letterOfTest == 'a':
            self._testArguments = [
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  1,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  1,  1,  1
                ]
            self._desiredOutputs = [ 0,  0,  0]
            self._desiredForLast =  0
        elif self._letterOfTest == 'b':
            self._testArguments = [
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  0,  0,  0,  0,
                1,  1,  1,  1,  0,
                1,  0,  0,  1,  0,
                1,  0,  0,  1,  0,
                1,  1,  1,  1,  0
                ]
            self._desiredOutputs = [1,  0,  0]
            self._desiredForLast =  0
        elif self._letterOfTest == 'o':
            self._testArguments = [
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  0,  0,  0,  0,
                 0,  1,  1,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  0,  1,  0,
                 0,  1,  1,  1,  0
                ]
            self._desiredOutputs = [ 0,  0, 1]
            self._desiredForLast = 0
        elif self._letterOfTest == 'A':
            self._testArguments = [
                 0, 1,  1,  1,  0,
                 1,  0,  0,  0,  1,
                 1,  0,  0,  0,  1,
                 1,  1,  1,  1,  1,
                 1,  0,  0,  0, 1,
                 1,  0,  0,  0, 1,
                 1,  0,  0,  0,  1
                 ]
            self._desiredOutputs = [1, 1, 1]
            self._desiredForLast = 1
        elif self._letterOfTest == 'B':
            self._testArguments = [
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0
            ]
            self._desiredOutputs = [1, 1, 1]
            self._desiredForLast = 1

        elif self._letterOfTest == 'C':
            self._testArguments = [
             0, 1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  0,
            1,  0,  0,  0,  1,
             0, 1,  1,  1,  0,
            ]
            self._desiredOutputs = [1, 1, 1]
            self._desiredForLast = 1

        elif self._letterOfTest == 'D':
            self._testArguments = [
            1,  1,  1,  1,  0,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  0,  0,  0,  1,
            1,  1,  1,  1,  0,
            ]
            self._desiredOutputs = [1, 1, 1]
            self._desiredForLast = 1
