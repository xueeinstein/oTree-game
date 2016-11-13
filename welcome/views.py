from . import models
from ._builtin import Page


class Info(Page):
    form_model = models.Player
    form_fields = ['q_stuID', 'q_age', 'q_gender', 'q_major']

    def before_next_page(self):
        post_dict = self.request.POST.dict()
        self.participant.vars['gender'] = post_dict.get('q_gender')


class Task_Intro(Page):
    pass


page_sequence = [
    Info,
    Task_Intro
]
