from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey!! How its going buddy?"

    if user_message in ("who are you ?", "Introduce yourself", "Do I know you ?", "Whats your good name ?"):
        return "I'm Abvitecbot, a user friendly bot. How may i help you?"

    if user_message in ("whats the time?", "time", "how long it has been?",):
        now = datetime.now()
        date_time = now.strframe("%d/%m/%y", "%H:%M:%S")

        return str(date_time)

    return "I do not understand what you mean bruh."
