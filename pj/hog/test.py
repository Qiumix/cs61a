from hog import *

always_three = make_test_dice(3)
always = always_roll


def play(strategy0,
         strategy1,
         score0=0,
         score1=0,
         dice=six_sided,
         goal=GOAL_SCORE,
         say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while True:
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1, dice)
            if score0 >= goal:
                break
            while extra_turn(score0, score1):
                score0 += take_turn(strategy0(score0, score1), score1, dice)
                if score0 >= goal:
                    break
            who = other(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
        else:
            score1 += take_turn(strategy1(score1, score0), score0, dice)
            if score1 >= goal:
                break
            while extra_turn(score1, score0):
                score1 += take_turn(strategy1(score1, score0), score0, dice)
                if score1 >= goal:
                    break
            who = other(who)
    # END PROBLEM 6
    return score0, score1


s0, s1, = play(always(5), always(3), goal=25, dice=always_three)

print(s0, s1)
