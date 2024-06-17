import numpy as np

def delay_noise(signal):
    delay=np.random.randint(2*len(signal),4*len(signal),1)
    noise_signal=np.hstack((np.zeros(delay),signal))+np.random.normal(0,0.8,delay+len(signal))
    return noise_signal
