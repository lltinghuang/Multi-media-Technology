# README
## Introduction to Multimedia Technology HW2

---

### Q1. DCT image compression (1.ipynb)
- dct_compress(img_arr, n, m):
    - divide img_arr into blocks of 8*8 pixels
    - for each block:
        1. call * dct2()*
        2. only remain upper-left n-by-n coefficients
        3. quantized by quantization table (Unit3 slide p.91)
    - call *uniformQ()* 
    - return 
        1. the quantized DCT coefficients (compressed_blocks)
        2. delta (for decompression)
- dct2(block):
    - Discrete Cosine Transform
    - implement equation (8.17) on the slide Unit3 p.64
    - return the transformed coefficients
- uniformQ(rq, gq, bq, m):
    - input the quantized coefficients per channel, respectively and an integer value m
    - apply uniform quantization and save the each coefficients with m bits
    - return the quantized coefficient which can be represent with m bits. Also return delta for the preparation of decompression
    
    for example: 
    ```python
        r_delta = (np.max(rq) - np.min(rq)) / (2**m - 1)  
        r_coef = np.round(rq / r_delta)
    ```

- dct_decompress(compressed_blocks, delta, n):
    - reverse the compression process
    - first, do *unquantization()*
    - second, divide image into blocks of 8*8 pixels
    - for each block: 
        1. multiply the quantization table
        2. call *idct2()* to get the coefficients for reconstructing the image
    - return the image 
- idct2(coefficients):
    - the inverse function of *dct2()*
    - implement equation (8.18) on the slide Unit3 p.64
    - return the coefficients 
- subsampling(ycbcr_arr):
    - input is an array on yCbCr color domain
    - implement 4:2:0 chrominance subsampling (refer Unit3 slide p.86)
    - return the array after subsampled 

### Q2. Filter audio signal (2.ipynb)
- filter(f_c, f_samp, N, t):
    - input:
        1. f_c is the cutoff frequency 
        2. f_sampe is the sampling frequency of the audio signal to be filterd
        3. N is the order of the filter; assum N is odd
        4. t indicates the filter type (1 for lowpass, 2 for highpass)
    - implement the lowpass filter and highpass filter (Unit4 slide p.72&76)
    - using Blackmann window function (Unit4 slide p.75)
    - return FIR filter (N-element array)
- bandpass(f_c1, f_c2, f_samp, N):
    - similar to *filter()*
    - frequency only between range(f_c1, f_c2) can pass through
#### Usage:
    - try to find suitable f_c and N
    - generate a filter as convolution mask
    - implement FIR filter function (Unit4 slide p.60)
    
- reduce sampling rate:
    - calculate the downsampling ratio by dividing the original sampling rate by the desired sampling rate of 2000 Hz
    - create an empty numpy array resampled_song to store the resampled signal
    - calculate the mean of each block of ratio samples in the original signal, storing the resulting value in the corresponding element of resampled_song.
- echo
    - implement the formula on Unit4 slide p.65
    - one-fold echo:
        ```python
        for i in range(len(data)):
            echo_song[i] = data[i] + 0.8*data[i-3200]
        ```
    - multiple-fold echo:
        ```python
        for i in range(len(data)):
            echo_song2[i] = data[i] + 0.8*echo_song2[i-3200]
        ```