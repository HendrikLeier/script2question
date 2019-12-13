FROM tiangolo/python-machine-learning:python3.6

RUN apt-get update
RUN apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
    flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev

COPY requirements.txt /tmp/

RUN pip install -U pip && \
    pip install -r /tmp/requirements.txt

COPY ./src/ /app/
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
