from controller import Robot
import numpy as np
import cv2 as cv

class Controller(Robot):

    def __init__(self):
        super().__init__()
        
        self.timeStep = int(self.getBasicTimeStep())

        self.camera = self.getDevice("Webcam for Robotino 3")
        self.camera.enable(self.timeStep)
        self.camera_width = self.camera.getWidth()
        self.camera_height = self.camera.getHeight()
    
    def get_image(self):
        image_data = self.camera.getImage()

        if not image_data:
            return None
        
        image_np = np.frombuffer(image_data, dtype = np.uint8).reshape((self.camera_height, self.camera_width, 4))

        return image_np

    def save_image(self, filename = "../../foto_teste.png"):
        image_np = self.get_image()

        if image_np is not None:
            cv.imwrite(filename, image_np)
            print(f"Imagem salva!")
    
    def run(self):

        while self.step(self.timeStep) != -1:

            self.save_image()
            break

if __name__ == "__main__":
    controller = Controller()
    controller.run()

    