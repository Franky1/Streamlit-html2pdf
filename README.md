# Streamlit-html2pdf

Streamlit test project for html2pdf conversion

> WORK IN PROGRESS - NOT FINISHED - DO NOT USE YET

## ToDo

- [ ] Test it in Docker environment
- [ ] Test it in Streamlit sharing
- [ ] Try other libraries

## Resources

Some links to articles and different libraries for html2pdf conversion in Python.

- wkhtmltopdf -> <https://wkhtmltopdf.org/>
- weasyprint -> <https://weasyprint.org/>
- xhtml2pdf -> <https://github.com/xhtml2pdf/xhtml2pdf>
- <https://gearheart.io/blog/how-generate-pdf-files-python-xhtml2pdf-weasyprint-or-unoconv/>
- <https://elements.heroku.com/buildpacks/jazzcore/python-pdfkit>
- <https://github.com/JazzCore/python-pdfkit>

## Docker Runtime

The provided `Dockerfile` tries to mimic the Streamlit Sharing runtime.

Pulling the base image from Docker Hub

```shell
docker pull python:3.7.10-slim
```

Run and shell into base python container

```shell
docker run -it --name py3710slim python:3.7.10-slim /bin/bash
docker run -ti --rm python:3.7.10-slim /bin/bash
```

Build local custom Docker Image from Dockerfile

```shell
docker build -t html2pdf:latest .
docker run -ti --name selenium --rm html2pdf:latest /bin/bash
```

Run custom Docker Container

```shell
docker run -ti -p 8501:8501 --rm html2pdf:latest
docker run -ti -p 8501:8501 -v $(pwd):/app --rm html2pdf:latest  # linux
docker run -ti -p 8501:8501 -v ${pwd}:/app --rm html2pdf:latest  # powershell
docker run -ti -p 8501:8501 -v %cd%:/app --rm html2pdf:latest  # cmd.exe
```

Open the local Streamlit application

<http://localhost:8501> for the local or dockerized application
