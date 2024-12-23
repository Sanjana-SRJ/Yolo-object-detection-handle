import cv2
import base64
import requests

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    img_bytes = buffer.tobytes()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    
    response = requests.post('http://localhost:8080/prediction', json={"img": img_base64})
    print("response text", response.text)
   

    if response.text:
        print("response json", response.json())
    else:
        print("Empty response received.")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()