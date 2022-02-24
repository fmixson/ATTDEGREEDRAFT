from GE_Requirements import GeRequirements

class SocialBehavAreas(GeRequirements):

    def __init__(self, degree_applicable_dict, ge_dataframe):
        self.degree_applicable_dict = degree_applicable_dict
        self.ge_dataframe = ge_dataframe
        self.soc_behav_course_list = []
        self.soc_behav_disc_list = []

    def two_discipline_check(self, course_key, soc_behav_course_list):
        discipline = course_key.split()
        discipline = discipline[0]
        disc = False
        discipline_set = set(soc_behav_course_list)
        if discipline in discipline_set:
            disc = True

        return disc

    def ge_courses_completed(self, area_name, ge_courses_completed):
        disc = False
        ge_course_list = [d['course'] for d in ge_courses_completed.values() if d]
        discipline_set = set(self.soc_behav_course_list)
        for i in range(len(self.ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == self.ge_dataframe.loc[i, area_name]:
                    discipline_set = set(self.soc_behav_disc_list)
                    if area_name not in ge_courses_completed:
                        if key not in ge_course_list:
                            if len(self.soc_behav_course_list) == 2:
                                if len(discipline_set) < 2:
                                     disc = SocialBehavAreas.two_discipline_check(self, course_key=key,
                                                                                soc_behav_course_list=discipline_set)
                            if not disc:
                                self.soc_behav_course_list.append(key)
                                ge_courses_completed[area_name] = {'course': key, 'units': self.degree_applicable_dict[key]['units']}
                                # self.completed_ge_units.append(self.degree_applicable_dict[key])
                                ge_units_total = sum(d['units'] for d in ge_courses_completed.values()if d)
                                discipline = key.split()
                                discipline = discipline[0]
                                self.soc_behav_disc_list.append(discipline)
                                discipline_set = set(self.soc_behav_disc_list)
        return ge_courses_completed
