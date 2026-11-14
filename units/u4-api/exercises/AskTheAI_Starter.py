# WARM-UP BUG: this program should print a joke, but it prints something strange. Run it, read the output, find the line, fix it.
# CLASSROOM STAND-IN: ZONE A is a fake Gemini client that returns fixed answers - it needs no key and no internet.
# Do not edit ZONE A. (For a live class with a real key the teacher replaces ZONE A - see the teacher's notes.)
# Documented bug (teacher): print(response) prints the whole response object; the text is in response.text.


# ===== ZONE A - CLASSROOM STAND-IN. Do not edit. =====
# It takes the place of the two real lines  `from google import genai`  and  `client = genai.Client(...)`.
SIMULATE_ERROR = None          # teacher demo: set to "429" or "503" to see what an overloaded service looks like


class FakeReply:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "GenerateContentResponse(candidates=[...], usage_metadata=...)"


class FakeModels:
    def __init__(self):
        self.calls = 0

    def generate_content(self, model, contents):
        self.calls += 1
        if SIMULATE_ERROR == "429":
            raise RuntimeError("429 RESOURCE_EXHAUSTED (stand-in simulation)")
        if SIMULATE_ERROR == "503":
            raise RuntimeError("503 UNAVAILABLE (stand-in simulation)")
        text = contents.lower()
        if "joke" in text:
            answer = "Why do programmers prefer dark mode? Because light attracts bugs."
        elif "moon" in text:
            answer = "The Moon is about 384,000 km from Earth, on average."
        elif "birthday" in text:
            answer = "Happy birthday, dear grandma! You are the warmest, kindest person we know."
        elif "dessert" in text:
            answer = "Crazy dessert: layer everything on the list with whipped cream, chill it, and enjoy."
        elif "schedule" in text:
            answer = "15:00 snack and homework, 16:30 short break, 17:00 the rest of the tasks, then free time."
        else:
            answer = "This is a fixed answer. A real model would answer your prompt here."
        return FakeReply("[stand-in] " + answer)


class FakeClient:
    def __init__(self):
        self.models = FakeModels()


client = FakeClient()
# ===== end of ZONE A =====

# ===== ZONE B - your program =====

# Warm-up: send a prompt and print the answer
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me a short joke about programmers")
print(response)


# Task 1: wrap the call in a function called ask_the_ai
#   - it takes one parameter: my_prompt
#   - it sends my_prompt to the model (the same two lines as the warm-up)
#   - it RETURNS the text of the answer (return, not print)
# Then call it from the main program with "What is the distance between the Earth and the Moon?",
# save the result in a variable, and print it.


# Task 2: a dynamic prompt
#   - read two things with input(): a grandma's name and a good trait of hers
#   - build the prompt with an f-string, for example:
#       f"Write a short birthday greeting for {name}, who is a very {trait} grandmother."
#   - print the prompt, send it with ask_the_ai, and print the answer


# Task 3: collect first, ask once
#   - all_ing = ""  and a while loop that continues until the user types done
#   - each time, read an ingredient and add it to all_ing, with a comma and a space after it
#   - AFTER the loop (not indented): build a prompt that asks for a crazy dessert that uses only the
#     ingredients in all_ing, send it with ask_the_ai ONCE, and print the answer


# If time: do not waste a call on bad input
#   - if the grandma's name is shorter than 2 letters, print a warning and do not call the AI
#   - if the trait is empty (""), use a default trait such as "wonderful"
