# set base image
FROM python:3

# set working folder inside container
WORKDIR /app

# copy requirements 
COPY requirements.txt ./

# install dependendies
RUN pip install --no-cache-dir -r requirements.txt

# copy project to the working folder
COPY . .

# expose port
EXPOSE 8001

# define command to excecute API
CMD ["python", "run.py"]