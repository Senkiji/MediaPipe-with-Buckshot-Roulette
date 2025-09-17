import cv2
from modules.gesture_recognition import HandDetector
from modules.ui_overlay import draw_layout, detect_region
from modules.action_mapping import perform_action

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        mirrored_frame = cv2.flip(frame, 1)
        frame = detector.find_hands(mirrored_frame)
        draw_layout(mirrored_frame)

        pos = detector.find_position(frame)
        if pos:
            x, y = pos
            region = detect_region(x, y)
            if region:
                cv2.putText(mirrored_frame, f"In: {region}", (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                perform_action(region)
        
        cv2.imshow("Buckshot Roulette Control", mirrored_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()