
from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolo11n.pt")

# Detect objects in shelf image
results = model("images/shelf2.jpg", save=True, conf=0.15)

# Display detected objects and count
for result in results:
    boxes = result.boxes
    count = len(boxes)

    print("\n--- RetailVision AI Detection Report ---")
    print(f"Total detected objects: {count}")

    if count == 0:
        print("No supported objects detected.")
        print("A custom-trained retail model may be needed.")
    else:
        for i, box in enumerate(boxes, start=1):
            class_id = int(box.cls[0])
            name = model.names[class_id]
            confidence = float(box.conf[0]) * 100

            print(
                f"{i}. {name} - Confidence: {confidence:.1f}%"
            )

print("\nDetection complete!")
print("Annotated image saved in the runs/detect folder.")