class Interviewee(object):
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots
        self.interview_count = 0

    def __str__(self):
        return f"Candidate Name: {self.name}, Availability: {self.slots}, Interview count: {self.interview_count}"
