import os.path
import platform
import shutil
import subprocess
import sys
import urllib.request
from urllib import request
from zipfile import ZipFile

RESTART_QUEUE = False
MODEL_PATH = os.path.join(os.path.abspath(''), 'Model')


# NEED TO IMPLEMENT (maybe) SoX


# noinspection PyBroadException
def internet_on():
    try:
        request.urlopen('https://google.com', timeout=4)
        return True
    except Exception:
        return False


# noinspection PyBroadException
def dependency_check_rtl():
    if internet_on():
        PLATFORM = platform.system()
        if PLATFORM == 'Windows':
            home_directory = os.path.expanduser('~')
            # check if RTL-SDR exists or not
            try:
                subprocess.Popen('rtl_fm -h')
                sys.stdout.write('RTL-SDR is installed\n')
            except Exception:
                if not os.path.exists(os.path.abspath('') + '\\Temp'):
                    os.makedirs(os.path.abspath('') + '\\Temp')
                sys.stdout.write("Downloading RTL-SDR Windows Binary ZIP File\n")
                urllib.request.urlretrieve(
                    url="https://github.com/rtlsdrblog/rtl-sdr-blog/releases/download/1.01/Release.zip",
                    filename=os.path.abspath('') + '\\Temp\\Release.zip')
                if not os.path.exists(home_directory + '\\rtl-sdr-release'):
                    os.makedirs(home_directory + '\\rtl-sdr-release')
                with ZipFile(os.path.abspath('') + '\\Temp\\Release.zip', 'r') as zObject:
                    zObject.extractall(path=home_directory + '\\rtl-sdr-release')
                p = subprocess.Popen(["powershell.exe", '$PATH = [Environment]::GetEnvironmentVariable("PATH", '
                                                        '"User"); $new_path = "' + home_directory +
                                      '\\rtl-sdr-release\\"; if( $PATH -notlike "*"+$new_path+"*" ){ ['
                                      'Environment]::SetEnvironmentVariable("PATH", "$PATH;$new_path", '
                                      '"User")}'])
                p.communicate()
                shutil.rmtree(os.path.abspath('') + '\\Temp')
                global RESTART_QUEUE
                RESTART_QUEUE = True
        elif PLATFORM == 'Linux':
            sys.stdout.write(PLATFORM)
            try:
                os.system('sudo apt install rtl-sdr gqrx-sdr')
                RESTART_QUEUE = True
            except Exception as e:
                sys.stdout.write(str(e) + '\n')
        elif PLATFORM == 'MacOS':
            sys.stdout.write(PLATFORM)
        else:
            sys.stdout.write('UNEXPECTED ERROR')
    else:
        sys.stdout.write('RTL-SDR DEPENDENCY CHECK ERROR: This device seems disconnected from the internet. '
                         'Dependency checks cannot be conducted. This may cause unexpected program '
                         'behavior. Please connect your device to the internet as soon as possible to '
                         'ensure all dependencies are properly installed. \n')


