from dexy.filter import DexyFilter

class CustomFilter(DexyFilter):
    aliases = ['custom']

    def process_text(self, input_text):
        return "This is the custom filter output.\n"
