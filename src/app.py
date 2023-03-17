from typing import Tuple
import sounddevice as sd
import argparse
from src.record import start_recording
from src.transcriber import start_transcribing
import sys
import os
from datetime import datetime

import numpy
assert numpy  # avoid "imported but unused" message (W0611)

# DEFAULTS
CHANNELS = 2


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


def init_args() -> Tuple[argparse.Namespace, argparse.ArgumentParser]:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all the audio devices and exit')

    parser.add_argument('-d', '--device', type=int_or_str,
                        help='The audio device to use')
    parser.add_argument('-m', '--model', type=str, choices=['tiny', 'base', 'small', 'medium', 'large'],
                        default="small", help='The model to use')
    parser.add_argument('--keep', action='store_false', default=True,
                        help='Keep the temporary file after the recording is finished')

    args = parser.parse_args()
    return args, parser


def run(output_dir: str):
    args, parser = init_args()
    if args.list:
        print(sd.query_devices())
        parser.exit(0)

    device = args.device

    # Getting default sample rate
    device_info = sd.query_devices(args.device, 'input')
    sample_rate = int(device_info['default_samplerate'])

    # Setting up output directory
    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    to_output = output_dir + "/" + date_time
    os.makedirs(to_output, exist_ok=True)

    # Starting recording
    file = start_recording(sample_rate, device, CHANNELS,
                           to_output, delete=args.keep)
    if file is None:
        print("Recording failed", file=sys.stderr)
        parser.exit(1)

    # Starting transcription
    start_transcribing(file.name, args.model, to_output)

    file.close()
    parser.exit(0)
