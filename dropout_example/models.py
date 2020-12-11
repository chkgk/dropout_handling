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


author = 'Christian König gen. Kersting'

doc = """
If multiple players are in a group, it can happen that one or more of the players drop out.
In this case, players who successfully completed the pages and are on the wait page already might have
to wait for a long time. This is because oTree runs down the timeouts for each page and does not check whether the
player is actually still there. Here, we implement a suggestion from the oTree manual which resets timeouts based on
dropout and therefore saves a lot of time for waiting players.
"""


class Constants(BaseConstants):
    name_in_url = 'dropout_example'
    players_per_group = 2
    num_rounds = 1

    page_timeout = 30  # seconds


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['dropped_out'] = False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
