from ultralytics import YOLO
import cv2



def main(args=None)->None:
    model = YOLO("best.pt")

    cap = cv2.VideoCapture(r"https://www.youtube.com/watch?v=KlCzROTAos4&pp=ygUDQ09E")  

    while True:
        key = cv2.waitKey(1)
        ret, frame = cap.read()

        results = model(frame, conf=0.5, iou=0.5)

        annotated_frame = results[0].plot()

        cv2.imshow("Weapon Detection", annotated_frame)

        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()