import argparse
import time
import numpy as np

import brainflow
from brainflow.board_shim import BoardShim, BoardIds, BrainFlowInputParams
from brainflow.data_filter import DataFilter

import matplotlib.pyplot as plt
from datetime import datetime
from pyedflib import highlevel

# display development messages
#BoardShim.enable_dev_board_logger()

# setup for my board
channel_names = ['Fp1']
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

# write an edf file
signals = [dataRaw[1]] # Ganglion's EEG channels are [1: 4]
signal_headers = highlevel.make_signal_headers(
    channel_names,
    sample_frequency=sfreq,
    physical_min=-600.0, # changed to ensure no data clipping occurs
    physical_max=600.0)
comments = "Comment."
header = highlevel.make_header(patientname='Nick Howlett', recording_additional=comments)
dateTime = datetime.today().strftime("20%y-%m-%d_%H-%M-%S")
file = 'data-eeg-ganglion_' + dateTime + '.edf'
highlevel.write_edf(file, signals, signal_headers, header)

print("data saved.")
