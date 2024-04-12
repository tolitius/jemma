try:
    from pyreadline3 import Readline # windows support
    readline = Readline()
except ImportError:
    import readline

from jemma.tools import color

def create_user_stories(brain,
                        project_manager,
                        business_owner,
                        engineer):

    project_manager.meet_to_create_user_stories(brain,
                                                business_owner)

    ## have another business owner to review the stories
    # project_manager.meet_to_review_user_stories(brain,
    #                                            business_owner,
    #                                            stories)

    project_manager.meet_to_refine_user_stories(brain,
                                                engineer,
                                                business_owner)

def build_user_stories(brain,
                       project_manager,
                       business_owner,
                       engineer):
    project_manager.meet_to_create_user_stories(brain,
                                                business_owner)
    # project_manager.meet_to_combine_user_stories(brain,
    #                                              business_owner)
    project_manager.user_stories_to_requirement()
    return project_manager.meet_to_build_prototype(brain,
                                                   engineer)


def ask_for_feedback():

    # make sure the cursor works
    readline.parse_and_bind('set editing-mode emacs')

    while True:
        feedback = input("\n" + color.GREEN + "tell me how to make it better > " + color.END)
        if feedback.strip():
            return feedback
        elif feedback == "":
            return None

def build_prototype(brain,
                    project_manager,
                    business_owner,
                    engineer,
                    prompt = None,
                    sketch = None):

    if prompt:
        project_manager.meet_to_create_requirements(brain,
                                                    business_owner,
                                                    prompt,
                                                    sketch)
    prototype = project_manager.meet_to_build_prototype(brain,
                                                        engineer)

    while True:
        feedback = ask_for_feedback()
        if not feedback:
            break

        prototype = project_manager.meet_to_refactor(brain,
                                                     engineer,
                                                     prototype,
                                                     feedback)

    return prototype

def test_prototype(brain,
                   project_manager,
                   tester):
    return project_manager.meet_to_test_prototype(brain,
                                                  tester)
