
import os, sys

dirpath= os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

from data.code.game import Game


game = Game()
game.run()