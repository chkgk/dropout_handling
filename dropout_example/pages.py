from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GamePage1(Page):
    template_name = 'dropout_example/GamePage.html'

    def is_displayed(self):
        # for demonstration purposes, we send players with group id == 2 straight to the wait page.
        # the is_displayed part is not part of the fast-forward mechanism and only here to show it in action.
        return self.player.id_in_group != 2

    # This block needs to be present on all pages that should be fast-forwarded in case of a dropout.
    def get_timeout_seconds(self):
        if self.participant.vars.get('dropped_out'):
            return 1  # instant timeout, 1 second
        else:
            return Constants.page_timeout

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['dropped_out'] = True
    # # #


class GamePage2(Page):
    template_name = 'dropout_example/GamePage.html'
    
    def is_displayed(self):
        # for demonstration purposes, we send players with group id == 2 straight to the wait page.
        # the is_displayed part is not part of the fast-forward mechanism and only here to show it in action.
        return self.player.id_in_group != 2

    # This block needs to be present on all pages that should be fast-forwarded in case of a dropout.
    def get_timeout_seconds(self):
        if self.participant.vars.get('dropped_out'):
            return 1  # instant timeout, 1 second
        else:
            return Constants.page_timeout

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['dropped_out'] = True
    # # #


class GamePage3(Page):
    template_name = 'dropout_example/GamePage.html'
    
    def is_displayed(self):
        # for demonstration purposes, we send players with group id == 2 straight to the wait page.
        # the is_displayed part is not part of the fast-forward mechanism and only here to show it in action.
        return self.player.id_in_group != 2

    # This block needs to be present on all pages that should be fast-forwarded in case of a dropout.
    def get_timeout_seconds(self):
        if self.participant.vars.get('dropped_out'):
            return 1  # instant timeout, 1 second
        else:
            return Constants.page_timeout

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['dropped_out'] = True
    # # #


class CollectPlayers(WaitPage):
    body_text = """
        In this example, players with group_id == 2 are sent to the wait page immediately, 
        for demonstration purposes.
        Normally, if a player drops out, the wait page is only reached after the sum of all timeouts on all previous
        pages has passed. In this implementation, if a timeout occurs on any page, the remaining pages are 
        "fast forwarded", i.e. their timeouts are set to 1 second. This drastically reduced wait times for players that
        did not drop out.
        Specifically, in this example, there are 3 pages with a 30 second timeout each. Normally, a dropout would 
        cause the other player to wait up to 90 seconds before they can move on. With fast-forwarding, the wait time
        is reduced to a maximum of 32 seconds.
        """


class Results(Page):
    pass

page_sequence = [GamePage1, GamePage2, GamePage2, CollectPlayers, Results]
