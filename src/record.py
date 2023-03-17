import soundfile as sf
import sounddevice as sd
import tempfile
import sys
import queue

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(f"Error: {status}", file=sys.stderr)
    q.put(indata.copy())


def start_recording(samplerate: int, device: int | str | None, channels: int, output_dir: str, delete=True):

    if not delete:
        tempfile.tempdir = output_dir
    tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=delete)

    try:
        with sf.SoundFile(tmp_file, "x", samplerate, channels) as file:
            with sd.InputStream(samplerate=samplerate, device=device, channels=channels, callback=callback):
                print("#" * 80)
                print("Press Ctrl+C to stop the recording")
                print("#" * 80)

                while True:
                    file.write(q.get())

    except KeyboardInterrupt:
        print("\nRecording finished: " + repr(tmp_file.name))
        return tmp_file

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return tmp_file
