from abc import ABC, abstractmethod
from Bot import Bot


class UserInterface(ABC):
    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def show_message(self, maessage):
        pass

    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_commands(self, commands):
        pass


class ConsoleUI(UserInterface):
    def show_message(self, message):
        print(message)

    def get_user_input(self):
        return input().strip().lower()

    def show_contacts(self, contacts):
        for contact in contacts:
            print(contact)

    def show_commands(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))


class ContactAssistan:
    def __init__(self, ui):
        self.bot = Bot()
        self.ui = ui

    def run(self):
        self.ui.show_message(
            'Hello. I am your contact-assistant. What should I do with your contacts?')
        self.bot.book.load("auto_save")

        while True:
            action = self.ui.get_user_input()

            self.process_action(action)

            if action == 'exit':
                break

    def process_action(self, action):
        if action == 'help':
            self.ui.show_commands(
                ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit'])
            action = self.ui.get_user_input()

        self.bot.handle(action)

        if action in ['add', 'remove', 'edit']:
            self.bot.book.save("auto_save")


if __name__ == "__main__":
    ui = ConsoleUI()
    assistant = ContactAssistan(ui)
    assistant.run()
