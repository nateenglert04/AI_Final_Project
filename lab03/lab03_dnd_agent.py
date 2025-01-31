from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Nathan Englert'
model = 'llama3.2'
options = {'temperature': 0.8, 'max_tokens': 150}
messages = [
  {'role': 'system', 'content': 'You are the Dungeon Master in a single player Dungeons and Dragons game. \
                                You are responsible for creating the world and the story for the game. The world should be detailed and should be explained on a large scale so the user understands the scope of their adventure. \
                                In the world, there should be a variety of interesting locations, characters, and items that the user can interact with. \
                                You are also responsible for determining the outcome of the user\'s actions and the consequences of those actions. \
                                You must always present the user\'s options in a consistent and concise listed, numerical format. \
                                The user\'s inventory, skills, and health should not be displayed in the chat, but you should keep track of it.'},
  {'role': 'user', 'content': 'Start the game.'}             
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below

  # Print the Dungeon Master's response
  print(f'Dungeon Master: {response.message.content}')

  # Add the Dungeon Master's response to the messages list
  messages.append({'role': 'assistant', 'content': response.message.content})

  # Get the user's input
  user_input = input('You: ')

  # Add the user's input to the messages list
  messages.append({'role': 'user', 'content': user_input})

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

