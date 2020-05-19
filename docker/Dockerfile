FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y jupyter

CMD [ "jupyter" "notebook" "--port" "8888" "--ip" "0.0.0.0" "--NotebookApp.token=''" "--NotebookApp.password=''" "--allow-root"  ]