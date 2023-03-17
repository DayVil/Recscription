from src import app
import os

OUTPUTDIR = "./output"

if __name__ == '__main__':
    os.makedirs(OUTPUTDIR, exist_ok=True)
    app.run(OUTPUTDIR)
