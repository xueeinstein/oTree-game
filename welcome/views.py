from . import models
from ._builtin import Page


class Info(Page):
    form_model = models.Player
    form_fields = ['q_stuID', 'q_age', 'q_gender', 'q_major']


class Task_Intro(Page):
    pass


page_sequence = [
    Info,
    Task_Intro
]
