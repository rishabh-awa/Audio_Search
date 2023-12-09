import whisper
import openai
import subprocess



#transcript model
def transcribe(url):
    text=""
    model = whisper.load_model("base")
    result = model.transcribe(url)
    for i in result["segments"]:
        text += "|text:"+i['text']+"-start time:"+str(i["start"])+"-end time"+str(i["end"])+"|"
    return(text)



#gpt model for question answer
def questioA(text,prompt,url):
    openai.api_key=	"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"
    message = prompt
    messages = f"You are given a video transcript:'{text}' containing text and starting and ending timestamps in format |text:'text'-start time:'start'-end time:'end'| return me the starting and ending timestamps for about 10 to 20 seconds long which contain information related to and relate to {message} the most.The answer must always be in format start:Start time-end:end time"

    chat = openai.completions.create(
            model="gpt-3.5-turbo-instruct",prompt=messages,temperature=0,max_tokens=100,top_p=1,frequency_penalty=0.0,presence_penalty=0.0
        )
    reply = chat.choices[0].text
    print(f"|| {reply} ||")
    reply = reply.split("-")
    s = reply[0].split(":")
    s= float(s[1])
    r = reply[-1].split(":")
    r=float(r[1])
    #trimming the video/audio
    if "mp3" in url:  
        path = r"C:\Users\Shiv\Desktop\Transcript\frontend\src\output.mp3"
    else:
        path = r"C:\Users\Shiv\Desktop\Transcript\frontend\src\output.mp4"
    command = ['ffmpeg',
               '-i',url,
               '-ss',str(s),
               '-to',str(r),
               '-c','copy',
               path]
    subprocess.run(command)
    return path
#transcribe("C:\Users\Shiv\Desktop\Transcript\backend\one.mp3")
