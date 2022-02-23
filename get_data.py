%matplotlib

import argparse
import time
import numpy as np

import brainflow
from brainflow.board_shim import BoardShim, BoardIds, BrainFlowInputParams
from brainflow.data_filter import DataFilter

import matplotlib.pyplot as plt
from datetime import datetime
import json

# display development messages
#BoardShim.enable_dev_board_logger()

# CONSTANTS: modify each recording
note = "Patient's eyes open, looking at laptop. Device on the floor, 1-metre away from laptop."
channel_name = 'Fp1'

# setup for my board
Id = BoardIds.GANGLION_BOARD.value
sfreq = BoardShim.get_sampling_rate(Id)
params = BrainFlowInputParams()
params.serial_port = 'COM3'
board = BoardShim(Id, params)

# get data from board
board.prepare_session()
board.start_stream()
time.sleep(30)
# data = board.get_current_board_data (256) # get latest 256 packages or less
dataRaw = board.get_board_data()  # get all data but remove it from internal buffer

# clean-up
board.stop_stream()
board.release_session()

# write a JSON file
data = dataRaw[1] # Ganglion's EEG channels are [1: 4]
dateTime = datetime.today().strftime("20%y-%m-%d_%H-%M")
fileName = 'data-eeg-ganglion_' + dateTime + '.json'
file = open(fileName, "w")
dataList = data.tolist()
JSON = {"note": note, channel_name: dataList}
json.dump(JSON, file)
file.close()

print("data saved.")

fig, ax = plt.subplots()
ax.plot(data)
