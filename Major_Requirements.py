import pandas as pd


class MajorRequirements:
    # major_requirements_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/English_PlanA_GE.csv")
    # major_requirements_dataframe = pd.read_csv("C:/Users/family/Desktop/Programming/Copy of COMM_AA.csv")
    # major_requirements_dict = {}

    def __init__(self, degree_applicable_courses, completed_ge_courses, major_requirements, major_name):
        self.degree_applicable_courses = degree_applicable_courses
        self.completed_ge_courses = completed_ge_courses
        self.major_requirements = major_requirements
        self.major_name = major_name
        self.major_course_dict = {}
        self.major_courses_list = []
        self.major_courses_list2 = []
        self.major_units_list = []
        self.major_units_dict = {}
        self.area_units_dict = {}
        self.discipline_list = []
        self.discipline_set = set()

    def construct_major_dataframe(self):
        major_dataframe = pd.read_csv(self.major_requirements)
        return major_dataframe

    def _two_disciplines(self, course_key, total_area_units, total_units):
        discipline = course_key.split()
        discipline = discipline[0]
        disc = False

        if total_area_units == (total_units - 3):
            unique_disciplines = set(self.discipline_list)
            if len(unique_disciplines) < 2:
                if discipline in unique_disciplines:
                    disc = True
                else:
                    self.discipline_list.append(discipline)
        else:
            self.discipline_list.append(discipline)
        return disc

    def _three_disciplines(self, course_key, total_area_units, total_units):
        discipline = course_key.split()
        discipline = discipline[0]
        disc = False

        if total_area_units >= (total_units - 6):
            unique_disciplines = set(self.discipline_list)
            if len(unique_disciplines) < 3:
                if len(unique_disciplines) == 2:
                    self.discipline_list.append(discipline)
                elif unique_disciplines == 1:
                    if discipline in unique_disciplines:
                        disc = True
            else:
                self.discipline_list.append(discipline)
        else:
            self.discipline_list.append(discipline)
        return disc

    def major_requirements_completed(self, major_dataframe, area_name, total_units, number_of_disciplines=1):
        proficiency_list = ['Writing_Proficiency', 'Math_Proficiency', 'Health_Proficiency', 'Reading_Proficiency']
        self.major_courses_list2 = []
        total_area_units = 0
        area_units_list = []
        ge_course_list = []


        Option = 2
        if self.major_name == 'English for Transfer-AAT':
            if "ENGL 103" in self.degree_applicable_courses:
                 Option = 1
            elif "ENGL 102" in self.degree_applicable_courses:
                Option == 1

        if Option == 1:
            if area_name == 'Core':
                total_units = 6
            elif area_name == "ListB":
                total_units = 3

        self.major_num_of_units_dict[area_name] = total_units

        disc = False
        self.discipline_list = []
        self.discipline_set = set()


        for key in self.completed_ge_courses:
            if key not in proficiency_list:
                ge_course_list.append(self.completed_ge_courses[key])

        for i in range(len(major_dataframe[area_name])):
            ge_course = False
            major_course = False

            if total_area_units < total_units:
                for course_key in self.degree_applicable_courses:

                    if course_key == major_dataframe.loc[i, area_name]:
                        if course_key in ge_course_list:
                            ge_course = True

                        if course_key in self.major_courses_list:
                            major_course = True
                        if not major_course:
                            if number_of_disciplines > 1:
                                if number_of_disciplines == 2:
                                    disc = MajorRequirements._two_disciplines(self, course_key=course_key,
                                                                              total_area_units=total_area_units,
                                                                              total_units=total_units)

                                elif number_of_disciplines == 3:
                                    disc = MajorRequirements._three_disciplines(self, course_key=course_key,
                                                                                total_area_units=total_area_units,
                                                                                total_units=total_units)
                            if not disc:
                                self.area_units_dict[area_name] = self.degree_applicable_courses[course_key]
                                self.major_courses_list.append(course_key)
                                self.major_courses_list2.append(course_key)
                                self.major_course_dict[area_name] = self.major_courses_list2
                                area_units_list.append(self.degree_applicable_courses[course_key]['units'])
                                if not ge_course:
                                    self.major_units_list.append(self.degree_applicable_courses[course_key]['units'])
            print('area units', area_units_list)
            total_area_units = sum(area_units_list)
            self.area_units_dict[area_name] = total_area_units
            print('area dict', self.area_units_dict)

        return self.area_units_dict, self.major_course_dict


