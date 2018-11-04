from flask import Flask, send_from_directory
from config import get_config_files_dir, get_config_default_file
import os

app = Flask(__name__)

#######################################################################
# Check that the directory for serving the files has been configured
#######################################################################
files_dir = get_config_files_dir()
default_file = get_config_default_file()

def send_file(filename):
    return send_from_directory(directory=files_dir, filename=filename)


@app.route('/')
def index():
    if default_file is None:
        return ''.join('{}\n'.format(x) for x in os.listdir(files_dir))
    return send_file(default_file)

@app.route('/<path:filename>')
def download(filename):
    return send_file(filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

