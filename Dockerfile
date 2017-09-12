FROM tiangolo/uwsgi-nginx:python2.7

# uwsgi.ini for Django
ENV UWSGI_INI /app/files_uwsgi/djangoapp.ini

# Install all python dependency libs
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy all source files to the container's working directory
#COPY . /app/
COPY files_uwsgi /app/files_uwsgi
COPY configmanager /app/files_django/configmanager
COPY netconfig /app/files_django/netconfig
COPY manage.py /app/files_django/
COPY etc /app/etc
WORKDIR /app/

# Create the log directory for uwsgi and the shared directory for static files
RUN mkdir /var/log/uwsgi /static
COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf
# Collect django static files
RUN python files_django/manage.py collectstatic --noinput


# Port to use with TCP proxy
EXPOSE 6678

# Start uWSGI on container startup
#CMD /usr/local/bin/uwsgi --emperor files_uwsgi --gid www-data --logto /var/log/uwsgi/emperor.log
