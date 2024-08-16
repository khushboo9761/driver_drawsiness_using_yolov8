# Drowsiness Detection System

![image](https://github.com/user-attachments/assets/81ab2ce9-94ed-479b-bb76-d289c99800fc)
![image](https://github.com/user-attachments/assets/0615e219-f623-47ff-9448-946a9c273500)
![image](https://github.com/user-attachments/assets/b25705ed-d976-45a3-a080-fe1e12f220fd)

## Overview

The **Drowsiness Detection System** is a tool designed to monitor a person's alertness in real-time by analyzing facial features. By utilizing computer vision and machine learning techniques, this system can detect signs of drowsiness and alert the user before it becomes dangerous, particularly while driving.

## Features

- **Real-time Detection**: Monitors and detects drowsiness in real-time using a webcam or pre-recorded video.
- **Dual Model Approach**: Utilizes two YOLOv8 models—one for eye state detection (open/closed) and another for yawning detection.
- **Facial Landmarks**: Analyzes eye closure, head position, and yawning frequency using advanced facial recognition.
- **Customizable Alerts**: Alerts can be customized based on detection thresholds.
- **Data Capture**: Captures and logs data for further analysis or training.
- **Auto Labeling**: Automated bounding box generation using GroundingDINO for training datasets.
- **User Interface**: A user-friendly interface built with PyQt5 to visualize detection results.

### Key Files

- **`AutoLabelling.py`**: Script to automatically label data for training.
- **`CaptureData.py`**: Captures video data for drowsiness detection.
- **`DrowsinessDetector.py`**: Core detection logic, including facial landmarks and alert systems.
- **`LoadData.ipynb`**: Notebook to load and preprocess data.
- **`RedirectData.ipynb`**: Redirect and manage captured data.
- **`train.ipynb`**: Jupyter notebook for training the detection model.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/tyrerodr/Real_time_drowsy_driving_detection.git
    cd Real_time_drowsy_driving_detection
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the detection script:**
    ```bash
    python DrowsinessDetector.py
    ```

## Usage

- **Real-Time Detection**: Simply run the `DrowsinessDetector.py` script and ensure your webcam is connected.
- **Data Capture**: Use `CaptureData.py` to record and log video data for analysis or training purposes.
- **Training**: Use `train.ipynb` to train the model with custom datasets.

## How It Works

The system uses two models based on YOLOv8:

1. **Eye Detection Model**: This model detects whether the eyes are open or closed. It was trained using the following public datasets:
    - [Eyes Dataset](https://www.kaggle.com/datasets/charunisa/eyes-dataset/code)
    - [MRL Eye Dataset](https://www.kaggle.com/datasets/tauilabdelilah/mrl-eye-dataset)

   Approximately 53,000 images were used for training and 3,000 images for validation.

2. **Yawning Detection Model**: This model detects yawning by classifying images where the mouth is open (yawning) or closed. It was trained using the following public dataset:
    - [Yawning Dataset](https://www.kaggle.com/datasets/deepankarvarma/yawning-dataset-classification?select=yawn)

To prepare the images for YOLO training, the [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) library was used to generate bounding boxes, ensuring precise detection areas.

Once the models were trained, the prediction logic was implemented, setting confidence thresholds for each class (eyes closed/open, yawning/not yawning). The results are displayed through a custom interface created using PyQt5.

### Technologies Used

- **Python**: Core programming language.
- **YOLOv8**: Used for object detection.
- **OpenCV**: For computer vision tasks.
- **GroundingDINO**: For generating bounding boxes.
- **Keras/TensorFlow**: For model training and inference.
- **PyQt5**: For the graphical user interface.

## Future Improvements

- **Integration with Wearables**: Adding support for wearable devices to monitor heart rate and other vital signs.
- **Multi-Person Detection**: Expanding the system to detect drowsiness in multiple individuals simultaneously.
- **Mobile Application**: Developing a mobile app version for on-the-go monitoring.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you have any suggestions or improvements.

