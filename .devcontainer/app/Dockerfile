FROM python:3.9

WORKDIR /tmp/app

#python
ADD requirements.txt .
RUN pip install -r requirements.txt 

#x11-apps
ENV DISPLAY host.docker.internal:0.0
RUN apt-get update -y \
&& apt-get install x11-apps -y \
&& apt-get install xclip -y \
&& apt-get install fonts-ipafont -y \
&& apt-get install locales -y \
&& echo "ja_JP UTF-8" > /etc/locale.gen
RUN locale-gen ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja
