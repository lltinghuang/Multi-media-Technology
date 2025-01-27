# README
## Introduction to Multimedia Technology HW1

---

### Color Quantization and Dithering (1.ipynb)

- median_cut_quantize(img_arr):
    - parameter: 
        - img_arr is an array, which represent a partition of the image.
    - return: None.
    - others: 
        - get the average color of this partition and store it in the LUT.
        - keep the img_arr in the MAP.

- split_into_buckets(img_arr, depth):
    - parameter:
        - img_arr is an array, which represent a partition of the image.
        - depth is the desired number of recursions. The process will stop when depth = 0. We pass **n_bit_colors** as depth.
    - return: None.
    - others:
        - sort the colors in specific channel, and split the img_arr into two array by the median.
        - order: R, G, B channel.

- get_new_val(old_val, nc):
    - parameter: 
        - old_val: the color of orginal pixel.
        - nc: n_bit_colors.
    - return: new_val is the cloest color to **old_val** in the  LUT we built.
    ```python
        if nc == 3:
            diff = np.abs(LUT_3_bit - old_val)
            idx = np.argmin((np.sum(diff ** 2, axis=1)) ** 0.5)
            new_val = LUT_3_bit[idx]
    ```

- fs_dither(arr, nc):
    - parameter:
        - arr: an array that represent the image.
        - nc: n_bit_colors.
    - return: carr is an array which represent the result image after we did the diffusion dithering.

### Interpolation
- nearest_neighbor_interpolation(image, scale):
    - parameter:
        - image: an Image object
        - scale: an integer or float number
    - return: output_image

- bilinear_interpolation(image, scale):
    - parameter:
        - image: an Image object
        - scale: an integer or float number
    - return: output_image


### Photo enhancement
- RGB->YIQ space:
    - by Matrix Operations
    ```python
    yiq_from_rgb = np.array([[0.299, 0.587, 0.114],
              [0.59590059, -0.27455667, -0.32134392],
              [0.21153661, -0.52273617, 0.31119955]])
    OrigShape=img_arr.shape
    yiq_arr = np.dot(img_arr.reshape(-1,3), yiq_from_rgb.transpose()).reshape(OrigShape)
    ```
- gamma transform to Y channel:
    - the gamma value *y* is an exponent that defines a nonlinear relationship between the input level *r* and the output level *s* for a pixel transform function.
    - $s = r^y $, $0 \leq s \leq 1$
    ```python
    gamma = 4
    y_max = np.max(yiq_arr[:,:,0])
    yiq_arr[:,:,0] = y_max * ((yiq_arr[:,:,0]/y_max) ** gamma)
    ```
- YIQ->RGB space
    - multiply the inverse matrix of yiq_from_rgb
    ```python
    OrigShape=yiq_arr.shape
    rgb_arr = np.dot(yiq_arr.reshape(-1,3), np.linalg.inv(yiq_from_rgb).transpose()).reshape(OrigShape)
    ```
