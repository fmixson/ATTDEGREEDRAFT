import pandas as pd
from GE_Requirements import GeRequirements
from Major_Requirements import MajorRequirements



class DegreeCompletionReport:
    columns = ['Student_ID', 'First_Term', 'Catalog_Term', 'Major', 'GE_Plan','Total_Degree_Units','GE_Units', 'Total_Major_Units',
               'Degree_Major_Units', 'Elective_Units', 'Total_Missing', 'GE_Missing', 'Major_Missing', 'Missing_GE_Courses',
               'Missing_Major_Courses', 'GE_Courses', 'Major_Courses', 'Elective_Courses', 'Enrolled_Courses', 'Passed_Courses']
    LS_AA_Degrees_df = pd.DataFrame(columns=columns)
    LS_AA_Degrees_df.index.name = 'Rows'

    def __init__(self, student_id, first_term, major_name, geplan, completed_ge_courses, major_units, area_units_dict, missing_units, missing_ge,
                 missing_major, major_courses, enrolled_courses, degree_applicable_courses, catalog_term):

        self.student_id = student_id
        self.first_term = first_term
        self.major_name = major_name
        # self.student_major = student_major
        self.area_units_dict = area_units_dict
        self.missing_ge = missing_ge
        self.missing_major_courses = missing_major
        self.completed_ge_courses = completed_ge_courses
        self.major_course_dict = major_courses
        # self.major_requirements_dict = major_requirements_dict
        self.missing_units_dict = missing_units
        self.enrolled_courses = enrolled_courses
        self.degree_applicable_courses = degree_applicable_courses
        self.catalog_term = catalog_term
        self.geplan = geplan
        self.major_units = major_units



    def degree_completion(self):

        length = len(DegreeCompletionReport.LS_AA_Degrees_df)

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Student_ID'] = self.student_id
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'First_Term'] = self.first_term
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Catalog_Term'] = self.catalog_term
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major'] = self.major_name
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Plan'] = self.geplan
        # totalGEUnitsTest = sum(self.completed_ge_courses[x]['units'] for x in self.completed_ge_courses if x
        #                        not in GeRequirements.proficiencies)
        ge_units = sum(self.completed_ge_courses[x]['units'] for x in self.completed_ge_courses if x not in GeRequirements.proficiencies)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Units'] = ge_units
        print('major units before sum', self.major_units)
        major_units = sum(self.major_units)
        print('major units after sum', self.major_units)

        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Major_Units'] = major_units
        missingUnits = sum(self.missing_units_dict.values())
        degree_major_units = sum(self.area_units_dict.values())
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Major_Units'] = degree_major_units
        # DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Units'] = sum(self.elective_units)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Degree_Units'] = ge_units + major_units



        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Missing'] = len(self.missing_ge)
        values = self.missing_major_courses.values()
        missing_major_courses = sum(values)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Missing'] = missing_major_courses
        values = self.missing_units_dict.values()
        missing_major_units = sum(values)
        # DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Missing_Units'] = missing_major_units
        print('missing ge', self.missing_ge)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_GE_Courses'] = self.missing_ge

        missing_major_list = self.missing_major_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Missing_Major_Courses'] = missing_major_list

        ge_list = self.completed_ge_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Courses'] = ge_list
        major_list = self.major_course_dict.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Courses'] = major_list

        # DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Elective_Courses'] = self.elective_courses
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Enrolled_Courses'] = self.enrolled_courses

        total_missing = len(self.missing_ge) + missing_major_courses
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Total_Missing'] = total_missing
        passed_courses = self.degree_applicable_courses.items()
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Passed_Courses'] = passed_courses

        # print('length', length)
        # print(DegreeCompletionReport.LS_AA_Degrees_df)
        # print('inside deg com', DegreeCompletionReport.LS_AA_Degrees_df)
        return DegreeCompletionReport.LS_AA_Degrees_df


