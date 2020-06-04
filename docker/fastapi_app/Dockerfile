FROM python:3.8-slim
RUN apt-get update && apt-get install -y gcc python3-dev libssl-dev
EXPOSE 8000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY fastapi_frm /fastapi_frm
CMD ["bash"]
