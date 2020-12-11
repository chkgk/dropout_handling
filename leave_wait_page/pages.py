from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class GroupMatching(WaitPage):
    group_by_arrival_time = True
    body_text = "We are looking for a second player. If we cannot find one soon, you will be forwarded automatically."

    def vars_for_template(self):
        # we abuse this function to set the time the participant first arrives on the waitpage.
        if not self.participant.vars.get('start_waiting_time', None):
            self.participant.vars['start_waiting_time'] = time.time()

        return dict()


class Game(Page):
    def is_displayed(self):
        return not self.participant.vars['dropout']


class Dropout(Page):
    def is_displayed(self):
        return self.participant.vars['dropout']


page_sequence = [GroupMatching, Game, Dropout]
