import json
from json import JSONEncoder, loads, dumps

class BPMNEncoder(JSONEncoder):
    """
    method : default
    """
    def default(self, o): return o.__dict__

class Object:
    """
    method : toJSON
    :return: dumps JSON
    """
    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, cls=BPMNEncoder)

class DumpDict(dict):
    """
    :return: json.dumps(self)
    """
    def __str__(self):
        return json.dumps(self)

class JSON_Object:
    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, cls=BPMNEncoder)

class JsonDictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

class ActiveSentence:
    def __init__(self, nsubj, verb, dobj, clause):
        self.nsubj, self.verb, self.dobj, self.clause = nsubj, verb, dobj, clause

class PassiveSentence:
    def __init__(self, nsubjpass, verbpass, dobj, clause):
        self.nsubjpass, self.verbpass, self.dobj, self.clause = nsubjpass, verbpass, dobj, clause

class BPMNProcess:
    def __init__(self, sequence, signalWord, activityName, conditionName, participantsName, symbol):
        self.sequence, self.signalWord, self.activityName, self.conditionName, self.participantsName, self.symbol = sequence, signalWord, activityName, conditionName, participantsName, symbol

class Condition:
    def __init__(self, sequence, condition):
        self.sequence, self.condition = sequence, condition

class ActivityOneSentence:
    def __init__(self, sentence):
        self.sentence = sentence

class ActivityMoreSentence:
    def __init__(self, activeSentence, passiveSentence):
        self.activeSentence, self.passiveSentence = activeSentence, passiveSentence