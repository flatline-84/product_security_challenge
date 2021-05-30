FROM ubuntu:20.04
COPY project/ /app
WORKDIR /app

# To prevent tzdata ruining the build process
ENV TZ=Australia/Melbourne
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Split up these lines so Docker can cache them
RUN apt-get update && \
    apt-get install -y --no-install-recommends \ 
    python3 python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT "5001"
ENV DEBUG "True"
ENV HOST "0.0.0.0"

EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD ["main.py"]