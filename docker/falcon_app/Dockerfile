FROM python:3.8-slim
RUN apt-get update && apt-get install -y gcc python3-dev libssl-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY falcon_frm /falcon_frm
CMD ["bash"]
