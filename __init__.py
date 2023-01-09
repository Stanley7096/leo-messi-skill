from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class LeoMessi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('messi.leo.intent')
    def handle_messi_leo(self, message):
        self.speak_dialog('messi.leo')
    
    @intent_file_handler('club.messi.intent')
    def handle_club_messi(self, message):
        self.speak_dialog('club')
    
    @intent_file_handler('golden.ball.intent')
    def handle_golden_ball(self, message):
        self.speak_dialog('golden.ball')
        
    @intent_handler(IntentBuilder('MessiIntent').require('MessiKeyword'))
    def handle_Messi_Intent(self, message):
    	self.speak_dialog('messi')

def create_skill():
    return LeoMessi()

