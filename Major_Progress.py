import pandas as pd

from Major_Requirements import MajorRequirements


class MajorProgress(MajorRequirements):

    requirements = []

    def __init__(self, major_course_dict, major_units_required, area_units, num_of_courses_required):
        self.area_units = area_units
        # self.student_id = student_id
        self.major_course_dict = major_course_dict
        self.major_units_required = major_units_required
        # self.major_df = pd.DataFrame
        self.num_of_courses_required = num_of_courses_required
        # self.requirements_dict = {}
        # self.missing_major_courses_dict = {}
        self.missing_courses_dict = {}
        self.missing_units_dict = {}
        # print('no of crses', self.no_of_courses_required)

    def major_num_of_courses(self):

        for major_key in self.num_of_courses_required:
            if major_key in self.major_course_dict:
                missing_courses = self.num_of_courses_required[major_key] - len(self.major_course_dict[major_key])
                if missing_courses == 0:
                    self.missing_courses_dict[major_key] = 0
                elif missing_courses > 0:
                    self.missing_courses_dict[major_key] = int(missing_courses)
            else:
                self.missing_courses_dict[major_key] = int(self.num_of_courses_required[major_key])

        # print('missing maj crs dic', self.missing_courses_dict)
        total_missing_major_courses = sum(self.missing_courses_dict.values())
        # print('tot mis', total_missing_major_courses)
        return self.missing_courses_dict

    def major_num_of_units(self):

        for major_key in self.major_units_required:
            if major_key in self.major_course_dict:
                missing_units = self.major_units_required[major_key] - self.area_units[major_key]
                if missing_units == 0:
                    self.missing_units_dict[major_key] = 0
                elif missing_units > 0:
                    self.missing_units_dict[major_key] = int(missing_units)
            else:
                self.missing_units_dict[major_key] = self.major_units_required[major_key]
        # print('mis units dict', self.missing_units_dict)

        return self.missing_units_dict