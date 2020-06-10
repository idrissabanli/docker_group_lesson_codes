FROM ubuntu:16.04

RUN apt -y update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install jupyter

CMD "jupyter" "notebook" "--ip" "0.0.0.0" "--port" "8888" "--allow-root" "--NotebookApp.token='idris'" "--NotebookApp.password=''"