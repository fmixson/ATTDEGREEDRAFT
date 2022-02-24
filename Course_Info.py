from Student_Info import StudentInfo


class CourseInfo(StudentInfo):

    def current_courses(self):
        current_term = 1219
        self.enrolled_courses = []

        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, "ID"]:
                if self.enrollment_history_df.loc[i, "Term"] == current_term:
                    if self.enrollment_history_df.loc[i, "Course"] not in self.enrolled_courses:
                        if self.enrollment_history_df.loc[i, 'Enrollment Drop Date'] == 0:
                            self.enrolled_courses.append(self.enrollment_history_df.loc[i, "Course"])
        return self.enrolled_courses

    def first_term(self):
        current_term = 1219
        semester = ''
        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, "ID"]:
                if self.enrollment_history_df.loc[i, 'Term'] != 800:
                    if self.enrollment_history_df.loc[i, 'Term'] <= current_term:
                        current_term = self.enrollment_history_df.loc[i, 'Term']
                        semester = self.enrollment_history_df.loc[i, 'Term Description']
        return semester


    def calculate_catalog_term(self):
        term_list = []
        previous_term = 0
        catalog_term = 0
        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, 'ID']:
                if self.enrollment_history_df.loc[i, 'Term'] not in term_list:
                    term_list.append(self.enrollment_history_df.loc[i, 'Term'])
                    term_list.sort()


        for term in term_list:
            term_difference = term - previous_term
            if term_difference > 10:
                catalog_term = term
            previous_term = term

        return catalog_term