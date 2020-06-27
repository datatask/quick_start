FROM google/cloud-sdk:261.0.0-slim

RUN apt update && apt install wget && \
    wget -q https://repo.continuum.io/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /opt/miniconda && \
    rm ~/miniconda.sh

RUN /opt/miniconda/bin/pip install --upgrade pip Flask

RUN mkdir /code

COPY hello_world.py /code/

CMD [ "/opt/miniconda/bin/python", "/code/hello_world.py" ]