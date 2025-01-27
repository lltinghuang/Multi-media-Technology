import numpy as np
import cv2
import matplotlib.pyplot as plt


##for(a)
def subplot(points , result1 , result2 , img):
    plt.imshow(img)
    plt.scatter(points[:, 0], points[:, 1],  s=0.5)
    plt.plot(result1[:, 0], result1[:, 1], 'b-' ,linewidth=0.5)

    plt.plot(result2[:, 0], result2[:, 1], 'r-' ,linewidth=0.5)
    plt.savefig('output/1a.png')
    plt.close()

##for(b)
def plot(points , result , img):
    plt.imshow(img)
    plt.scatter(points[:, 0], points[:, 1],  s=5)
    plt.plot(result[:, 0], result[:, 1], 'r-' ,linewidth=0.5)
    plt.savefig('output/1b.png')
    plt.close()


def bezier_curve(control_points, t):
    n = len(control_points) - 1
    result = 0
    for i in range(n + 1):
        coefficient = np.math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
        result += coefficient * control_points[i]
    return result

def nearest_neighbor_interpolation(image, scale):
    height, width = image.shape[:2]

    new_width = int(width * scale)
    new_height = int(height * scale)

    output_image = np.zeros((new_height, new_width, image.shape[2]), dtype=np.uint8)
    for y in range(new_height):
        for x in range(new_width):
            input_x = int(x / scale)
            input_y = int(y / scale)
            output_image[y, x, :] = image[input_y, input_x, :]

    return output_image

def main():      
    # Load the image and points
    img = cv2.imread("./bg.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    points = np.loadtxt("./points.txt")
    
    
    ##You shold modify result1 , result2 , result
    ## 1.a
    t_low = np.linspace(0, 1, 3)
    t_high = np.linspace(0, 1, 101)
    result1 = []
    result2 = []

    for i in range(0, points.shape[0], 3):
        result1 += [bezier_curve(points[i:i+4], t) for t in t_low]
        result2 += [bezier_curve(points[i:i+4], t) for t in t_high]

    result1 = np.array(result1)
    result2 = np.array(result2)
    subplot(points  , result1 , result2 , img)
    
    # 2.a 
    scaled_img = nearest_neighbor_interpolation(img, 4)
    scaled_points = points * 4
    result = []
    for i in range(0, scaled_points.shape[0], 3):
        result += [bezier_curve(scaled_points[i:i+4], t) for t in t_high]
    result = np.array(result)
    plot(scaled_points  , result , scaled_img)
    
    
    

if __name__ == "__main__":
    main()