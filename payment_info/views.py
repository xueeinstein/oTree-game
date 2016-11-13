from . import models
from ._builtin import Page, WaitPage


class Select_Round(Page):
    form_model = models.Player
    form_fields = ['selected_round']


class Payment_Info(Page):
    def vars_for_template(self):
        selected_round = self.player.selected_round
        payoff = self.participant.vars['payoffs'][selected_round - 1]
        print(self.participant.vars['payoffs'])
        print(payoff)
        return {
            'payoff': payoff
        }


class Last(Page):
    pass


page_sequence = [
    Select_Round,
    Payment_Info,
    Last
]
