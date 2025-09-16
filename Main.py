import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, mode=False, max_hands=1, detection_conf=0.7, track_conf=0.7):
        self.hands = mp_hands.Hands(
            static_image_mode=mode,
            max_num_hands=max_hands,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=track_conf
        )

    def find_hands(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

        if draw and self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        return frame

    def find_position(self, frame):
        """
        return (x,y) ของปลายนิ้วชี้ (index finger tip)
        """
        h, w, _ = frame.shape
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                lm = hand.landmark[8]  # index finger tip
                return int(lm.x * w), int(lm.y * h)
        return None