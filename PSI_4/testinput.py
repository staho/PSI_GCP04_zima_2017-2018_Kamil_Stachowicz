"""Klasa z emoji (wejsciami)"""
class TestInput():
    avaliableEmojis = ["sad","D","wrr","xD", "|"]   #lista dostepnych emoji w danych

    def __init__(self):
        self.inputsMap = {}
        self.makeInputs()

    """Wszystkie emoji w formie binarnej"""
    def makeInputs(self):
        for emoji in TestInput.avaliableEmojis:
            if emoji == "|":
                self.inputsMap["|"]=[
                    0,0,0,0,0,0,0,0,
                    0,1,1,0,0,1,1,0,
                    0,1,1,0,0,1,1,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,1,1,1,1,1,1,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    ]
            if emoji == "D":
                 self.inputsMap["D"] = [
                    0,0,0,0,0,0,0,0,
                    0,1,1,0,0,1,1,0,
                    0,1,1,0,0,1,1,0,
                    0,0,0,0,0,0,0,0,
                    0,1,1,1,1,1,1,0,
                    0,1,1,1,1,1,1,0,
                    0,0,1,1,1,1,0,0,
                    0,0,0,0,0,0,0,0,
                    ]
            if emoji == "sad":
                 self.inputsMap["sad"] = [
                    0,0,0,0,0,0,0,0,
                    0,1,1,0,0,1,1,0,
                    0,1,0,0,0,0,1,0,
                    0,0,0,0,0,0,0,0,
                    0,0,1,1,1,1,0,0,
                    0,1,0,0,0,0,1,0,
                    0,1,0,0,0,0,1,0,
                    0,0,0,0,0,0,0,0,
                    ]
            if emoji == "wrr":
                 self.inputsMap["wrr"] = [
                    0,1,0,0,0,0,1,0,
                    0,1,1,0,0,1,1,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,1,1,0,0,0,
                    0,0,1,0,0,1,0,0,
                    0,1,0,0,0,0,1,0,
                    0,0,0,0,0,0,0,0,
                    ]
            if emoji == "xD":
                 self.inputsMap["xD"] = [
                    0,1,1,0,0,1,1,0,
                    0,0,0,1,1,0,0,0,
                    0,1,1,0,0,1,1,0,
                    0,0,0,0,0,0,0,0,
                    0,1,1,1,1,1,1,0,
                    0,1,0,0,0,0,1,0,
                    0,0,1,1,1,1,0,0,
                    0,0,0,0,0,0,0,0,
                    ]
    def getInputsMap(self): #zwrocenie danych jako mapy
        return self.inputsMap