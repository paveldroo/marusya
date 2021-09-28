registred_states = {}


def get_state(state_id):
    return registred_states[state_id]


class Transition:
    def __init__(self, to_id, synonims):
        self.to_id = to_id
        self.synonims = synonims

    def must_go(self, user_text):
        return user_text in self.synonims

    def get_dest_id(self):
        return self.to_id


class State:
    def __init__(self, id, text, transitions, default_transition):
        self.id = id
        self.text = text
        self.transitions = transitions
        self.default_transition = default_transition

    def get_next_state(self, user_input):
        for transition in self.transitions:
            if transition.must_go(user_input):
                return get_state(transition.to_id)

        return get_state(self.default_transition)

    def register(self):
        global registred_states
        registred_states[self.id] = self


def init():
    global root_state_id
    State('100', 'Привет, вы хотите отправиться в космос?', [], None).register()

    root_state_id = '100'


init()
