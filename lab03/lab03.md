# Prompt Engineering Process

**ATTEMPT 1** 
Provided the attempt from attempts.txt, the 'Dungeon Master' struggled providing an initial response to the user, which hinders and prevents the user from interacting with the game. 

For the next attempt, I am going to try and alter the prompt that I had given the AI model so that it is capable of providing that initial response. It will be integral for understanding the game and giving a better flow to the user so you can hop right in to the fun. 

Also, I plan on adding more max_tokens to the parameters so that the AI can give a more detailed scenery of the world the user plans on playing in. 


**ATTEMPT 2** 
In this attempt, I decided to exit early before allowing the AI to give a real prompt. My idea for the 'Dungeon Master' to give its first response was not successful and ended in the same outcome of Attempt 1.  

I assume there will be a way to implement this story building element in code, so I will attempt to do so. 


**ATTEMPT 3** 
I successfully figured out how to start the game before entering the chat loop. I did so by adding a user role to the message list and making it start the game. 

Now after this troubleshooting is done, I want to fine tune the model so that it provides the best and most consistent experience to the user.  

First, I noticed some inconsistencies when prompting the user with what they can do. I will change the initial Dungeon Master prompt so that it will always display the user's options with a list of numbers (i.e. 1,2,3,4,etc.). Furthermore, I am going to alter the temperature of the model to see if it gives any intriguing game elements I would like to keep for the future. 

 
**ATTEMPT 4** 
From the new Dungeon Master prompt, the user is correctly given 3 options so that they can respond with either 1, 2, or 3. 

From the new temperature fine tuned parameter, I personally believe the story that was generated was much more interesting with an abundance of descriptives that excite the user with what choice to make. However, from the previous attempts, the Dungeon Master does not display any equipment, skill points, or health. In my opinion, I feel these elements to the game are neglible and/or clutter for what I want. When going further with the AI project I would like to implement these elements, but for the purposes of this project, I like how the game is structured in a 'Choose Your Own Story" format. 

For the next attempt, I want to fine tune the prompt so that I can get interesting NPCs and have a larger scope of the game's environment. 


**ATTEMPT 5** 
After this attempt, I am dissappointed with the uniqueness of the story and will increase the temperature once again.  

Also, within the prompt I am going to make it so the user is not given a display of their inventory since I believe it is more clutter than necessary right now.  

Once these aspect are fine tuned, I feel the model will be good for user enjoyment since the story will always be intriguing. 


**ATTEMPT 6** 
The prompt was not definitve enough for the AI model to understand what I wanted the Dungeon MAster to do. In this case, I will quickly fine tune the prompt so that it is more consistent with what I want the user to interact with. 


**ATTEMPT 7** 
I am happy with where my Dungeons and Dragons game has gone and how it turned out. I feel that the stories provided enough interactivity and excitement for the user to be pleased with their experience. 

 