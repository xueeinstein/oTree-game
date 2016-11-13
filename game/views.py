from . import models
from ._builtin import Page, WaitPage
import random


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


class GameWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


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


class Results(Page):
    form_model = models.Player
    form_fields = ['rank_guessed']

    def vars_for_template(self):
        return {
            'score': self.player.score
        }


def generate_gender_gmat(M_players, F_players):
    """Generate gender-constraint random group"""
    random.shuffle(M_players)
    random.shuffle(F_players)
    group_mat = []
    new_group = []
    mem_num = 0
    while M_players:
        new_group.append(M_players.pop())
        mem_num += 1
        if mem_num == 4:
            group_mat.append(new_group)
            new_group = []
            mem_num = 0

    while F_players:
        new_group.append(F_players.pop())
        mem_num += 1
        if mem_num == 4:
            group_mat.append(new_group)
            new_group = []
            mem_num = 0

    random.shuffle(group_mat)
    return group_mat


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        if self.round_number == 7:
            # randomly match with three other players of the same gender
            players = self.subsession.get_players()
            M_players = [p for p in players if p.participant.vars['gender'] == 'Male']
            F_players = [p for p in players if p.participant.vars['gender'] == 'Female']
            group_mat = generate_gender_gmat(M_players, F_players)
            self.subsession.set_group_matrix(group_mat)


class PayoffWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_ranks_payoffs()


page_sequence = [
    ShuffleWaitPage,
    Instruction,
    GameWaitPage,
    Gaming,
    Results,
    PayoffWaitPage
]

