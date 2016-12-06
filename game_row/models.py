"""
Main Gaming Rounds 1-7
"""
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


# record a global round number for Player
round_num = 1


class Constants(BaseConstants):
    players_per_group = 4
    num_rounds = 6
    name_in_url = 'game_row'


class Subsession(BaseSubsession):
    def before_session_starts(self):
        global round_num
        round_num = self.round_number


class Group(BaseGroup):
    def set_ranks_payoffs(self):
        players = [self.get_player_by_id(i) for i in range(1, 5)]
        sorted_players = sorted(players, key=lambda p: p.score, reverse=True)
        for rank, p in enumerate(sorted_players):
            if rank == 0:
                p.rank = 'First'
            elif rank == 1:
                p.rank = 'Second'
            elif rank == 2:
                p.rank = 'Third'
            elif rank == 3:
                p.rank = 'Fourth'

        # set payoff according to score, method
        for p in players:
            if p.method == 'Method A':
                p.payoff = p.score
            elif p.method == 'Method B':
                if p.rank == 'First':
                    p.payoff = 4 * p.score
                else:
                    p.payoff = 0
            elif p.method == 'Method C':
                if random.random() < 0.25:
                    p.payoff = 4 * p.score
                else:
                    p.payoff = 0

            # additional bonus if rank guessed is right
            if p.rank == p.rank_guessed:
                p.payoff += 4

            # record payoff in session so that it can be accessed in payment_info subsession
            if 'payoffs' not in p.participant.vars.keys():
                p.participant.vars['payoffs'] = []

            p.participant.vars['payoffs'].append(p.payoff)

            # record scores of each round in session so that it can be accessed in payment_info subsession
            if 'scores' not in p.participant.vars.keys():
                p.participant.vars['scores'] = []

            p.participant.vars['scores'].append(p.score)


class Player(BasePlayer):
    score = models.IntegerField(initial=0)
    method = models.CharField(initial=None)
    rank_guessed = models.CharField(initial=None,
                                    choices=['First', 'Second', 'Third', 'Fourth'],
                                    verbose_name='Please guess your rank in this round:',
                                    widget=widgets.RadioSelect())
    rank = models.CharField(initial=None)