# noinspection PyBroadException
def dependency_check_ffmpeg():
    if internet_on():
        PLATFORM = platform.system()
        if PLATFORM == 'Windows':
            # sys.stdout.write(PLATFORM + '\n')
            home_directory = os.path.expanduser('~')
            # check if FFMPEG exists or not
            try:
                subprocess.Popen('ffmpeg -h')
                sys.stdout.write('FFMPEG is installed\n')
            except Exception:
                if not os.path.exists(os.path.abspath('') + '\\Temp'):
                    os.makedirs(os.path.abspath('') + '\\Temp')
                sys.stdout.write("Downloading FFMPEG Windows Binary ZIP File\n")
                urllib.request.urlretrieve(
                    url="https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64"
                        "-gpl.zip",
                    filename=os.path.abspath('') + '\\Temp\\ffmpeg-master-latest-win64-gpl.zip')
                # if not os.path.exists(home_directory + '\\ffmpeg'):
                #     os.makedirs(home_directory + '\\ffmpeg')
                with ZipFile(os.path.abspath('') + '\\Temp\\ffmpeg-master-latest-win64-gpl.zip', 'r') as zObject:
                    zObject.extractall(path=home_directory)
                os.rename(home_directory + '\\ffmpeg-master-latest-win64-gpl', home_directory + '\\ffmpeg')
                p = subprocess.Popen(["powershell.exe", '$PATH = [Environment]::GetEnvironmentVariable("PATH", '
                                                        '"User"); $new_path = "' + home_directory +
                                      '\\ffmpeg\\bin\\"; if( $PATH -notlike "*"+$new_path+"*" ){ ['
                                      'Environment]::SetEnvironmentVariable("PATH", "$PATH;$new_path", '
                                      '"User")}'])
                p.communicate()
                # os.environ["PATH"] += os.pathsep + home_directory + '\\ffmpeg\\bin;'
                shutil.rmtree(os.path.abspath('') + '\\Temp')
                global RESTART_QUEUE
                RESTART_QUEUE = True
        elif PLATFORM == 'Linux':
            sys.stdout.write(PLATFORM)
            try:
                os.system('sudo apt install ffmpeg')
                RESTART_QUEUE = True
            except Exception as e:
                sys.stdout.write(str(e) + '\n')
        elif PLATFORM == 'MacOS':
            sys.stdout.write(PLATFORM)
        else:
            sys.stdout.write('UNEXPECTED ERROR')
    else:
        sys.stdout.write('FFMPEG DEPENDENCY CHECK ERROR: This device seems disconnected from the internet. '
                         'Dependency checks cannot be conducted. This may cause unexpected program '
                         'behavior. Please connect your device to the internet as soon as possible to '
                         'ensure all dependencies are properly installed. \n')


# noinspection PyBroadException
def dependency_check_multimon():
    if internet_on():
        PLATFORM = platform.system()
        if PLATFORM == 'Windows':
            # sys.stdout.write(PLATFORM + '\n')
            home_directory = os.path.expanduser('~')
            # check if Multimon-NG exists or not
            try:
                subprocess.Popen('multimon-ng -h')
                sys.stdout.write('Multimon-NG is installed')
            except Exception:
                if not os.path.exists(os.path.abspath('') + '\\Temp'):
                    os.makedirs(os.path.abspath('') + '\\Temp')
                sys.stdout.write("Downloading Multimon-NG Windows Binary ZIP File\n")
                urllib.request.urlretrieve(
                    url="https://github.com/cuppa-joe/multimon-ng/releases/download/WIN32-0415/multimon-ng-WIN32.zip",
                    filename=os.path.abspath('') + '\\Temp\\multimon-ng-WIN32.zip')
                if not os.path.exists(home_directory + '\\multimon-ng'):
                    os.makedirs(home_directory + '\\multimon-ng')
                with ZipFile(os.path.abspath('') + '\\Temp\\multimon-ng-WIN32.zip', 'r') as zObject:
                    zObject.extractall(path=home_directory + '\\multimon-ng')
                p = subprocess.Popen(["powershell.exe", '$PATH = [Environment]::GetEnvironmentVariable("PATH", '
                                                        '"User"); $new_path = "' + home_directory +
                                      '\\multimon-ng\\"; if( $PATH -notlike "*"+$new_path+"*" ){ ['
                                      'Environment]::SetEnvironmentVariable("PATH", "$PATH;$new_path", '
                                      '"User")}'])
                p.communicate()
                shutil.rmtree(os.path.abspath('') + '\\Temp')
                global RESTART_QUEUE
                RESTART_QUEUE = True
        elif PLATFORM == 'Linux':
            sys.stdout.write(PLATFORM)
            try:
                os.system('sudo apt install multimon-ng')
                RESTART_QUEUE = True
            except Exception as e:
                sys.stdout.write(str(e) + '\n')
        elif PLATFORM == 'MacOS':
            sys.stdout.write(PLATFORM)
        else:
            sys.stdout.write('UNEXPECTED ERROR')
    else:
        sys.stdout.write('MULTIMON-NG DEPENDENCY CHECK ERROR: This device seems disconnected from the internet. '
                         'Dependency checks cannot be conducted. This may cause unexpected program '
                         'behavior. Please connect your device to the internet as soon as possible to '
                         'ensure all dependencies are properly installed. \n')


