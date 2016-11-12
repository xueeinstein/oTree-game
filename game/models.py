"""
Main Gaming Rounds 1-7
"""
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

# record a global round number for Player
round_num = 1


class Constants(BaseConstants):
    players_per_group = 4
    num_rounds = 7
    name_in_url = 'game'


class Subsession(BaseSubsession):
    def before_session_starts(self):
        global round_num
        round_num = self.round_number

        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score = models.IntegerField(initial=0)
    method = models.CharField(initial=None)
    guess_rank = models.CharField(initial=None,
                                  choices=['First', 'Second', 'Third', 'Fourth'],
                                  verbose_name='Please guess your rank in this round:',
                                  widget=widgets.RadioSelect())
