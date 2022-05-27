FROM ubuntu:20.04

ARG arg="windows"

RUN if [ "$arg" = "windows" ] ; then \
	export ENV DISPLAY=host.docker.internal:0.0 \
	export ENV PULSE_SERVER=tcp:host.docker.internal:4713 ; \
	else echo you are using $arg ; \
fi

COPY asound.conf /etc/asound.conf
COPY . .

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC  apt-get -y install python3 python3-pip alsa-base libsdl2-2.0 libsdl2-dev pulseaudio
RUN pip install pygame pygame-widgets

CMD ["python3", "./main.py"]
