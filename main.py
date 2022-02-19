import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import cv2
import mediapipe as mp
import numpy as np

fontName = 'NanumGothicBold.ttf'

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


class SayHello(App):

    def build(self):
        self.window=GridLayout()
        self.window.cols = 1


        #image widget
        self.window.add_widget(Image(source="hi.jpg"))
        #Label widget
        self.greeting=Label(text="너의 이름은?",font_name=fontName)
        self.window.add_widget(self.greeting)
        # text input widget
        self.user=TextInput(multiline=False,font_name=fontName)
        self.window.add_widget(self.user)

        #button widget
        self.button=Button(text="open camera")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window
    def callback(self, instance):
        cap = cv2.VideoCapture(0)
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Mediapipe Feed', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

if __name__== "__main__":
    SayHello().run()
