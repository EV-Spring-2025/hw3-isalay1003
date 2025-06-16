import cv2
import numpy as np
import os

def psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def compute_video_psnr(video_path1, video_path2):
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    psnr_values = []
    frame_count = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break

        if frame1.shape != frame2.shape:
            print("Frame size mismatch!")
            break

        psnr_val = psnr(frame1, frame2)
        psnr_values.append(psnr_val)
        frame_count += 1
    cap1.release()
    cap2.release()

    if psnr_values:
        average_psnr = np.mean(psnr_values)
        print(f"Average PSNR over {frame_count} frames: {average_psnr:.2f} dB")
        return average_psnr
    else:
        print("No frames compared.")
        return None

if __name__ == "__main__":
    material = "jelly"
    param = "soft=0"
    print(f"Evaluating PSNR for {material} with {param}")
    compute_video_psnr(f"video/{material}_base.mp4", f"video/{material}_{param}.mp4")
