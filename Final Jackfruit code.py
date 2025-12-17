import cv2
import os

def convert_to_grayscale_opencv(input_path, output_path):
    try:
        with open(input_path, 'r') as f:
             pass # Will only execute if the file exists
        
        # Read the image from the specified path
        color_img = cv2.imread(input_path) 
        
        if color_img is None:
            print(f"Error: Could not open or find the image at '{input_path}'")
            return
        
        # Resize and display the original color image
        resized_img1 = cv2.resize(color_img, (600, 500)) 
        cv2.imshow("Image window", resized_img1)
        cv2.waitKey(0) # Wait indefinitely for a key press
        cv2.destroyAllWindows() # Close all opened windows

        # Convert the color image (BGR) to grayscale
        grayscale_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY) 

        # Save the grayscale image to the output path
        cv2.imwrite(output_path, grayscale_img) 

        print(f"✅ Success: Grayscale image saved to '{output_path}'.") 

        # Resize and display the resulting grayscale image
        resized_img2 = cv2.resize(grayscale_img, (600, 500))

        cv2.imshow("Image", resized_img2)
        cv2.waitKey(0) # Wait indefinitely for a key press
        cv2.destroyAllWindows() # Close all opened windows

    
    except FileNotFoundError as e:
        print(f"❌ File Not Found Exception: {e}")
        print("Please check if the input file path and name are correct.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the input image file path
    input_filename = r"Assets/Sunrise.jpg"
    
    # Generate the output filename by adding '_opencv_grayscale' before the extension
    base, ext = os.path.splitext(input_filename)
    output_filename = base + "_opencv_grayscale" + ext
    
    # Call the conversion function
    convert_to_grayscale_opencv(input_filename, output_filename)



