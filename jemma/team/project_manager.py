import os
from jemma.tools import say, color, open_local_browser, name_to_file_name
from jemma.requirements.feature import Feature, UserStory

class ProjectManager:
    def __init__(self, feature, project_name="project", role = "Project Manager"):
        self.feature = feature
        self.role = role
        self.project_name = project_name

    def record_requirement(self,
                           name,
                           requirement,
                           path):
        # create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)

        requirement_path = os.path.join(path,
                                        name_to_file_name(name))
        with open(requirement_path, "w") as requirement_file:
            requirement_file.write(requirement)

        print(f"storing requirements for \"{name}\" in \"{requirement_path}\"")

    def meet_to_create_user_stories(self,
                                    thinker,
                                    business_owner):
        say(self.role, "\nDear Business Owner, in this meeting we'll work on splitting the requirements and creating user stories.",
            who_color = color.CYAN, message_color = color.YELLOW)

        refined = business_owner.split_and_refine(thinker,
                                                  self.feature.requirements)

        for unit in refined:
            user_story = UserStory(title=unit["title"],
                                   acceptance_criteria=unit["acceptance_criteria"])
            self.feature.add_user_story(user_story)

    def meet_to_refine_user_stories(self,
                                    thinker,
                                    engineer,
                                    business_owner,
                                    max_refinement_attempts = 1):

        say(self.role, "\nDear Engineer, meet the Business Owner, welcome to the refinement meeting, let's refine'em user stories!",
            who_color = color.CYAN, message_color = color.YELLOW)

        for title, user_story in self.feature.get_user_stories().items():
            self._refine_user_story(thinker,
                                    engineer,
                                    business_owner,
                                    user_story,
                                    max_refinement_attempts)

    def _refine_user_story(self,
                           thinker,
                           engineer,
                           business_owner,
                           user_story,
                           max_refinement_attempts):

        refinement_attempts = 0
        engineer_response = engineer.review_user_story(thinker,
                                                       user_story,
                                                       self.feature.requirements)

        while "No clarification needed" not in engineer_response and refinement_attempts < max_refinement_attempts:
            say(self.role, "\nDear Business Owner, the Engineer would like you to clarify details about \"" + user_story.title + "\"",
                who_color=color.CYAN, message_color=color.YELLOW)

            clarified_user_story = business_owner.clarify_user_story(thinker,
                                                                     self.feature.requirements,
                                                                     user_story,
                                                                     engineer_response)
            self.feature.update_user_story(user_story.title,
                                           clarified_user_story)

            refinement_attempts += 1
            if refinement_attempts < max_refinement_attempts:
                engineer_response = engineer.review_user_story(thinker,
                                                               self.feature.get_user_story(user_story.title),
                                                               self.feature.requirements)

    def meet_to_build_prototype(self,
                                thinker,
                                engineer,
                                path = "prototype"):

        say(self.role,
            "\nDear Engineer, in this meeting let's put our heads together to build a prototype based on the requirements.",
            who_color = color.CYAN,
            message_color = color.YELLOW)

        prototype = engineer.create_prototype(thinker,
                                              self.feature.requirements)
        engineer.record_prototype(path,
                                  prototype)
        open_local_browser(path)

        return prototype

    def meet_to_refactor(self,
                         thinker,
                         engineer,
                         prototype,
                         feedback,
                         path = "prototype"):

        say(self.role,
            "\nDear Engineer, we have met with the user and received a valuable feedback. sudo make it better! 🛠️",
            who_color = color.CYAN,
            message_color = color.YELLOW)

        refactored = engineer.refactor_prototype(thinker,
                                                 self.feature.requirements,
                                                 prototype,
                                                 feedback)

        engineer.record_prototype(path,
                                  refactored)
        open_local_browser(path)

        return refactored

    def meet_to_test_prototype(self,
                               thinker,
                               tester,
                               path = "prototype"):

        say(self.role,
            "\nDear Tester, in this meeting let's focus on requirements and built code to test a prototype.",
            who_color = color.CYAN,
            message_color = color.YELLOW)

        prototype = tester.read_prototype(path)
        test_results = tester.review_prototype(thinker,
                                               self.feature.requirements,
                                               prototype)

        return test_results

    def meet_to_combine_user_stories(self,
                                     thinker,
                                     business_owner):

        say(self.role, "\nDear Business Owner, in this meeting we'll combine user stories into a single document",
            who_color = color.CYAN, message_color = color.YELLOW)

        combined_user_stories = business_owner.combine_user_stories(thinker,
                                                                    self.feature.requirements,
                                                                    self.feature.get_user_stories())
        self.feature = Feature(combined_user_stories)

    def user_stories_to_requirement(self):
        self.feature = Feature(self.feature.export_user_stories_titles_and_criteria())

    def meet_to_create_requirements(self,
                                    thinker,
                                    business_owner,
                                    idea,
                                    sketch = None,
                                    store_path="requirements"):
        say(self.role, "\nDear Business Owner, in this meeting we'll work on creating requirements based on the 💡 idea",
            who_color = color.CYAN, message_color = color.YELLOW)

        requirements = "requirements not created yet"
        if sketch:
            sketch_intel = business_owner.idea_with_sketch_to_intel(thinker,
                                                                    idea,
                                                                    sketch)
            print(f"sketch intel: {sketch_intel}")

            requirements = business_owner.idea_with_sketch_to_prompt(thinker,
                                                                     idea,
                                                                     sketch_intel)
        else:
            requirements = business_owner.idea_to_prompt(thinker, idea)

        self.record_requirement(idea, requirements, store_path)

        self.feature = Feature(requirements)
