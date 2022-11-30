import logging


from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root

# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("737ae4c6ea0522bf69191331e8cfbe9c49ba5d33062df9d853cf5953bf313cda","af861a87d4ba9aa977773696182d33127f20f551c75d8b109745fa447c9674cf",testnet=True, futures=True)
    bitmex = BitmexClient("TvocXJz-oiKjienBoQ2m7oXV", "op5eK0MFEnyVYLKMjQkdHpnVUuCiop50SFpgnEZy_LYf9bBv", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
