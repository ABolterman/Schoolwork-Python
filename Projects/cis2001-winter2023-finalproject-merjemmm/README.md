ASSIGNMENT DESCRIPTION

Please submit the url to your repo AND a self assessment AND a partner assessment


Texas Holdem Odds

Using the Monte Carlo method - https://en.wikipedia.org/wiki/Monte_Carlo_method

Display odds of winning a 1 v 1 Texas holdem game vs a computer - https://en.wikipedia.org/wiki/Texas_hold_%27em

Poker Hand ranks - https://en.wikipedia.org/wiki/List_of_poker_hands
 

Our simple version always has the player bet first ( $0 is an option - computer should always call ),
and the computer will either fold or call - if it has a 50% or better chance of winning it will call, otherwise it folds

4 rounds of play - display odds of winning to the player

1st round, player and computer each get 2 cards, no shared cards -
( 2,118,760 possible 5 shared card combinations , 990 possible 2 card opponent hands for each of those) 
2,097,572,400 possible combinations of 5 shared cards and 2 opponent cards - maybe 1% is a good size to sample

If the computer does not fold:

2nd round - 3 cards are put in the shared pool - 
1,081 possible 5 shared card combinations now - 990 possible opponent hands - 1,070,190 possible combinations total

3rd round - a 4th card is put in the shared pool - 
46 possible 5 shared card combinations - 990 possible opponents hands - 45,540 possible combinations total

4th round - 5th card is put in the shared pool - 990 possible opponents hands

 

Track the players $ and the computers $, start the player and computer with $100 each

don't allow the player to bet more than the computer has