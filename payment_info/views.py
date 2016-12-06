from . import models
from ._builtin import Page, WaitPage


class Select_Round(Page):
    form_model = models.Player
    form_fields = ['selected_round']

    def vars_for_template(self):
        params = {
            'scores': self.participant.vars['scores'],
            'participation_fee': self.session.config['participation_fee']
        }
        params['rounds'] = range(1, len(params['scores']) + 1)
        return params


class Payment_Info(Page):
    def vars_for_template(self):
        selected_round = self.player.selected_round
        payoff = self.participant.vars['payoffs'][selected_round - 1]
        payoff += self.session.config['participation_fee']
        self.player.payoff = payoff
        return {
            'payment': payoff
        }


class Last(Page):
    pass


page_sequence = [
    Select_Round,
    Payment_Info,
    Last
]
