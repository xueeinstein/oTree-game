from . import models
from ._builtin import Page


class Warmup(Page):
    form_model = models.Player
    form_fields = ['score']

    q_num = 20
    q_ids = range(1, q_num + 1)
    timeout_seconds = 120

    def before_next_page(self):
        if self.timeout_happened:
            post_dict = self.request.POST.dict()
            self.player.score = post_dict.get('score')

    def vars_for_template(self):
        return {
            'q_ids': self.q_ids,
            'q_num': self.q_num
        }


class Results(Page):
    def vars_for_template(self):
        return {
            'score': self.player.score
        }


page_sequence = [
    Warmup,
    Results
]
