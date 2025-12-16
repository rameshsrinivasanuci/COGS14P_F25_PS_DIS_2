# %%
import numpy as np 
import sounddevice as sd
import warnings 

# %%
def pop_scales():
    ''' pop_scales()
        This function returns a dictionary containing the major scale in the 1st octave 
        returns:     notes           '''
    notes = dict()
    notes = {'A':440,'Bb':466,'B':494,'C':523,'C#':554,'D':587,'Eb':622,'E':659,'F':698,'F#':740,'G':784,'Ab':831}
    notes['names'] = ['A','Bb','B','C','C#','D','Eb','E','F','F#','G','Ab']
    notes['frequencies'] = np.array([440,466,494,523,554,587,622,659,698,740,784,831])
    return notes

# %%
def make_tone(frequency,duration,samplingrate=44100):
    ''' make_tone returns a pure tone 
        args:       frequency - frequency of the tone in hz
                    duration - duration of the tone in seconds 
        optional:   samplingrate - samplingrate in units of hz
                    default is 44100 
        returns:    tone   '''
    time = np.linspace(0, duration, int(duration*samplingrate)) 
    # The number of samples is the length of time X sampling rate. 
    tone = np.sin(frequency * time  * 2 * np.pi)
    return tone  

# %%
def play_sound(sample,volume = 0.05,samplingrate = 44100,block = True):
    ''' play_sound will apply a volume to a sound sample, and send it to the sound card to play
        warning: for safety reasons, this function limits output to 0.25 of the sound card range. 
        args:       sample -    numpy array to be played by the sound card
        optional:   volume -    in range 0 to 0.25 to scale the sound, default to 0.05. 
                                in case of volume > 0.25, returns to default value
                    samplingrate = sampling rate in hz, defaults to 44100
                    block = True or False. flag to block card while sound plays, default is True'''
    if volume > 0.25:
        warnings.warn('volume cannot be larger than 0.25, reset to 0.05')
        volume = 0.05
    if max(sample) != 0: 
        sample  = volume*sample/np.max(np.abs(sample)) # FOR SAFETY.  PLEASE LIMIT THE MAXIMIM VOLUME!   
    sample = 32767*sample # scale to the range of the sound card.
    sample  = sample.astype(np.int16) # convert to 16 bit integers. 
    sd.play(sample, samplingrate, blocking=block) 

# %% [markdown]



