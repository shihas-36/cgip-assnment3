import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_and_display_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
        return
    
    height, width, channels = image.shape
    print(f"Dimensions: {width}x{height}")
    print(f"Shape: {image.shape}")
    
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    resized = cv2.resize(image, (width // 3, height // 2), interpolation=cv2.INTER_AREA)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    cv2.imwrite("grayscale.jpg", grayscale)
    cv2.imwrite("binary.jpg", binary)
    cv2.imwrite("resized.jpg", resized)
    cv2.imwrite("blurred.jpg", blurred)

    print("Images processed and saved successfully.")
    

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))  

    axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')

    axes[0, 1].imshow(grayscale, cmap='gray')
    axes[0, 1].set_title('Grayscale Image')
    axes[0, 1].axis('off')

    axes[1, 0].imshow(binary, cmap='gray')
    axes[1, 0].set_title('Binary Image')
    axes[1, 0].axis('off')

    axes[1, 1].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
    axes[1, 1].set_title('Resized Image')
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.show()
image_path = "input.jpg"
process_and_display_image(image_path)