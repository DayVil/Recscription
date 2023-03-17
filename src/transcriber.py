import whisper


def start_transcribing(file, model, output_dir):
    model = whisper.load_model(model)
    result = model.transcribe(file)

    with open(output_dir + "/transcription.txt", "w") as f:
        print(result["text"], file=f)
