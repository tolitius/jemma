class UserStory:
    def __init__(self, title, acceptance_criteria, description=""):
        self.title = title
        self.description = description
        self.acceptance_criteria = acceptance_criteria

    def update_acceptance_criteria (self, acceptance_criteria):
        self.acceptance_criteria = acceptance_criteria

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nAcceptance Criteria:\n{self.acceptance_criteria}"

class Feature:
    def __init__(self, requirements, title="feature"):
        self.title = title
        self.requirements = requirements
        self.user_stories = {}

    def add_user_story(self, user_story):
        self.user_stories[user_story.title] = user_story

    def update_user_story(self, title, updated_user_story):
        self.user_stories[title] = updated_user_story

    def get_user_story(self, title):
        return self.user_stories.get(title)

    def get_user_stories(self):
        return self.user_stories

    def export_user_stories_titles_and_criteria(self):
        export_list = []
        for title, user_story in self.user_stories.items():
            export_list.append(f"Title: {user_story.title}\nAcceptance Criteria:\n{user_story.acceptance_criteria}")
        return "\n\n".join(export_list)
