import os, time
from jemma.tools import color, say, image_path_to_data

import ollama
import replicate
from anthropic import Anthropic
from openai import OpenAI

class Thinker:

    # defining init method for class
    def __init__(self, model_name):
        self.model_name = model_name

    def __str__(self):
        return f"{self.__class__.__name__} 🧠 {self.model_name} ✅"

    def think(prompt, who="user", sleep_time=0):
        raise NotImplementedError("can't think without a implementation. try creating Ollama that is based on me")

class Ollama(Thinker):

    def __init__(self, model_name):
        super().__init__(model_name)

    def think(self, prompt, who="user", action="", mute=False, sleep_time=0):
        thinking = ollama.generate(model=self.model_name,
                                   prompt=prompt,
                                   options={'num_predict': 4096},
                                   stream=True)
        if action != "" or not mute:
            say(who, action)

        response = ""
        for word in thinking:
            response += word['response']
            if not mute:
                print(word['response'], end="")

        return response

class Replicate(Thinker):

    def __init__(self, model_name):
        super().__init__(model_name)

    def think(self, prompt, who="user", action="", mute=False, sleep_time=0):

        if action != "" or not mute:
            say(who, action)

        response = ""
        for event in replicate.stream(
            self.model_name,
            input={
                "prompt": prompt,
                # "max_new_tokens": 32000,
                # "max_length": 32000
            },
        ):
            response = response + str(event)
            if not mute:
                print(str(event), end="")

        # print(color.RED + ">>" + response + "<<" + color.END)

        return response

class Claude(Thinker):

    def __init__(self, model_name):
        super().__init__(model_name)

        ## make sure ANTHROPIC_API_KEY is exported in shell
        ## or it is exported in a .env file
        self.client = client = Anthropic()

    def see(self,
            prompt,
            image_path,
            who="user",
            max_tokens=1024,
            action="👀 looking at the image... ",
            mute=False,
            sleep_time=1):

        say(who, action + image_path)

        image_data, image_type = image_path_to_data(image_path).values()

        response = self.client.messages.create(
                model=self.model_name,
                max_tokens=max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": image_type,
                                    "data": image_data,
                                    },
                                },
                            {
                                "type": "text",
                                "text": prompt,
                                }
                            ],
                        }
                    ],
                )

        saw_this = response.content[0].text

        # print(color.RED + f">> {saw_this} <<" + color.END)

        return saw_this

    def think(self, prompt, who="user", action="", mute=False, sleep_time=1): # sleep not to exceed the rate limit

        if action != "" or not mute:
            say(who, action)

        time.sleep(sleep_time)

        response = ""
        with self.client.messages.stream(max_tokens=4096,
                                         messages=[{"role": "user",
                                                    "content": prompt}],
                                         model=self.model_name
        ) as stream:
          for text in stream.text_stream:
              if not mute:
                  print(text, end="", flush=True)
              response += text

        # print(color.RED + ">>" + response + "<<" + color.END)

        return response

class ChatGPT(Thinker):

    def __init__(self, model_name):
        super().__init__(model_name)

        ## make sure OPENAI_API_KEY is exported in shell
        ## or it is exported in a .env file
        self.client = client = OpenAI()

    def think(self, prompt, who="user", action="", mute=False, sleep_time=2): # sleep not to exceed the rate limit

        if action != "" or not mute:
            say(who, action)

        time.sleep(sleep_time)

        response = ""
        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user",
                       "content": prompt}],
            max_tokens=4096,
            stream=True,
        )
        for chunk in stream:
            thought = chunk.choices[0].delta.content or ""
            if not mute:
                print(thought, end="")
            response += thought

        # print(color.RED + ">>" + response + "<<" + color.END)

        return response

## makes a brain from cli arguments
def make_brain(args, default_models = {'claude': 'claude-3-haiku-20240307',
                                       'openai': 'gpt-3.5-turbo',
                                       'ollama': 'gemma:7b-instruct-v1.1-fp16',
                                       'replicate': 'mistralai/mixtral-8x7b-instruct-v0.1'}):

    model_classes = {
        'claude': Claude,
        'openai': ChatGPT,
        'ollama': Ollama,
        'replicate': Replicate
    }

    # make it with the first model argument that is provided
    for model_name in model_classes.keys():
        model_arg = getattr(args, model_name, None)
        if model_arg is not None:

            model_name_to_use = default_models[model_name] if model_arg is True else model_arg

            brain = model_classes[model_name](model_name_to_use)
            print(color.GRAY_MEDIUM + f"{brain}" + color.END)
            return brain

    # ollama by default
    brain = Ollama(default_models['ollama'])
    print(color.GRAY_MEDIUM + f"{brain}" + color.END)

    return brain

# ---- local models

# nous-hermes2:10.7b-solar-q4_0
# nous-hermes2:10.7b-solar-q6_K
# mistral:7b-instruct-v0.2-fp16
# dolphin-mistral:7b-v2.6-dpo-laser-fp16
# mixtral:8x7b-instruct-v0.1-q4_K_M
# deepseek-coder:6.7b-instruct-fp16
# gemma:7b-instruct-fp16

# ---- claude models

# claude-3-haiku-20240307
# claude-3-sonnet-20240229
# claude-3-opus-20240229

# ---- chatgpt models

# gpt-3.5-turbo-0125   (16K context window)
# gpt-4-32k
# gpt-4-turbo-preview  (128K context window)
