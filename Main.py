import cv2
from src.gesture_recognition import HandDetector
from src.ui_overlay import draw_layout, detect_region
from src.action_mapping import perform_action

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detector.find_hands(frame)
        draw_layout(frame)

        pos = detector.find_position(frame)
        if pos:
            x, y = pos
            region = detect_region(x, y)
            if region:
                cv2.putText(frame, f"In: {region}", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                perform_action(region)

        cv2.imshow("Buckshot Roulette Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
