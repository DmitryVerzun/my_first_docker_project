#pulling python image (alpine because i'm running out of memory)
#FROM python:3.11-rc-alpine  sadly didn't work
FROM python:3.10.2-slim-bullseye

#setting work directory
WORKDIR /usr/src/app
#RUN pwd
#RUN ls

#environmental variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#installing dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app/
#StackOverflow-inspired fixes for pg_config and greenlet problems :)
RUN  python3 -m pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
#copy project
COPY . /usr/src/app/

#CMD ["which", "bash"]
#CMD ["/usr/src/app/entrypoint.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
#ENTRYPOINT ["entrypoint]