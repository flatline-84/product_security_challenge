FROM python:alpine3.8
COPY project/ /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV PORT "5001"
ENV DEBUG "True"

EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]