import os
import cv2

input_dir = r'C:\RoboLabCopy\data\masks'
output_dir = r'C:\RoboLabCopy\data\labels\train'

# Define the color values for each class in the mask
class_colors = {
    0: 29,  # Weed
    1: 76   # Lettuce
}

for j in os.listdir(input_dir):
    image_path = os.path.join(input_dir, j)
    # Load the binary mask
    mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    H, W = mask.shape
    polygons = []

    # Process each class separately
    for class_id, color in class_colors.items():
        # Create a binary mask for the current class
        class_mask = cv2.inRange(mask, color, color)
        
        # Find contours for the current class mask
        contours, _ = cv2.findContours(class_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Convert the contours to polygons
        for cnt in contours:
            if cv2.contourArea(cnt) > 200:
                polygon = [class_id]  # Start with the class_id as the first entry
                for point in cnt:
                    x, y = point[0]
                    polygon.append(x / W)
                    polygon.append(y / H)
                polygons.append(polygon)

    # Write the polygons to a file
    with open('{}.txt'.format(os.path.join(output_dir, j)[:-4]), 'w') as f:
        for polygon in polygons:
            # Write the class id and coordinates in the required format
            f.write('{} '.format(polygon[0]))  # Write class_id
            for p_, p in enumerate(polygon[1:]):
                if p_ == len(polygon) - 2:
                    f.write('{}\n'.format(p))
                else:
                    f.write('{} '.format(p))
        f.close()
