from lib.network import get_tor_address
from consts import light_font

import pygame


class infoSection():
    def __init__(self, parent):
        self.title = "Info section"
        self.data = "Data"
        self.font = False
        self.width = 1
        self.parent = parent
        self.dataFunction = "return"

    def updateData(self):
        btc = self.parent.btc_rpc
        lnd = self.parent.lnd_grpc
        self.data = eval(self.dataFunction)

    def getData(self):
        self.updateData()
        return (self.title, self.data, self.ownRow, self.font)

class InfoSectionsList():

    def __init__(self, btc, lnd):
        # Init RPC connections
        self.btc_rpc = btc
        self.lnd_grpc = lnd

# Disabled to match Umbrel's security requirements
'''
    class torURL(infoSection):
        def __init__(self, parent):
            infoSection.__init__(self, parent)
            self.title = "Tor URL"
            self.data = "Loading..."
            self.font = pygame.freetype.Font(light_font, 22)
            self.width = 3
            self.dataFunction = "get_tor_address()"
'''

    class maxSend(infoSection):
        def __init__(self, parent):
            infoSection.__init__(self, parent)
            self.title = "Max Send"
            self.data = "Loading..."
            self.dataFunction = "lnd.get_max_send()"

    class maxReceive(infoSection):
        def __init__(self, parent):
            infoSection.__init__(self, parent)
            self.title = "Max Recieve"
            self.data = "Loading..."
            self.parent = parent
            self.dataFunction = "lnd.get_max_receive()"

    class activeChannels(infoSection):
        def __init__(self, parent):
            infoSection.__init__(self, parent)
            self.title = "Active Channels"
            self.data = "Loading..."
            self.dataFunction = "lnd.get_active_channels()"

    class forward(infoSection):
        def __init__(self, parent):
            infoSection.__init__(self, parent)
            self.title = "24H Forwards"
            self.data = "Loading..."
            self.dataFunction = "lnd.get_forwarding_events()"

    class syncProgress(infoSection):
        def __init__(self, parent):
            infoSection.__init__(self, parent)
            self.title = "Sync progress"
            self.data = "Loading..."
            self.dataFunction = "str(btc.get_sync_progress()) + '%'"
