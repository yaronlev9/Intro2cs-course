from wave_helper import *
import os.path
import copy
import math

NOTE_CHART={'A':440,'B':494,'C':523,'D':587,'E':659,'F':698,'G':784,'Q':0}
MAX_VOLUME=32767
MIN_VOLUME=-32768
FORMAT='.wav'

def average(x, y, z=0, divider=2):
    """returns the average value of up to 3 numbers"""
    return int((x+y+z)/divider)

def revers_audio (audiofile):
    """this function reverses the data on the
    given file and returns a new file"""
    new_audiofile=audiofile[::-1]
    return new_audiofile



def speedup_audio (audiofile):
    '''this function recieves an audio file and speeds it
         2 times faster'''
    speed_audio = []
    for i in range(len(audiofile)):
        if i % 2 == 0:
            speed_audio.append(audiofile[i])
    return speed_audio

def make_avg_list(list):
    """creates a list of the average values of each speaker"""
    avg_list=[[] for k in range (len(list)-1)]
    for i in range(len(list)):
        for k in range (len(list[0])):
            if(i<len(list)-1):
                avg_list[i].append(average(list[i][k], list[i + 1][k]))
    return avg_list

def slowdown_audio(audiofile):
    """creates a new list of original values and average values in between"""
    avg_audio=make_avg_list(audiofile)
    slow_audio=[]
    for i in range(len(audiofile)*2-1):
        for k in audiofile:
            if(i%2==0 ):
                slow_audio.append(audiofile[i//2])
                break
            else:
                slow_audio.append(avg_audio[i//2])
                break
    return slow_audio

def volume_up(audiofile):
    """creates a new list of values which are
    1.2 times larger than the original values"""
    for samp in audiofile:
        if (samp[0]*1.2>=MAX_VOLUME or samp[0] * 1.2 <= MIN_VOLUME):
            if(samp[0]>0):
                samp[0]=MAX_VOLUME
            else:
                samp[0] = MIN_VOLUME
        else:
            samp[0] = int(samp[0] * 1.2)
        if (samp[1]*1.2>=MAX_VOLUME or samp[1] * 1.2 <= MIN_VOLUME):
            if(samp[1]>0):
                samp[1]=MAX_VOLUME
            else:
                samp[1] = MIN_VOLUME
        else:
            samp[1] = int(samp[1] * 1.2)
    return audiofile

def volume_down(audionfile):
    """creates a new list of values which are
       1.2 times smaller than the original values"""
    for samp in audionfile:
        samp[0] = int(samp[0] / 1.2)
        samp[1] = int(samp[1] / 1.2)
    return audionfile

def muffle_filter(audiofile):
    """creates a list of the average
    values of the surrounding items"""
    copy_audio=copy.deepcopy(audiofile)
    for i,samp in enumerate (audiofile):
        for j,side in enumerate(samp):
            if(i==0):
                samp[j]=average(copy_audio[i + 1][j], side)
                continue
            if (i == len(audiofile)-1):
                samp[j] =average (copy_audio[i - 1][j], side)
                continue
            samp[j]=average(copy_audio[i - 1][j], side, copy_audio[i + 1][j],3)
    return audiofile

def main_menu():
    """the main menu of the program: help the user
    navigate to different features"""
    print("main menu:(please enter the number of desired action)\n"
          "1.change wav file\n"
          "2.merge two wav files\n"
          "3.compose a tune in wav format\n"
          "4.exit program")
    inp=input()
    while inp!='4':
        if inp=='1':
            change_wav_menu()
            break
        elif inp == '2':
            merge_wav_menu()
            break
        elif inp == '3':
            compose_wav_menu()
            break
        else:
            inp=input("please enter a valid input (1 or 2 or 3 or 4):")

def change_wav_menu(filename=''):
    """a menu that helps the user change an audio file"""
    editedaudio=[]
    if filename is '':
        print("please enter the name of the file you want to change:")
        filename=input()
        while (not os.path.isfile(filename) or
               filename[len(filename)-4:len(filename)]!=".wav"):
            #checking that the file is as expected
            filename=input("this file doesn't exist please "
                           "enter an existing file name:")
    frame_rate,audiodata=load_wave(filename)
    print("change wav menu:(please enter the number of desired action)\n"
    "1.reverse the audio\n"
    "2.speed up the audio\n"
    "3.slow down the audio\n"
    "4.increase volume of the audio\n"
    "5.decrease volume of the audio\n"
    "6.muffle the audio")
    inp=input()
    while inp not in ['1','2','3','4','5','6']:
        inp=input("please enter a valid input (a number from 1 to 6):")
    if inp == '1':
        editedaudio=revers_audio(audiodata)
    if inp == '2':
        editedaudio =speedup_audio(audiodata)
    if inp == '3':
        editedaudio= slowdown_audio(audiodata)
    if inp=='4':
        editedaudio =volume_up(audiodata)
    if inp=='5':
        editedaudio =volume_down(audiodata)
    if inp=='6':
        editedaudio =muffle_filter(audiodata)
    transfer_menu(editedaudio,frame_rate,filename)



def transfer_menu(audiodata,frame_rate,filename=""):
    """a menu taht helps the user save or change and audio file"""
    print("transfer menu:(please enter the number of desired action)\n"
    "1.save the audio\n"
    "2.change the audio")
    inp=input()
    while inp not in ['1','2']:
        inp=input("please enter a valid input (1 or 2):")
    if inp=='1':
        new_name=input("please enter the new file name:")
        save_wave(frame_rate,audiodata,new_name)
        main_menu()
    elif inp=='2':
        change_wav_menu(filename)

def merge_wav_menu():
    """a menu that helps the user merge two audio files"""
    inp=input("please enter the names of the files you "
              "wish to merge(each path inside <path>)")
    index = inp.find(FORMAT)
    print(inp[index+4:index+6])
    while not "><" in inp[index+4:index+6]:
        inp=input("please enter files using the proper "
                  "format(<file1.wav><file2.wav>):")
    path1=inp[1:index+4]
    path2=inp[index+6:len(inp)-1]
    while (not os.path.isfile(path1) or not os.path.isfile(path2)
            or path1[len(path1)-4:len(path1)]!=FORMAT or
            path2[len(path2)-4:len(path2)]!=FORMAT):
        #checking that the files are as expected
        inp = input("the files do not exist please try "
                    "again:(each path inside <path>)")
        index = inp.find(FORMAT)
        path1 = inp[1:index + 4]
        path2 = inp[index + 6:len(inp) - 1]
    merge_files(path1,path2)

def merge_equal_rates(data1, data2):
    '''this function recieves 2 datas from 2 files
     with equal rate and returns the merge'''
    new_data=[]
    if len(data1) == len(data2):
        for i in range(len(data1)):
            sample0 = average(data1[i][0],data2[i][0])
            sample1 = average(data1[i][1],data2[i][1])
            new_data.append([sample0, sample1])
        return new_data
    elif len(data1) < len(data2):
        for i in range(len(data1)):
            sample0 =average(data1[i][0],data2[i][0])
            sample1 =average(data1[i][1],data2[i][1])
            new_data.append([sample0, sample1])
        new_data += data2[len(data1):]
        return new_data
    else:
        for i in range(len(data2)):
            sample0 =average(data1[i][0],data2[i][0])
            sample1 =average(data1[i][1],data2[i][1])
            new_data.append([sample0, sample1])
        new_data += data1[len(data2):]
        return new_data

def GCD(x,y):
    """"this function returns the largest integer
     that divides the two numbers"""
    while y>0:
        x,y=y,x%y
    return x

def convert_high_rate_data(data, gcd, sample_rate1, sample_rate2):
    """this function recieves the data with the highest
    frame rate and returns the given data with the frame rate
    of the lowest"""
    new_data = []
    for i in range(0, len(data), int(sample_rate2 / gcd)):
        j = i
        while j < i + int(sample_rate1 / gcd) and j < len(data):
            new_data.append(data[j])
            j += 1
    return new_data

def merge_files(filename1,filename2):
    """this function merges the datas of the
    2 given files and returns a new file"""
    sample_rate1,data1=load_wave(filename1)
    sample_rate2,data2=load_wave(filename2)
    if sample_rate1==sample_rate2:
        new_data = merge_equal_rates(data1, data2)
        transfer_menu(new_data,sample_rate1)
    elif sample_rate1<sample_rate2:
        gcd=GCD(sample_rate1,sample_rate2)
        new_data2 = convert_high_rate_data(data2, gcd, sample_rate1, sample_rate2)
        new_data=merge_equal_rates(data1, new_data2)
        transfer_menu(new_data,sample_rate1)
    elif sample_rate2<sample_rate1:
        gcd=GCD(sample_rate1,sample_rate2)
        new_data1 = convert_high_rate_data(data1, gcd, sample_rate2, sample_rate1)
        new_data=merge_equal_rates(new_data1, data2)
        transfer_menu(new_data,sample_rate2)

def make_easy_list(string):
    """makes a list of lists each item holds
    a note and how many time it should be played"""
    easy_list=[]
    note=''
    times=''
    for i in string:
        if note!='' and i in NOTE_CHART:
            easy_list.append([note,int(times)])
            note=''
            times=''
        if i in NOTE_CHART:
            note=i
        elif i!=" " and i!="\n":
            times+=i
    easy_list.append([note, int(times)])
    return easy_list

def compose_wav_menu():
    """a menu that helps the user compose an audio file"""
    print("please enter the name of the composing file")
    inp=input()
    while inp[len(inp)-4:len(inp)]!=".txt" or not os.path.isfile(inp):
        inp=input("the file does not exist or ins't "
                  "in txt format please try again:")
    composition_file=open(inp)
    comp_list=make_easy_list(composition_file.read())
    composition_file.close()
    audio_data = compose_audio(comp_list)
    transfer_menu(audio_data,2000)

def compose_audio(comp_list):
    """composes audio using a list of notes and
    how may time they should be played"""
    audio_data = []
    for i in comp_list:
        for j in range(i[1] * 125):
            if i[0] is 'Q':
                audio_data.append([0, 0])
                continue
            spc = 2000 / NOTE_CHART[i[0]]
            sample = int(MAX_VOLUME * math.sin(math.pi * 2 * (j / spc)))
            audio_data.append([sample, sample])
    return audio_data

if __name__=="__main__":
    main_menu()