from Inter import Interview


def test_register_interviewers_test1(interview):
    # TC 1
    interview.register_interviewer("Interviewer1", ["MC", "PSDS"], 7, [1, 2, 3, 4])
    interview.register_interviewer("Interviewer2", ["MC", "PSDS"], 6, [1, 2, 3, 4])


def test_register_interviewers_test2(interview):
    # TC 2
    interview.register_interviewer("Interviewer1", ["MC", "PSDS"], 7, [1, 2, 3, 4])
    interview.register_interviewer("Interviewer2", ["MC", "PSDS"], 6, [2, 3, 4])
    # interview.register_interviewer("Interviewer2", ["MC", "PSDS"], 6, [2, 3, 4])
    # for user in interview.interviewers:
    #     print(user)


def test_register_interviewers_test3(interview):
    # TC 3
    interview.register_interviewer("Interviewer1", ["MC", "PSDS"], 7, [1, 2, 3, 4])
    interview.register_interviewer("Interviewer2", ["MC", "PSDS"], 6, [2, 3, 4])
    interview.register_interviewer("Interviewer2", ["MC", "PSDS"], 6, [2, 3, 4])


def test_register_interviewers_test4(interview):
    # TC 4
    interview.register_interviewer("Interviewer1", ["MC", "PSDS"], 7, [1, 2, 3, 4])
    interview.register_interviewer("Interviewer2", [], 6, [2, 3, 4])


def test_register_interviewee_test1(interview):
    # TC 1
    interview.register_interviewee("Candidate1", [1, 2, 3, 7, 8])
    interview.register_interviewee("Candidate2", [1, 2, 3, 7, 8])
    interview.register_interviewee("Candidate3", [8])


def test_register_interviewee_test2(interview):
    # TC 2
    interview.register_interviewee("Candidate1", [1, 2, 3, 7, 8])
    interview.register_interviewee("Candidate2", [1, 2, 3, 7, 8])
    # for user in interview.interviewees:
    #     print(user)


if __name__ == "__main__":
    # TC1
    print("Conducting Test Case 1")
    interview1 = Interview()
    test_register_interviewers_test1(interview1)
    test_register_interviewee_test1(interview1)
    interview1.allocate_interviews()
    interview1.show_allocations()

    print()

    # TC2
    print("Conducting Test Case 2")
    interview2 = Interview()
    test_register_interviewers_test2(interview2)
    test_register_interviewee_test2(interview2)
    interview2.allocate_interviews()
    interview2.show_allocations()

    # TC3
    print("Conducting Test Case 3")
    interview1 = Interview()
    test_register_interviewers_test3(interview1)
    test_register_interviewee_test1(interview1)
    interview1.allocate_interviews()
    interview1.show_allocations()

    # TC4
    print("Conducting Test Case 4")
    interview1 = Interview()
    test_register_interviewers_test4(interview1)
    test_register_interviewee_test1(interview1)
    interview1.allocate_interviews()
    interview1.show_allocations()
