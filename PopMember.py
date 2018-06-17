from smac.configspace import Configuration


class PopMember(object):

    def __init__(config: Configuration,
                 age: int,
                 gender: int):
        self.config = config
        self.age = age
        self.gender = gender

    def increase_age(self):
        self.age += 1
