from flask import Flask, send_from_directory
from config import get_config_files_dir
import os

app = Flask(__name__)

#######################################################################
# Check that the directory for serving the files has been configured
#######################################################################
files_dir = get_config_files_dir()


@app.route('/')
def index():
    return ''.join('{}\n'.format(x) for x in os.listdir(files_dir))


@app.route('/<path:filename>')
def download(filename):
    return send_from_directory(directory=files_dir, filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')