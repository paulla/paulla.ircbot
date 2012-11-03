#! /usr/bin/env python
# -*- coding: utf-8 -*

"""
Simple script to test to irc module.
"""


import irc.bot

class Botanik(irc.bot.SingleServerIRCBot):
    def __init__(self, channel="#paulla", nickname="botanik", server="irc.freenode.net", port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_welcome(self, c, e):
        c.join(self.channel)
        c.privmsg(self.channel, u"cyp c'est pour quand le prochain sprint ?")
        c.privmsg(self.channel, u"cyp j'ai vraiment l'impression de mouler !")
        lost_masters = ['solevis', 'Llew', 'Mika64']
        for master in lost_masters:
            c.privmsg(self.channel, u"Mon maître %s m'a abandonné" % master)
        c.privmsg(self.channel, u"Mon maître Kasba m'a trouvé")

def main():
    """Main function."""
    bot = Botanik()
    bot.start()
    #import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
