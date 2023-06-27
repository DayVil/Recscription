# Rescription

Rescription is a simple script to transcribe data received from the mricrophone to text.

## Use
Start the script via the command line. 
- Use ``python run.py --help`` to get the list of all possible commands.  
- Start by checking your audio devices via ``python run.py -l``.  
- Select your device and run the script via ``python run.py -d <DEVICE>``. This will run the transcriber with the basic model. If you want to select a better model, use ``python run.py -d <DEVICE> -m [tiny, base, small, medium, large]``. Be aware that using the bigger models requires an NVIDIA GPU.  

Once the script starts, you can start speaking. By pressing ``CTRL + C`` the script will be interrupted, and after some time, a file called ``transcription.txt`` will be created in your current working directory.

## Help


## Requirements  

- ffmpeg  
- Python3.10 or lower
- the requirements from the requirements file
