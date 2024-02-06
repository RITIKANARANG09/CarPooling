import datetime
import re
import re
from src.helper.logs import Log
from src.Exceptions.app_decorators import loop
from src.helper.message import Message
from src.config.app_config import AppConfig
import logging
from datetime import datetime

logger = logging.getLogger("validations")
class Validations:


        @staticmethod
        @loop
        def input_username() -> str:
            username = input(Message.username).lower()
            if re.match(AppConfig.REGEX_USERNAME, username):
                return username
            print(Message.wrong_input)
            logger.info(Log.LOG_INVALID_INPUT)

        # @staticmethod
        # @loop
        # def input_password() -> str:
        #     password = maskpass.askpass(PromptConfig.PASSWORD_PROMPT).strip()
        #     if re.match(AppConfig.REGEX_PASSWORD, password):
        #         return password
        #     print("Invalid input...")
        #     logger.info(LogsConfig.LOG_INVALID_INPUT)

        @staticmethod
        @loop
        def input_name(name_prompt) -> str:
            name = input(name_prompt)
            if re.match(AppConfig.REGEX_NAME, name):
                return name
            print(Message.wrong_input)
            logger.info(Log.LOG_INVALID_INPUT)

        @staticmethod
        @loop
        def input_number() -> str:
            number = input(Message.phone_number)
            if re.match(AppConfig.REGEX_NUMBER, number):
                return number
            print(Message.wrong_input)
            logger.info(Log.LOG_INVALID_INPUT)

        @staticmethod
        @loop
        def input_time() -> str:
            time = input(Message.time)
            if re.match(AppConfig.REGEX_TIME, time):
                return time
            print(Message.wrong_input)
            logger.info(Log.LOG_INVALID_INPUT)

        @staticmethod
        @loop
        def input_date() -> str:
            date = input(Message.date)
            if re.match(AppConfig.REGEX_DATE, date) and Validations.current_date_validation(date):
                return date
            print(Message.wrong_input)
            logger.info(Log.LOG_INVALID_INPUT)


        @staticmethod
        @loop
        def current_date_validation(date) -> str:
            if date>=datetime.now().date():
                return date
            return ""