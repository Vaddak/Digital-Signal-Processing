import scipy.signal as signal
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

def mfreqz(b,a=1):
    w,h = signal.freqz(b,a, worN=1024)
    w=w[1:]
    h=h[1:]
    fig, ax1 = plt.subplots()
    plt.title('Frequency response')
    #ax1 = fig.add_subplot(111)
        
    ax1.plot(w, 20 * np.log10(abs(h)), 'b')

    
    ax1.set_ylabel('Amplitude [dB]')
    ax1.set_xlabel('Frequency [rad/sample]', color='b')    
    
    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    ax2.plot(w, angles, 'g')
    ax2.set_ylabel('Angle (radians)', color='g')
    plt.grid()
    plt.axis('tight')
    plt.show()
    
    
def impz(b,a=1):
    l = len(b)
    impulse = repeat(0.,l); impulse[0] =1.
    x = arange(0,l)
    response = signal.lfilter(b,a,impulse)
    subplot(211)
    stem(x, response)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Impulse response')
    subplot(212)
    step = cumsum(response)
    stem(x, step)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Step response')
    subplots_adjust(hspace=0.5)
    show()
def zeropoles(b, a=1):
    w,h = signal.freqz(b,a)
    sys1=signal.lti(b, a)
    #subplot(121)
    #plot(h.real, h.imag)
    #plot(h.real, -h.imag)
    #subplot(122)
    ang=np.arange(0.0,2*np.pi,0.01)
    xp=np.cos(ang)
    yp=np.sin(ang)
    plot(xp,yp,'--')
    plot(sys1.zeros.real, sys1.zeros.imag, 'o')
    plot(sys1.poles.real, sys1.poles.imag, 'x')
    #xlim(np.min(sys1.zeros.imag)-1, np.max(sys1.zeros.imag)+1)
    #ylim(np.min(sys1.zeros.imag)-1, np.max(sys1.zeros.imag)+1)
    show()
    
    
def computeZ(num, den, zeros, poles, data):
    sys1=signal.lti(num, den)
    w,h = signal.freqz(num, den)
    # agrego los polos y ceros al sistema
    zerosnew=np.hstack((sys1.zeros, zeros))
    polesnew=np.hstack((sys1.poles, poles))
    #gain=sys1.gain
    num2=np.poly(zerosnew)
    den2=np.poly(polesnew)
    #Impulse and step response
    figure(2)
    impz(num2, den2)
    show()
    #zero-poles diagrams
    zeropoles(num2, den2)
    show()
    #Frequency and phase response
    mfreqz(num2, den2)
    show()
    data2=signal.lfilter(num2, den2, data)
    subplot(211)
    plot(data)
    subplot(212)
    plot(data2)
    show()
    
