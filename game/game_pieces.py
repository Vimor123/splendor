class Card:
    def __init__(level, vp, resource, w, u, b, r, g):
        self.level = level
        self.vp = vp
        self.resource = resource
        self.cost = { "w" : w,
                      "u" : u,
                      "b" : b,
                      "r" : r,
                      "g" : g }

class Player:
    def __init__():
        self.vp = 0
        self.production = { "w" : 0,
                            "u" : 0,
                            "b" : 0,
                            "r" : 0,
                            "g" : 0}
        self.tokens = { "w" : 0,
                        "u" : 0,
                        "b" : 0,
                        "r" : 0,
                        "g" : 0,
                        "j" : 0 }
        self.reserved_cards = []
        self.built_cards = []
        self.nobles = []

class Bank:
    def __init__(no_of_players):
        no_of_tokens = { 2 : 4, 3 : 5, 4 : 7 }
        self.resources = { "w" : no_of_tokens[no_of_players],
                           "u" : no_of_tokens[no_of_players],
                           "b" : no_of_tokens[no_of_players],
                           "r" : no_of_tokens[no_of_players],
                           "g" : no_of_tokens[no_of_players],
                           "j" : 5 }

class Noble:
    def __init__(vp, w, u, b, r, g):
        self.vp = vp
        self.requirements = { "w" : w,
                              "u" : u,
                              "b" : b,
                              "r" : r,
                              "g" : g }
