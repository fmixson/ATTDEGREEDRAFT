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


def ge_progess(student_id, enrollment_history_df, ge_plan, ge_plan_list):
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
            # print('ge main', ge_courses_completed)
    missing_ge_courses = gereq.ge_requirements_completed(ge_plan_list)
    return ge_courses_completed, degree_applicable_courses, missing_ge_courses


def major_progress(degree_applicable_courses, ge_courses_completed, **kwargs):
    global area_units_dict
    global major_course_dict
    print(len(kwargs))
    print(kwargs['major_name'])
    if len(kwargs) == 18:
        print(kwargs['major_course_requirements'])
        major = MajorRequirements(degree_applicable_courses=degree_applicable_courses,
                                  completed_ge_courses=ge_courses_completed,
                                  major_name=kwargs['major_name'],
                                  major_requirements=kwargs['major_course_requirements'])
        major_dataframe = major.construct_major_dataframe()
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major1'],
                                           total_units=kwargs['major1_units'],
                                           number_of_disciplines=kwargs['major1_disciplines'],
                                           number_of_courses=kwargs['major1_courses'])
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major2'],
                                           total_units=kwargs['major2_units'],
                                           number_of_disciplines=kwargs['major2_disciplines'],
                                           number_of_courses=kwargs['major2_courses'])
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major3'],
                                           total_units=kwargs['major3_units'],
                                           number_of_disciplines=kwargs['major3_disciplines'],
                                           number_of_courses=kwargs['major3_courses'])
        area_units_dict, major_course_dict, major_units_list = major.major_requirements_completed(major_dataframe=major_dataframe,
                                                                                area_name=kwargs['major4'],
                                                                                total_units=kwargs['major4_units'],
                                                                                number_of_disciplines=kwargs[
                                                                                    'major4_disciplines'],
                                                                                number_of_courses=kwargs[
                                                                                    'major4_courses'])
    if len(kwargs) == 14:
        print(kwargs['major_course_requirements'])
        major = MajorRequirements(degree_applicable_courses=degree_applicable_courses,
                                  completed_ge_courses=ge_courses_completed,
                                  major_name=kwargs['major_name'],
                                  major_requirements=kwargs['major_course_requirements'])
        major_dataframe = major.construct_major_dataframe()
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major1'],
                                           total_units=kwargs['major1_units'],
                                           number_of_disciplines=kwargs['major1_disciplines'],
                                           number_of_courses=kwargs['major1_courses'])
        major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major2'],
                                           total_units=kwargs['major2_units'],
                                           number_of_disciplines=kwargs['major2_disciplines'],
                                           number_of_courses=kwargs['major2_courses'])
        area_units_dict, major_course_dict, major_units_list = major.major_requirements_completed(major_dataframe=major_dataframe, area_name=kwargs['major3'],
                                           total_units=kwargs['major3_units'],
                                           number_of_disciplines=kwargs['major3_disciplines'],
                                           number_of_courses=kwargs['major3_courses'])
        # area_units_dict, major_course_dict = major.major_requirements_completed(
        #                                     major_dataframe=major_dataframe,
        #                                     area_name=kwargs['major4'],
        #                                     total_units=kwargs['major4_units'],
        #                                     number_of_disciplines=kwargs['major4_disciplines'],
        #                                     number_of_courses=kwargs['major4_courses'])


    elif len(kwargs) == 10:
        major = MajorRequirements(degree_applicable_courses=degree_applicable_courses,
                                  completed_ge_courses=ge_courses_completed,
                                  major_name=kwargs['major_name'],
                                  major_requirements=kwargs['major_course_requirements'])
        major_dataframe = major.construct_major_dataframe()
        major.major_requirements_completed(major_dataframe=major_dataframe,
                                           area_name=kwargs['major1'],
                                           total_units=kwargs['major1_units'],
                                           number_of_disciplines=kwargs['major1_disciplines'],
                                           number_of_courses=kwargs['major1_courses'])
        area_units_dict, major_course_dict, major_units_list = major.major_requirements_completed(major_dataframe=major_dataframe,
                                           area_name=kwargs['major2'],
                                           total_units=kwargs['major2_units'],
                                           number_of_disciplines=kwargs['major2_disciplines'],
                                           number_of_courses=kwargs['major2_courses'])


    major_prog = MajorProgress(major_course_dict=major.major_course_dict,
                               major_units_required=major.major_num_of_units_dict,
                               area_units=major.area_units_dict,
                               num_of_courses_required=major.major_num_of_courses_dict)
    missing_course_dict = major_prog.major_num_of_courses()
    missing_units_dict = major_prog.major_num_of_units()
    # print('major course dict major progress func', major_course_dict, missing_course_dict, missing_units_dict, area_units_dict)

    return missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list


