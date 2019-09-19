#!miskiln1278
#data sinyal diambil dari database universitas michigan

if __name__ == "__main__":
    import numpy as np
    import pylab as plt
    import math as m
    from PyEMD import CEEMDAN
    import scipy.io.wavfile as wav

    maxImf = -1
    DTYPE = np.float64
    N = 8000
    tMin, tMax = 0, 1
    T = np.linspace(tMin, tMax, N, dtype=DTYPE)
    # S = 6*T +np.cos(8*np.pi**T)+0.5*np.cos(40*np.pi*T)
    file = 'as_early_uw_8k.wav'
    sig, fs = wav.read(file)
    w = np.array(fs)
    s = w/32767
    S = s[0:8000]
    
    cemdan = CEEMDAN()
    cemdan.FIXE_H = 5
    cemdan.nbsym = 1
    cemdan.spline_kind = 'cubic'
    cemdan.DTYPE = DTYPE
    
    imfs = cemdan.ceemdan(S, T, maxImf)
    imfNo = imfs.shape[0]
    
    c = 1
    r = np.ceil((imfNo+1)/c)
    
    plt.figure(1)
    plt.ioff()
    plt.subplot(r, c, 1)
    plt.plot(T, S, 'r')
    plt.xlim((tMin, tMax))
    plt.title("Original signal")

    for num in range(imfNo):
        plt.subplot(r,c,num+2)
        plt.plot(T, imfs[num], 'g')
        plt.xlim((tMin, tMax))
        plt.ylabel("Imf "+str(num+1))
   
    plt.tight_layout()    
    plt.show()

