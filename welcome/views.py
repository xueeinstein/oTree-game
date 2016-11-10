from . import models
from ._builtin import Page, WaitPage


class Info(Page):
    form_model = models.Player
    form_fields = ['q_stuID', 'q_age', 'q_gender', 'q_major']


page_sequence = [
    Info
]