def degree_report(id, first_term, major_name, geplan, completed_ge, major_units, area_units_dict, missing_units, missing_ge, missing_major,
                  major_courses, enrolled_courses, degree_applicable_courses, catalog_term):
    print('major course in degree report function', id, major_courses)
    # , first_term, major_name, missing_ge, completed_ge, major_courses, major_requirements):
    report = DegreeCompletionReport(id, first_term, major_name, geplan, completed_ge, major_units, area_units_dict, missing_units, missing_ge,
                                    missing_major, major_courses, enrolled_courses, degree_applicable_courses, catalog_term)
    # , first_term, major_name, completed_ge,missing_ge,major_courses, major_requirements)
    report.degree_completion()


Plan_B_list = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Amer_Hist',
               'Hum', 'Arts_Hum',
               'Amer_Gov', 'Institutions', 'Self_Dev']
Plan_B_list_21 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts',
                  'Amer_Hist_Gov', 'Hum', 'Arts_Hum',
                  'Institutions', 'Self_Dev', 'Ethnic_Stds']
Plan_C_list = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2',
               'Soc_Behav3',
               'Phys_Sci', 'Bio_Sci', 'Sci_Labs']

enrollment_history_file = fileopenbox('Upload Enrollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()
sid = StudentID(enrollment_history_df=enrollment_history_df)
student_ids_list = sid.student_ids()

GePlans = ['PlanB', 'PlanC']
for plan in GePlans:
    for id in student_ids_list:
        print('student id', id)
        crsinfo = CourseInfo(student_id=id, enrollment_history_df=enrollment_history_df)
        enrolled_courses = crsinfo.current_courses()
        semester = crsinfo.first_term()
        catalog_term = crsinfo.calculate_catalog_term()

        if plan == 'PlanB':
            if catalog_term >= 1219:
                ge_courses_completed, degree_applicable_courses, missing_ge_courses = ge_progess(student_id=id,
                                                                                                 enrollment_history_df=enrollment_history_df,
                                                                                                 ge_plan='PlanB_GE_2021.csv',
                                                                                                 ge_plan_list=Plan_B_list_21, )
            else:
                ge_courses_completed, degree_applicable_courses, missing_ge_courses = ge_progess(student_id=id,
                                                                                                 enrollment_history_df=enrollment_history_df,
                                                                                                 ge_plan='PlanB_GE.csv',
                                                                                                 ge_plan_list=Plan_B_list)

        else:
            ge_courses_completed, degree_applicable_courses, missing_ge_courses = ge_progess(student_id=id,
                                                                                             enrollment_history_df=enrollment_history_df,
                                                                                             ge_plan='PlanC_GE.csv',
                                                                                             ge_plan_list=Plan_C_list)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list = major_progress(
            degree_applicable_courses=degree_applicable_courses,
            ge_courses_completed=ge_courses_completed,
            major_name="Comm Studies for Transfer-AAT",
            major_course_requirements='AAT_COMM.csv',
            major1='Core', major1_units=3, major1_disciplines=1, major1_courses=1,
            major2='ListA', major2_units=6, major2_disciplines=1, major2_courses=2,
            major3='ListB', major3_units=3, major3_disciplines=1, major3_courses=1,
            major4='ListC', major4_units=3, major4_disciplines=1, major4_courses=1)

        degree_report(id=id, first_term=CourseInfo.first_term, major_name="Comm Studies for Transfer-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

        print('major dict in main', major_course_dict)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list = major_progress(
            degree_applicable_courses=degree_applicable_courses,
            ge_courses_completed=ge_courses_completed,
            major_name="English for Transfer-AAT",
            major_course_requirements='AAT_English.csv',
            major1='Core', major1_units=3, major1_disciplines=1, major1_courses=1,
            major2='ListA', major2_units=6, major2_disciplines=1, major2_courses=2,
            major3='ListB', major3_units=6, major3_disciplines=1, major3_courses=1,
            major4='ListC', major4_units=3, major4_disciplines=1, major4_courses=1)
        print('2nd major dict in main', major_course_dict)

        degree_report(id=id, first_term=CourseInfo.first_term, major_name="English for Transfer-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses,degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list = major_progress(
            degree_applicable_courses=degree_applicable_courses,
            ge_courses_completed=ge_courses_completed,
            major_name="Spanish for Transfer-AAT",
            major_course_requirements='AAT_Spanish.csv',
            major1='Core', major1_units=19, major1_disciplines=1, major1_courses=4,
            major2='ListA', major2_units=3, major2_disciplines=1, major2_courses=1)

        print('after span', major_course_dict)
        degree_report(id=id, first_term=CourseInfo.first_term, major_name="Spanish for Transfer-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list =major_progress\
            (degree_applicable_courses=degree_applicable_courses,
                       ge_courses_completed=ge_courses_completed,
                        major_name="Business Administration-AST",
                        major_course_requirements='AAT_BusAdmin.csv',
                        major1='Core', major1_units=15, major1_disciplines=1, major1_courses=5,
                        major2='ListA', major2_units=3, major2_disciplines=1, major2_courses=1,
                        major3='ListB', major3_units=6, major3_disciplines=1, major3_courses=2)

        degree_report(id=id, first_term=CourseInfo.first_term, major_name="Business Administration-AST",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)
        #
        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list =major_progress(degree_applicable_courses=degree_applicable_courses, ge_courses_completed=ge_courses_completed,
                       major_name="Psychology for Transfer-AAT",
                       major_course_requirements="AAT_Psychology.csv",
                       major1='Core', major1_units=11, major1_disciplines=1, major1_courses=3,
                       major2='ListA', major2_units=3, major2_disciplines=1, major2_courses=1,
                       major3='ListB', major3_units=3, major3_disciplines=1, major3_courses=1,
                       major4='ListC', major4_units=3, major4_disciplines=1, major4_courses=1)

        degree_report(id=id, first_term=CourseInfo.first_term,
                      major_name="Psychology for Transfer-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list =major_progress(degree_applicable_courses=degree_applicable_courses, ge_courses_completed=ge_courses_completed,
                       major_name="Sociology for Transfer-AAT",
                       major_course_requirements="AAT_Sociology.csv",
                       major1='Core1', major1_units=3, major1_disciplines=1, major1_courses=1,
                       major2='Core2', major2_units=6, major2_disciplines=1, major2_courses=2,
                       major3='ListA', major3_units=6, major3_disciplines=1, major3_courses=2,
                       major4='ListB', major4_units=3, major4_disciplines=1, major4_courses=1)

        degree_report(id=id, first_term=CourseInfo.first_term,
                      major_name="Sociology for Transfer-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list=major_progress(
                        degree_applicable_courses=degree_applicable_courses,
                        ge_courses_completed=ge_courses_completed,
                       major_name="Administration of Justice for Transfer-AAT",
                       major_course_requirements="AAT_AdminJust.csv",
                       major1='Core', major1_units=6, major1_disciplines=1, major1_courses=2,
                       major2='ListA', major2_units=6, major2_disciplines=1, major2_courses=2,
                       major3='ListB', major3_units=6, major3_disciplines=1, major3_courses=2)

        degree_report(id=id, first_term=CourseInfo.first_term,
                      major_name="Administration of Justice for Transfer-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

        missing_course_dict, missing_units_dict, major_course_dict, area_units_dict, major_units_list = major_progress(
            degree_applicable_courses=degree_applicable_courses,
            ge_courses_completed=ge_courses_completed,
            major_name="Elementary Teacher Education-AAT",
            major_course_requirements='AAT_TeacherEd.csv',
            major1='Core', major1_units=42, major1_disciplines=1, major1_courses=13,
            major2='ListA', major2_units=3, major2_disciplines=1, major2_courses=1,
            major3='ListB', major3_units=3, major3_disciplines=1, major3_courses=1)

        degree_report(id=id, first_term=CourseInfo.first_term, major_name="Elementary Teacher Education-AAT",
                      completed_ge=ge_courses_completed, major_units=major_units_list,
                      area_units_dict=area_units_dict, missing_units=missing_units_dict, missing_ge=missing_ge_courses,
                      missing_major=missing_course_dict, major_courses=major_course_dict,
                      enrolled_courses=enrolled_courses, degree_applicable_courses=degree_applicable_courses,
                      catalog_term=catalog_term,
                      geplan=plan)

    DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
    DegreeCompletionReport.LS_AA_Degrees_df.to_csv(
        'C:/Users/fmixson/Desktop/AAT_LA_Division_Degrees.csv')
