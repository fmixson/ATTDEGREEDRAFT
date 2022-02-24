class StudentID:

    def __init__(self, enrollment_history_df):
        self.enrollment_history_df = enrollment_history_df
        self.student_ids_list = []

    def student_ids(self):
        for i in range(len(self.enrollment_history_df)):
            if self.enrollment_history_df.loc[i, 'ID'] not in self.student_ids_list:
                self.student_ids_list.append(self.enrollment_history_df.loc[i, 'ID'])
        return self.student_ids_list