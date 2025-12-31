FROM python:3.12-slim-bookworm
LABEL authors="vj"

WORKDIR /app

RUN pip install uv
RUN pip install django

COPY . .
#RUN uv sync
CMD ["source", ".venv/bin/activate"]
#ENTRYPOINT ["python", "app.py"]

EXPOSE 7860