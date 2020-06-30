FROM google/cloud-sdk:235.0.0-slim

RUN mkdir /code
RUN pip install google-cloud-bigquery
RUN pip install google-cloud-storage
RUN pip install pandas

COPY ./Extract.py /code/
COPY ./cred.json /code/

CMD python /code/Extract.py