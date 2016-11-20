"""
Welcome session

collect participants basic information: student ID, gender, age, major
"""
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'welcome'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_stuID = models.PositiveIntegerField(verbose_name='What is your student ID?')

    q_age = models.PositiveIntegerField(verbose_name='What is your age?',
                                        choices=range(15, 41),
                                        initial=None)

    q_gender = models.CharField(initial=None,
                                choices=['Male', 'Female'],
                                verbose_name='What is your gender?',
                                widget=widgets.RadioSelect())
