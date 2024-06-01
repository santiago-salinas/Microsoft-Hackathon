import asyncio

from fastanpr import FastANPR
import cv2


async def main():
    fast_anpr = FastANPR()
    files = ["./test2.jpeg"]
    images = [cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2RGB) for file in files]
    number_plates = await fast_anpr.run(images)

# Print out results
    for file, plates in zip(files, number_plates):
        print(file)
        for plate in plates:
            print("Plate Attributes:")
            print("Detection bounding box:", plate.det_box)
            print("Detection confidence:", plate.det_conf)
            print("Recognition text:", plate.rec_text)
            print("Recognition polygon:", plate.rec_poly)
            print("Recognition confidence:", plate.rec_conf)
            print()
        print()


if __name__ == '__main__':
    asyncio.run(main())