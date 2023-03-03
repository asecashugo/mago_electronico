import config
import openai

f=open("file.mp3",'rb')
transcript=openai.Audio.translate("whisper-1",f)
print(transcript)

question=transcript

completion=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"Answer in json format yes/no/I don't know, your level of confidence from 0 to 100 and a short answer in <200 characters to the following question:{question}"}])
print(completion.choices[0].message.content)