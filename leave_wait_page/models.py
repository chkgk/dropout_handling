from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import time


author = 'Christian König gen. Kersting'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'leave_wait_page'
    players_per_group = None
    num_rounds = 1

    max_group_match_waiting = 15  # seconds


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['dropout'] = False

    def group_by_arrival_time_method(self, waiting_players):
        # handle group matching:
        if len(waiting_players) >= 2:
            return waiting_players[:2]

        # we only get here, if not enough players are waiting
        # every 30 seconds (approx.) the wait page reloads. These reloads trigger this method.
        for p in waiting_players:
            if p.matching_takes_too_long():
                p.participant.vars['dropout'] = True
                return [p]  # make sure your app can handle a group with size 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def matching_takes_too_long(self):
        now = time.time()
        return now - self.participant.vars.get('start_waiting_time', now) > Constants.max_group_match_waiting
