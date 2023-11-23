import cv2
import numpy as np
import os
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename as opfile


def calculate_batch_intensity(image, batch_size):

    cv2.namedWindow("image")
    cv2.imshow("image", image)
    cv2.waitKey(1)

    def click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            image_copy = image.copy()
            point_coords = f"({x}, {y})"
            cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1)
            cv2.putText(
                image_copy,
                point_coords,
                (x + 5, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3,
            )
            cv2.imshow("image", image_copy)

            print("Координаты точки:", point_coords)

            left = x - batch_size // 2
            right = x + batch_size // 2
            top = y - batch_size // 2
            bottom = y + batch_size // 2

            batch = image[top:bottom, left:right]

            blue_intensity = np.mean(batch[:, :, 0])
            green_intensity = np.mean(batch[:, :, 1])
            red_intensity = np.mean(batch[:, :, 2])

            print("Средняя интенсивность по каналу синего:", blue_intensity)
            print("Средняя интенсивность по каналу зеленого:", green_intensity)
            print("Средняя интенсивность по каналу красного:", red_intensity)
            print()

    cv2.setMouseCallback("image", click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def openfile():
    Tk().withdraw()
    file = opfile(title="Выберите изображение")
    image = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        print("Ошибка загрузки изображения!!!")
        os.system("pause")
        sys.exit(0)
    if len(image.shape) != 3 or image.shape[2] != 3:
        print("Некорректное изображение!")
        os.system("pause")
        sys.exit(0)
    return image


def batch_input():
    batch_size = int(input("Введите размер батча (от 30 до 80 пикселей): "))
    if batch_size < 30 or batch_size > 80:
        print("Недопустимый размер батча!")
        return batch_input()
    return batch_size


if __name__ == "__main__":
    image = openfile()
    batch_size = batch_input()
    calculate_batch_intensity(image, batch_size)
    os.system("pause")
