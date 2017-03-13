# Simple-Connect-Four-Game

You can play with another person or a semi-intelligent AI. The AI simply looks ahead a few steps (depending on how you initialize it) and calculates the moves it can make by judging the gain from the potential move.

HOW TO PLAY:
You need to first run the connect_four.py in a shell. An example is Python's IDLE.
Once you've ran the file, first initialize your player/AIplayer names (can be any name) and your side (between 'X' or 'O'). 
  To play as a human, an example input would be: 
    playername1 = Player("X") 
  If you want to play against another human (or yourself if you want), don't forget to initialize the 2nd player! 
    playername2 = Player("O")
  However, if you want to play against an AI, an example input would be: 
    playername2 = AIPlayer("O", "LEFT", 3)
      NOTE:
      "X" is the piece you want to use.
      "LEFT" is the tiebreak method. Other options include "RIGHT" or "RANDOM".
      3 is the number of steps you want the AIplayer to look ahead to. (Best keep it 4 or under unless you are patient since it'll take longer for the AI to respond).
Once you have all the players defined, you can finally start playing! All you need to do now is enter into the shell:
  connect_four(playername1, playername2)
The board will then be created and you can play by entering what column you want to put your piece in (or just watch the AIs duke it out depending on how you initialized the players). Enjoy!
 
