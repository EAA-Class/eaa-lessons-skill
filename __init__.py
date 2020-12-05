from mycroft import MycroftSkill, intent_file_handler


class EaaLessons(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lessons.eaa.intent')
    def handle_lessons_eaa(self, message):
        self.speak_dialog('lessons.eaa')


def create_skill():
    return EaaLessons()

