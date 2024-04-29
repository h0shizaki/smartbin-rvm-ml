FROM continuumio/miniconda:latest
WORKDIR /my_app
ADD . /my_app
# Install gcc as it is missing in continuumio/miniconda:latest
RUN apt-get update && apt-get -y install gcc
RUN conda env create -f environment.yml
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
# Make sure the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"
EXPOSE 5000
# The code to run when container is started:
ENTRYPOINT ["conda", "run", "-n", "smart-bin-rvm", "python", "app.py"]