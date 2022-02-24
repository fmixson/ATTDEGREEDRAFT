from easygui import fileopenbox
import pandas as pd
from Enrollment_History_Dataframe import EnrollmentHistoryDataFrame
from Student_Info import StudentInfo
from Course_Info import CourseInfo
from GE_Requirements import GeRequirements
from Social_Behavioral_Areas import SocialBehavAreas
from Student_ID import StudentID
from Major_Requirements import MajorRequirements
from Major_Progress import MajorProgress
from Degree_Completion_Report import DegreeCompletionReport


def ge_progess(student_id, enrollment_history_df, ge_plan, ge_plan_list, **kwargs):
    sinfo = StudentInfo(student_id=id, enrollment_history_df=enrollment_history_df)
    degree_applicable_courses = sinfo.completed_courses()
    current_courses = crsinfo.current_courses()
    gereq = GeRequirements(degree_applicable_dict=degree_applicable_courses, ge_plan=ge_plan)
    ge_dataframe = gereq.construct_ge_dataframe()
    # gereq.ge_courses_completed(ge_dataframe=ge_dataframe)
    socbeh = SocialBehavAreas(degree_applicable_dict=degree_applicable_courses, ge_dataframe=ge_dataframe)
    for area in ge_plan_list:
        if area == 'Soc_Behav1' or area == 'Soc_Behav2' or area == 'Soc_Behav3':
            socbeh.ge_courses_completed(area_name=area, ge_courses_completed=ge_courses_completed)
        else:
            ge_courses_completed = gereq.ge_courses_completed(area_name=area, ge_dataframe=ge_dataframe)
    missing_ge_courses = gereq.ge_requirements_completed(ge_plan_list)

def major_progress(degree_applicable_courses, ge_courses_completed, **kwargs):
    if len(kwargs) == 14:
        major = MajorRequirements(degree_applicable_courses=degree_applicable_courses, completed_ge_courses=ge_courses_completed,
                                   major_name=kwargs['major_name'], major_requirements=kwargs['major_requirements'])
        major_dataframe = major.construct_major_dataframe()
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])

        majorProgress = MajorProgress(major_course_dict=major.major_course_dict,
                                 major_units_required=major.major_num_of_units_dict,
                                 area_units=major.area_units_dict,
                                 num_of_courses_required=major.major_num_of_courses_dict)

        missing_course_dict = majorProgress.major_num_of_courses()
        missing_units_dict = majorProgress.major_num_of_units()



Plan_B_list = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist', 'Amer_Gov', 'Institutions', 'Self_Dev']
Plan_B_list_21 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist_Gov', 'Institutions', 'Self_Dev', 'Ethnic_Stds']
Plan_C_list = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2', 'Soc_Behav3',
               'Phys_Sci', 'Bio_Sci', 'Sci_Labs']

enrollment_history_file = fileopenbox('Upload Enrollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()
sid = StudentID(enrollment_history_df=enrollment_history_df)
student_ids_list = sid.student_ids()

GePlans = ['PlanB', 'PlanC']
for plan in GePlans:
    for id in student_ids_list:
        crsinfo = CourseInfo(student_id=id, enrollment_history_df=enrollment_history_df)
        semester = crsinfo.first_term()
        catalog_term = crsinfo.calculate_catalog_term()
        if plan == 'PlanB':
            if catalog_term >= 1219:
                ge_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanB_GE_2021.csv', ge_plan_list=Plan_B_list_21, )
            else:
                ge_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanB_GE.csv',
                           ge_plan_list=Plan_B_list)

        else:
            ge_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanC_GE.csv', ge_plan_list=Plan_C_list)

        major_progress(degree_applicable_courses=StudentInfo.completed_courses, ge_courses_completed=GeRequirements.ge_courses_completed,
                       major_name="Comm Studies for Transfer-AAT", major_course_requirements='AAT_COMM.csv',
                       major1='Core', major1_units=3, major1_disciplines=1, major1_courses=1,
                       major2='ListA', major2_units=6, major2_disciplines=1, major2_courses=2,
                       major3='ListB', major3_units=3, major3_disciplines=1, major3_courses=1,
                       major4='ListC', major4_units=3, major4_disciplines=1, major4_courses=1)

        major_progress(degree_applicable_courses=StudentInfo.completed_courses, ge_courses_completed=GeRequirements.ge_courses_completed,
                        major_name="English for Transfer-AAT",
                        major_course_requirements='AAT_English.csv',
                        major1='Core', major1_units=3, major1_disciplines=1, major1_courses=1,
                        major2='ListA', major2_units=6, major2_disciplines=1, major2_courses=2,
                        major3='ListB', major3_units=6, major3_disciplines=1, major3_courses=1,
                        major4='ListC', major4_units=3, major4_disciplines=1, major4_courses=1)

        major_progress(degree_applicable_courses=StudentInfo.completed_courses, ge_courses_completed=GeRequirements.ge_courses_completed,
                        major_name="Spanish for Transfer-AAT",
                        major_course_requirements='AAT_Spanish.csv',
                        major1='Core', major1_units=19, major1_disciplines=1, major1_courses=1,
                        major2='ListA', major2_units=3, major2_disciplines=1, major2_courses=2)






