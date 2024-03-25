FROM python:3.12-alpine3.19

COPY crm_partners_files /crm_partners_files
COPY requirements.txt /temp/requirements.txt
WORKDIR /crm_partners_files
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password crm_user
RUN chown crm_user:crm_user -R /crm_partners_files/



USER crm_user