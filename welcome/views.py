from . import models
from ._builtin import Page


class First(Page):
    pass


class Info(Page):
    form_model = models.Player
    form_fields = ['q_stuID', 'q_age', 'q_gender']

    def before_next_page(self):
        post_dict = self.request.POST.dict()
        self.participant.vars['gender'] = post_dict.get('q_gender')


class Task_Intro(Page):
    pass


page_sequence = [
    First,
    Info,
    Task_Intro
]
