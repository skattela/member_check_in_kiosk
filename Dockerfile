FROM python:3.10.0a6-slim

COPY . /
COPY mysite mysite

RUN pip install -r requirements.txt

RUN python manage.py makemigrations nfc_time
RUN python manage.py migrate
#ENV webhook_api_token ${webhook_api_token}
#ENV jira_url ${jira_url}
#ENV jira_user ${jira_api_token}
#ENV jira_api_token ${jira_api_token}
#ENV slack_api_token ${slack_api_token}

CMD python manage.py runserver 0.0.0.0:80