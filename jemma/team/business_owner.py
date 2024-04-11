import json
from jemma.requirements.feature import UserStory
from jemma.tools import read_file, say, color
import jemma.prompt.business.owner as prompt

class BusinessOwner:
    def __init__(self, role, title="Business Owner"):
        self.role = role
        self.title = title

    def split_requirements_to_features(self, thinker, requirements, features="", evaluation=""):
        features = thinker.think(prompt.split_requirements_to_features(self.role,
                                                                       requirements,
                                                                       features,
                                                                       evaluation),
                                 self.title)
        splits = [line for line in features.strip().split('\n') if line.strip()]
        return splits

    def evaluate_features(self, thinker, features, requirements):
        features_json = json.dumps(features)
        evaluation = thinker.think(prompt.evaluate_features(self.role, features_json, requirements), self.title)
        return evaluation

    def refine_feature(self, thinker, requirements, feature):
        refined_feature = thinker.think(prompt.refine_feature(self.role, requirements, feature), self.title)
        return refined_feature

    def split_and_refine(self,
                         thinker,
                         requirements,
                         max_refinement_attempts=1):

        # slit requirements into features
        features = self.split_requirements_to_features(thinker, requirements)

        # evaluate and split features until approved or max attempts reached
        refinement_attempts = 0
        while refinement_attempts < max_refinement_attempts:
            evaluation = self.evaluate_features(thinker, features, requirements)
            if "APPROVED AND READY FOR REFINEMENT" in evaluation:
                break
            features = self.split_requirements_to_features(thinker, requirements, features, evaluation)
            refinement_attempts += 1

        if refinement_attempts == max_refinement_attempts:
            say(self.title, "end of day for me (\"max refinement attempts\" is reached)")
        else:
            say(self.title, "we did well: requirements are split into features and approved for refinement")

        # refine each feature individually
        refined_features = []
        for feature in features:
            refined_feature = self.refine_feature(thinker, requirements, feature)
            feature_map = {"title": feature,
                           "acceptance_criteria": refined_feature}
            refined_features.append(feature_map)

        return refined_features

    def clarify_user_story(self,
                           thinker,
                           requirements,
                           user_story,
                           clarification_request):

            # use the thinker to clarify the user story
            clarified = thinker.think(prompt.clarify_user_story(self.role,
                                                                requirements,
                                                                user_story,
                                                                clarification_request),
                                           self.title)

            user_story.update_acceptance_criteria(clarified)

            return user_story

    def combine_user_stories(self, thinker, requirements, user_stories):
        say(self.title, "combining user stories...", message_color=color.DARKCYAN)
        return thinker.think(prompt.combine_user_stories(self.role, requirements, user_stories),
                             self.title)


    def idea_to_prompt(self, thinker, idea):
        say(self.title, "📚 creating detailed requirements ...🖋️", message_color=color.DARKCYAN)
        return thinker.think(prompt.idea_to_prompt(idea),
                             self.title,
                             mute=True)

    def idea_with_sketch_to_intel(self,
                                  thinker,
                                  idea,
                                  sketch):
        say(self.title, "🔍 collecting intel about the sketch ...", message_color=color.DARKCYAN)
        return thinker.see(prompt.idea_with_sketch_to_intel(idea, sketch),
                           sketch,
                           self.title)

    def idea_with_sketch_to_prompt(self,
                                   thinker,
                                   idea,
                                   sketch_intel):
        say(self.title, "📚 creating detailed requirements (for: idea + sketch) ...🖋️", message_color=color.DARKCYAN)
        return thinker.think(prompt.sketch_intel_to_requirements(idea, sketch_intel),
                             self.title)
