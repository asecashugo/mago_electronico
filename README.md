I used to play this game that my grandma gave me when I was a kid. My brother and I learnt to read with the questions on the board. We would point the robot at a question, read it out loud, wonder for a while and then transfer it to the second stand. 
It would suddenly spin and point at the right answer without hesitation ([see it in action](https://www.youtube.com/watch?v=QE0VkjnnxO4)) Magic! It may look naîve today, but it was brilliant at the time.
![image](https://github.com/user-attachments/assets/4f07182b-2387-4238-b37f-2104f9822e7b)

![image](https://github.com/user-attachments/assets/df2ae795-7fbf-4cd8-bbab-7d2661dafa27)


Anyways, we outgrew it long ago. Still loved he game for its ingenuity and wanted to honor it with a retrofit. So here's what I did:

I replaced the box for a smaller, deeper one, enough to house a servo coupled with a bunch of magnets

![image](https://github.com/user-attachments/assets/f511cc43-9db4-4718-b899-452bf2843b60)

Wired a rpi4 with a cheap e-paper module (drew some fan art while at it) and a microphone:

![image](https://github.com/user-attachments/assets/95f5fb26-563f-4393-a092-272b0c2ac8f3)

Used [openAI api](https://openai.com/api/) (and my credit card) for:
- whisper: speech-to-text the audio prompt
- chat completion (ChatGPT 3.5 at the time)
- Wrapped the prompt to coerce the model into a binary classification to Yes/No

https://github.com/user-attachments/assets/b81977b4-848b-455f-bce3-0b6d81b9ba03

My 2.0 robot wizard will now answer yes/no to any question (not just the hundred in the original game). It will also point gracefully at a 'YES' or 'NO' badge on the board with its cane and provide some context infrmation on the paper screen.

Look at it go :)

https://github.com/user-attachments/assets/463e31e9-834f-4b6a-a2ed-f2ab186aa3f2

