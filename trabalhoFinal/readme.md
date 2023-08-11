# Final Project Digital Image Processing
## Locked Door Detector

### Attempt 1 - Detecting Image Edges
The first attempt to determine if the door was locked or not involved using a Gaussian blur
followed by the Canny edge detection algorithm from cv2 to see if it was possible to
identify the door lock in the locked image that didn't exist in the unlocked image. It might
have been possible with this approach, but I quickly realized it probably wouldn't be as
accurate and would be more complex to implement.

### Attempt 2 - Filtering the Door Lock Color
The second attempt was more efficient. Now, the grayscale RGB variations that have a higher
concentration on the door lock are filtered. Then, the quantity of pixels is counted based on this filtering,
and it's compared with the unlocked image. As the lock won't be visible on the unlocked door,
it's expected that the locked door will have more pixels. The issue with this attempt is due to
color variation caused by different lighting conditions.

### Attempt 3 - Detecting Door Lock using Machine Learning
For this attempt, a machine learning algorithm in Python was used to distinguish locked doors from
unlocked ones. Thirteen pictures of a locked door and twelve pictures of an unlocked door were
used to train the algorithm, which operated with 100% accuracy.


![image](https://github.com/PedroRamos360/ProcessamentoDigitalImagens/assets/53490820/654e822a-82c2-4a28-ac38-15ce9bb7a6c1)
![image](https://github.com/PedroRamos360/ProcessamentoDigitalImagens/assets/53490820/b43b55a9-04ba-4da0-8ad4-bd31514cf5e1)

