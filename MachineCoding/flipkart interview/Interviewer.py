class Interviewer(object):
    def __init__(self, name, interview_type, yoe, slots):
        self.name = name
        self.interview_type = interview_type
        self.yoe = yoe
        self.slots = slots
        self.interview_taken = 0

    def __str__(self):
        return f"Interviewer Name: {self.name}, Interview type: {self.interview_type}," \
               f"Years of Experience: {self.yoe}, Available Slots: {self.slots}"
