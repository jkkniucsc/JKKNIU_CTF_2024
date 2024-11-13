> [!NOTE]
> This script is designed to decode all QR codes in a given set of images or video frames. It’s functional but poorly written and can be optimized for better performance, readability, and efficiency:)
```python
import cv2    #pip install cv
from pyzbar.pyzbar import decode

video_path = 'dump.mp4'
cap = cv2.VideoCapture(video_path)
unique_data = set()

frame_skip = 5
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_skip == 0:
        qr_codes = decode(frame)
        for qr_code in qr_codes:
            data = qr_code.data.decode("utf-8")
            if data not in unique_data:  # Only add if data is new
                unique_data.add(data)
                print(f"Frame {frame_count}: {data}")
    
    frame_count += 1

cap.release()

with open("result.txt", "w") as f:
    for data in unique_data:
        f.write(f"{data}\n")

print("Done and result saved to 'result.txt'.")
```

> Filter the output using the following command for better result: 
```sh
sed 's/^Frame [0-9]*: //' result.txt | grep -vE 'https|EMAIL|TEL|N:|END' | sort -u
```
The output should be like below: <br>
`First part: JKKNIUCTF{`  <br>
`M3JkIHBhcnQ6IF81M2NyMzdfTTM1NTQ5MzJ9`   <br>
`Mm5kIHBhcnQ6IFFSX0MwRDM1X0M0bl81NzByMw==` <br>

Decode the base64 hashes to get the full flag
```sh
echo 'Mm5kIHBhcnQ6IFFSX0MwRDM1X0M0bl81NzByMw==' | base64 -d                                    
2nd part: QR_C0D35_C4n_570r3
```
```sh
'M3JkIHBhcnQ6IF81M2NyMzdfTTM1NTQ5MzJ9' | base64 -d                                        
3rd part: _53cr37_M3554932}
``` 
---
### **Flag**: `JKKNIUCTF{QR_C0D35_C4n_570r3_53cr37_M3554932}`
