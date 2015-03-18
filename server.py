import sendwithus
import time

from datetime import datetime, timedelta

SENDWITHUS_API_KEY = 'test_1ed063f355c8f1a7cd2aa9f1ee5c9b2ac36e08af'

def send_messages():
    sender = {u'address': 'admin@antonpravdin.com'}
    email_template_id = 'tem_wS3kQUeLyrWVnMyKjkZWja'
    email_address = 'antons.alternate@gmail.com'
    email_data = {
        'date': 'Right Meow',
        'message_date': 'One minute ago',
        'message': 'ZOMG we be testing,'
    }
    locale = 'en_US'

    api = sendwithus.api(api_key=SENDWITHUS_API_KEY)
    response = api.send(
        sender=sender,
        email_id=email_template_id,
        recipient={u'address': email_address},
        email_data=email_data,
        email_version_name=locale
    )

    print response
    print response.content


def parse_messages():
    pass

SEND_TIME = 18
MIN_SECONDS = 5

if __name__ == '__main__':
    next_run = datetime.now()
    last_run = next_run
    while True:
        if datetime.now() > next_run:
            send_messages()

            parse_messages()

            last_run = datetime.now()
            next_run = datetime.now().replace(hour=SEND_TIME, minute=0, second=0) + timedelta(days=1)

        time_diff = next_run - datetime.now()
        time_diff_seconds = max(time_diff.seconds, MIN_SECONDS)
        time.sleep(time_diff_seconds)
