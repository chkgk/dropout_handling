# Techniques for dropout handling in oTree experiments

## Overview
The oTree manual describes two methods to reduce and handle dropouts in interactive experiments with multiple players. The repository contains implementations of these suggestions.

## Fast-forwarding players who have dropped out
The app ``dropout_example`` demonstrates 'fast-forwarding' of participants who have dropped out through the pages leading to the next wait page. If players drop out and the pages have timeouts, oTree moves participants forward through the page sequence only if the timeouts occur or the participant submits a page. If, for example, each page has a timeout of 30 seconds and the player drops out on the first, the other players have to wait up to (3x30=) 90 seconds on the waitpage, despite a player having left already.

The manual suggest to dynamically adjust timeouts if a dropout is detected on any page. Basically, the player is marked as "dropped out" and subsequent page timeouts are reduced to 1 second each. This drastically reduced the time others have to wait for the player who has dropped out. In the example, the waiting time is cut to a maximum of (30+1+1=) 32 seconds.


## Allow players to leave a group matching stage
Using ``group_by_arriva_time`` drastically reduces waiting times for participants on group matching stages. However, one might want to limit the time participants have to wait on these pages in case no match is found. Especially on online platforms like mTurk it is important that players can still reach the end of the experiment and receive their code to complete the experiment. It is not their fault that they could not be matched with another player in time.

In the second app, ``leave_wait_page``, I demonstrate another suggestion from the oTree manual. The app implements a maximum waiting time on the wait page. We use the fact that wait pages regularly reload. The page reload triggers the ``group_by_arrival_time_method``. If any waiting player's page reload calls this method, we check if any of the waiting players have been waiting too long. In this case, we create a one-player group and allow them to continue. With some clever display conditions, this player could be forwarded to the end of the experiment and receive their payment. 

## Background
Dropouts can occur for any number of reasons. With standard wait pages, other players might get stuck waiting for players who have dropped out. This was the reason for the development of the custom mTurk wait page as well as the leavable wait page. Neither works with oTree 3.x and they are hard to adapt because of some changes in otree-core.