class DataframeFilter():
    studentIDList = []
    def __init__(self, degreeCompletionReport):
        self.degreeCompletionReport = degreeCompletionReport


    def build_student_list(self):
        for i in range(len(self.degreeCompletionReport)):
            if self.degreeCompletionReport.loc[i, 'Student_ID'] not in DataframeFilter.studentIDList:
                DataframeFilter.studentIDList.append(self.degreeCompletionReport.loc[i, 'Student_ID'])
        print('filter id list', DataframeFilter.studentIDList)
        return DataframeFilter.studentIDList

    def select_majors(self):


        total_row_list=[]

        for id in DataframeFilter.studentIDList:
            missing_list = []
            row_by_student_list = []
            for i in range(len(self.degreeCompletionReport)):
                if self.degreeCompletionReport.loc[i, 'Student_ID'] == id:

                    if len(row_by_student_list) < 1:
                         missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                         row_by_student_list.append(i)
                    elif len(row_by_student_list) < 2:
                        if self.degreeCompletionReport.loc[i, 'Total_Missing'] <= missing_list[0]:
                             missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                             row_by_student_list.insert(0, i)
                        else:
                            missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                            row_by_student_list.append(i)
                    elif len(row_by_student_list) < 3:
                        if self.degreeCompletionReport.loc[i, 'Total_Missing'] <= missing_list[0]:
                             missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                             row_by_student_list.insert(1, i)
                        elif missing_list[0] <= self.degreeCompletionReport.loc[i, 'Total_Missing'] < missing_list[1]:
                                    missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                                    row_by_student_list.insert(1, i)
                        else:
                            missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                            row_by_student_list.append(i)

                    elif len(row_by_student_list) >= 3:
                        if self.degreeCompletionReport.loc[i, 'Total_Missing'] < missing_list[0]:
                             missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                             row_by_student_list.insert(0, i)
                        elif missing_list[0] <= self.degreeCompletionReport.loc[i, 'Total_Missing'] < missing_list[1]:
                                    missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                                    row_by_student_list.insert(1, i)
                        elif missing_list[1] <= self.degreeCompletionReport.loc[i, 'Total_Missing'] < missing_list[2]:
                                    missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                                    row_by_student_list.insert(2, i)

                        # else:
                        #     missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
                        #     row_by_student_list.append(i)



                    print('id', id, row_by_student_list, missing_list)
            rows = row_by_student_list[:3]
            total_row_list.append(rows)
            print('total', total_row_list)

        #     print('len', len(row_by_student_list))
        #     if len(row_by_student_list) == 0:
        #         missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
        #         row_by_student_list.append(i)
        #     else:
        #         if self.degreeCompletionReport.loc[i, 'Total_Missing'] < missing_list[0]:
        #             missing_list.clear()
        #             row_by_student_list.clear()
        #             missing_list.append(self.degreeCompletionReport.loc[i, 'Total_Missing'])
        #             row_by_student_list.append(i)
        #     print('id', id, row_by_student_list, missing_list)
        # total_row_list.append(row_by_student_list)
        print('total', total_row_list)
        return total_row_list

    def select_top_majors(self, total_row_list):
        clean_row_list = []
        for sub_list in total_row_list:
            clean_row_list += sub_list
        print('clean row', clean_row_list)
        return clean_row_list

    # def degree_status(self, length, missing_major_courses):
    #     degree_status_ge = False
    #     degree_status_major = False
    #     if len(self.missing_ge) == 0:
    #         DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Completed'
    #         degree_status_ge = True
    #     else:
    #         DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'GE_Status'] = 'Incomplete'
    #
    #     if missing_major_courses == 0:
    #             DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Completed'
    #             degree_status_major = True
    #     else:
    #             DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Major_Status'] = 'Incomplete'


        # if sum(self.completed_ge_units) + sum(self.major_units_list) + sum(self.elective_units) >= 60:
        #     if degree_status_ge == True and degree_status_major == True:
        #         DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Completed'
        #     else:
        #         DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Degree_Status'] = 'Incomplete'
        #
        # return length

    def unused_courses(self, length, ge_courses, major_courses, elective_courses, student_course_list):
        """
           This function will take as inputs ge courses, major courses, elective courses, and revised courses list. It will
           compare the revised course list to the other three lists and remove any courses that appear in the other lists.
           This will leave a list of unused courses, giving us information about where students are wasting their units.
           """
        unused_courses = []
        print('maj crses', major_courses)
        ge_course_list = ge_courses.values()
        print('ge crses', ge_course_list)

        for course_key in student_course_list:
            if course_key not in ge_course_list:
                if course_key not in major_courses:
                    if course_key not in elective_courses:
                        unused_courses.append(course_key)
        print('un crses', unused_courses)
        DegreeCompletionReport.LS_AA_Degrees_df.loc[length, 'Additional_Courses'] = unused_courses

