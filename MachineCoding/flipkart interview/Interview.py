from Interviewee import Interviewee
from Interviewer import Interviewer


class Interview(object):
    def __init__(self):
        self.interviewees = []
        self.interviewers = []
        self.mc = dict()
        self.psds = dict()
        self.allocation = dict()

    def add_to_slots(self, user, slots, mc=False, psds=False):
        if mc:
            for slot in slots:
                if slot not in self.mc:
                    self.mc[slot] = []
                self.mc[slot].append(user)
        elif psds:
            for slot in slots:
                if slot not in self.psds:
                    self.psds[slot] = []
                self.psds[slot].append(user)

    def register_interviewer(self, name, interview_type, yoe, slots):
        try:
            user = Interviewer(name, interview_type, yoe, slots)
            for interviewer in self.interviewers:
                if interviewer.name == name:
                    raise Exception(f"Interviewer {name} is already registered")
            if len(interview_type) == 0 or len(interview_type) > 2:
                raise Exception(f"Interview Type for Interviewer {name} can only contain MC or PSDS")
            for interview in interview_type:
                 if interview not in ["MC", "PSDS"]:
                    raise Exception(f"Interview Type for Interviewer {name} can only contain MC or PSDS")
            self.interviewers.append(user)
            for interview in interview_type:
                if interview == "MC":
                    self.add_to_slots(user, slots, mc=True)
                elif interview == "PSDS":
                    self.add_to_slots(user, slots, psds=True)

        except Exception as e:
            print(str(e))

    def register_interviewee(self, name, slots):
        try:
            user = Interviewee(name, slots)
            for interviewee in self.interviewees:
                if interviewee.name == name:
                    raise Exception(f"Interviewee {name} is already registered")
            self.interviewees.append(user)
        except Exception as e:
            print(str(e))

    def allocate_interviews(self):
        for candidate in self.interviewees:
            self.allocation[candidate.name] = dict()
            mc_interviewer = None
            psds_interviewer = None
            # MC
            allocate = False
            slots = list(candidate.slots)
            for slot in slots:
                if slot in self.mc and len(self.mc[slot]) > 0:
                    # for interviewer in self.mc[slot]:
                    mc_interviewer = self.mc[slot][0].name
                    self.allocation[candidate.name]["MC"] = [candidate.name, "MC", mc_interviewer, slot]
                    self.mc[slot].pop(0)
                    allocate = True
                    candidate.slots.remove(slot)
                    candidate.interview_count += 1
                    break
            if not allocate:
                self.allocation[candidate.name]["MC"] = [candidate.name, "MC", "Cannot Allocate Slot", None]

            # PSDS
            allocate = False
            slots = list(candidate.slots)
            for slot in slots:
                if slot in self.psds and len(self.psds[slot]) > 0:
                    for i, interviewer in enumerate(self.psds[slot]):
                        if interviewer.name != mc_interviewer:
                            psds_interviewer = interviewer.name
                            self.allocation[candidate.name]["PSDS"] = [candidate.name, "PSDS", psds_interviewer, slot]
                            self.psds[slot].pop(i)
                            allocate = True
                            candidate.slots.remove(slot)
                            candidate.interview_count += 1
                            break
                if allocate:
                    break
            if not allocate:
                self.allocation[candidate.name]["PSDS"] = [candidate.name, "PSDS", "Cannot Allocate Slot", None]

    def show_allocations(self):
        print("#################### ALLOCATIONS ####################")
        print("Candidate Name \tInterview type \tInterviewer \tSlot")
        for candidate in self.allocation:
            for data in self.allocation[candidate]["MC"]:
                print(data, end="\t\t")
            print()
            for data in self.allocation[candidate]["PSDS"]:
                print(data, end="\t\t")
            print()
