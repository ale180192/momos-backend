FROM python
EXPOSE 80
EXPOSE 8000
RUN mkdir /code
RUN apt-get update
RUN apt install -y nginx && apt install -y ufw
RUN ufw allow 'Nginx HTTP'
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/
RUN mkdir /usr/share/nginx/html/static
COPY /static/ /usr/share/nginx/html/static
RUN rm -f /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN pip install -r requirements.txt
COPY init.sh /code/init.sh
ENTRYPOINT ["sh","/code/init.sh"]