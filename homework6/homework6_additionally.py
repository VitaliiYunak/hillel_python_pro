# Реалізація системи відправки повідомлень, яка приймає список адаптерів і відправляє одне і те ж
# повідомлення через усі доступні сервіси.
# Додана обробка помилок для кожного сервісу, якщо відправка повідомлення не вдалася.


class MessageSender:
    def send_message(self, message: str):
        pass


# Існуючі класи для відправки повідомлень
class SMSService:
    def send_sms(self, phone_number, message):
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    def send_email(self, email_address, message):
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    def send_push(self, device_id, message):
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


# Адаптери
class SMSAdapter(MessageSender):
    def __init__(self, sms_service, phone_number):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Не вдалося відправити SMS: {e}")


class EmailAdapter(MessageSender):
    def __init__(self, email_service, email_address):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Не вдалося відправити Email: {e}")


class PushAdapter(MessageSender):
    def __init__(self, push_service, device_id):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Не вдалося відправити Push-повідомлення: {e}")


if __name__ == "__main__":
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()

    sms_adapter = SMSAdapter(sms_service, "+380123456789")
    email_adapter = EmailAdapter(email_service, "user@example.com")
    push_adapter = PushAdapter(push_service, "device123")

    # Відправка повідомлень через різні сервіси за допомогою адаптерів
    message = "Привіт! Це тестове повідомлення."

    # Відправляємо повідомлення через усі адаптери
    for adapter in [sms_adapter, email_adapter, push_adapter]:
        adapter.send_message(message)
