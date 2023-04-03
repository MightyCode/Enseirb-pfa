class AudioStream:
    def __init__(self, id) -> None:
        self._id = id
        self._rightValue = 0
        self._leftValue = 0

        self._priority = -1

    def id(self):
        return self._id

    def value(self, left: bool):
        return self._leftValue if left else self._rightValue
    
    def leftValue(self):
        return self._leftValue
    
    def rightValue(self):
        return self._rightValue

    def bothValue(self):
        return [self._leftValue, self._rightValue]

    def setValueBoth(self, priority, value):
        if self._priority <= priority:
            self._priority = priority

            self._leftValue = value
            self._rightValue = value

    def setBothValue(self, priority, valueL, valueR):
        if self._priority <= priority:
            self._priority = priority

            self._leftValue = valueL
            self._rightValue = valueR

    def priority(self):
        return self._priority

    def reset(self):
        self._rightValue = 0
        self._leftValue = 0

        self._priority = -1

    def copy(self):
        copy: AudioStream = AudioStream(self._id)
        copy.setBothValue(self._leftValue, self._rightValue)

        return copy