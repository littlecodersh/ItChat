FROM python:2-alpine
ADD . /opt
WORKDIR /opt
RUN pip install requests
RUN python setup.py develop
CMD ["python","demo.py"]
