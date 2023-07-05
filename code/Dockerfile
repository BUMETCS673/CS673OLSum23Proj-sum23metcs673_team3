FROM ubuntu:kinetic
RUN apt update
RUN apt -y upgrade
RUN apt install -y python3 && apt install -y python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install tzdata
RUN pip3 install gunicorn
COPY ./Project ./app
WORKDIR app
EXPOSE 8000

CMD ["gunicorn","-b 0.0.0.0:8000","calorietracker.wsgi"]