def dependency_check_model(MODEL_NAME):
    if internet_on():
        if not os.path.exists(os.path.join(MODEL_PATH, MODEL_NAME)):
            sys.stdout.write("Model path does not exist. Creating folders and downloading files. \n")
            os.makedirs(os.path.join(MODEL_PATH, MODEL_NAME))
        if not os.path.exists(os.path.join(MODEL_PATH, MODEL_NAME, 'model.bin')):
            sys.stdout.write("Downloading model.bin for model " + MODEL_NAME + "\n")
            urllib.request.urlretrieve(
                url="https://huggingface.co/guillaumekln/faster-whisper-" + MODEL_NAME + "/resolve/main/model.bin",
                filename=os.path.join(MODEL_PATH, MODEL_NAME, 'model.bin'))
        if not os.path.exists(os.path.join(MODEL_PATH, MODEL_NAME, 'config.json')):
            sys.stdout.write("Downloading config.json for model " + MODEL_NAME + "\n")
            urllib.request.urlretrieve(
                url="https://huggingface.co/guillaumekln/faster-whisper-" + MODEL_NAME + "/resolve/main/config.json",
                filename=os.path.join(MODEL_PATH, MODEL_NAME, 'config.json'))
        if not os.path.exists(os.path.join(MODEL_PATH, MODEL_NAME, 'tokenizer.json')):
            sys.stdout.write("Downloading tokenizer.json for model " + MODEL_NAME + "\n")
            urllib.request.urlretrieve(
                url="https://huggingface.co/guillaumekln/faster-whisper-" + MODEL_NAME + "/resolve/main/tokenizer.json",
                filename=os.path.join(MODEL_PATH, MODEL_NAME, 'tokenizer.json'))
        if not os.path.exists(os.path.join(MODEL_PATH, MODEL_NAME, 'vocabulary.txt')):
            sys.stdout.write("Downloading vocabulary.txt for model " + MODEL_NAME + "\n")
            urllib.request.urlretrieve(
                url="https://huggingface.co/guillaumekln/faster-whisper-" + MODEL_NAME + "/resolve/main/vocabulary.txt",
                filename=os.path.join(MODEL_PATH, MODEL_NAME, 'vocabulary.txt'))
        sys.stdout.write('All dependencies are installed and up to date for model ' + MODEL_NAME + ' \n')
    else:
        sys.stdout.write(MODEL_NAME + ' DEPENDENCY CHECK ERROR: This device seems disconnected from the internet. '
                                      'Dependency checks cannot be conducted. This may cause unexpected program '
                                      'behavior. Please connect your device to the internet as soon as possible to '
                                      'ensure all dependencies are properly installed. \n')


if platform.system() == 'Linux':
    os.system('sudo apt install xterm')
dependency_check_model('small')
dependency_check_model('medium')
dependency_check_model('large-v2')
dependency_check_model('small.en')
dependency_check_model('medium.en')
dependency_check_multimon()
dependency_check_ffmpeg()
dependency_check_rtl()
# if RESTART_QUEUE:
#     # NEED OS CHECK HERE
#     sys.stdout.write('One or more of the dependencies have been successfully installed! However, in order for '
#                      'them to work properly, you will need to restart your system. Would you like to restart '
#                      'now? (Y/N): ')
#     CHOICE = sys.stdin.readline()
#     CHOICE = CHOICE.replace('\n', '')
#     if CHOICE.capitalize() == 'Y':
#         os.system("shutdown /r /t 0")
#         exit()
#     else:
#         exit()
# else:
#     exit(23)
