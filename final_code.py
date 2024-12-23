# # source from https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993

# from ultralytics import YOLO
# import cv2
# import math 
# # start webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# # model
# model = YOLO("yolov8n.pt")

# # object classes
# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"
#               ]

# detections = []

# def object_detection(img):
#     detections = []
#     results = model(img, stream=True)

#     # coordinates
#     for r in results:
#         boxes = r.boxes

#         for box in boxes:
#             # bounding box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

#             # put box in cam
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

#             # confidence
#             confidence = math.ceil((box.conf[0]*100))/100
#             print("Confidence --->",confidence)

#             # class name
#             cls = int(box.cls[0])
#             class_name = classNames[cls]
#             print("Class name -->", classNames[cls])
#             detections.append({
#                 "class_name": class_name,
#                 "confidence": confidence,
#                 "bounding_box": {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
#             })

#             # object details
#             org = [x1, y1]
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2

#             cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
#     if img is not None:
#         cv2.imshow('Webcam', img)
#     if cv2.waitKey(1) == ord('q'):
#         return detections  # or you can return img, detections if needed

# cap.release()
# cv2.destroyAllWindows()