import cv2
from modules.hand_tracking import HandTracker
from modules.gesture_recognition import GestureRecognizer
from modules.mouse_actions import MouseController
from overlay.overlay_manager import OverlayManager
from config.mapping import ACTION_MAPPING

def main():
    cap = cv2.VideoCapture(0)
    hand_tracker = HandTracker()
    gesture_recognizer = GestureRecognizer()
    mouse_controller = MouseController()
    overlay = OverlayManager()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # ตรวจจับมือ
        hand_landmarks = hand_tracker.get_hand_landmarks(frame)

        if hand_landmarks:
            # หาปลายนิ้ว index finger
            fingertip = hand_tracker.get_index_fingertip(hand_landmarks)

            # ตรวจ gesture ว่า hover อยู่ใน region ไหน
            hovered_region = gesture_recognizer.detect_hover(fingertip)

            if hovered_region:
                action = ACTION_MAPPING.get(hovered_region)
                if action:
                    mouse_controller.execute_action(action)

            # วาด overlay + highlight region
            frame = overlay.draw(frame, hovered_region, fingertip)

        cv2.imshow("Buckshot Roulette Controller", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
