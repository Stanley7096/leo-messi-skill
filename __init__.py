from mycroft import MycroftSkill, intent_file_handler


class LeoMessi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('messi.leo.intent')
    def handle_messi_leo(self, message):
        self.speak_dialog('messi.leo')


def create_skill():
    return LeoMessi()

