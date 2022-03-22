import sys
import exifread
from exif import Image

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  try:
    file = sys.argv[1]
    with open (file, 'rb') as img_file:
        img = Image(img_file)
    #Return Exif tags
    #exif_tags = exifread.process_file(file)
    #print(file.model)
    #file.close()
    print(f'Make: {img.get("make")}')
    print(f'Model: {img.get("model")}')
    print(f'Original Date/Time: {img.get("datetime_original")}')
    print(f'Latitude: {img.get("gps_latitude")}')
    print(f'Longitude: {img.get("gps_longitude")}')

  except IOError as e:
      print (e)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
