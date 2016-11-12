from . import models
from ._builtin import Page


class Instruction(Page):
    form_model = models.Player
    form_fields = ['method']

    def vars_for_template(self):
        round_id = self.round_number
        variables = {
            'round': round_id,
            'method_ab': [1, 4, 6, 7],
            'instruction': 'game/Instruction_R' + str(round_id) + '.html'
        }

        return variables


class Gaming(Page):
    form_model = models.Player
    form_fields = ['score']

    q_num = 40
    q_ids = range(1, q_num + 1)
    timeout_seconds = 300

    def before_next_page(self):
        if self.timeout_happened:
            post_dict = self.request.POST.dict()
            self.player.score = post_dict.get('score')

    def vars_for_template(self):
        variables = {
            'q_ids': self.q_ids,
            'q_num': self.q_num,
            'round': self.round_number
        }

        return variables


page_sequence = [
    Instruction
]
