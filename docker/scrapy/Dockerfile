FROM python:3.6
ENV TZ=Europe/Istanbul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip
RUN pip install scrapy==2.5
RUN pip install ipython
RUN pip install scrapy_proxies