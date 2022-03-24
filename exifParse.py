import sys
import exifread
from exif import Image


def format_dms_coordinates(coordinates, coordinates_ref):
    if coordinates_ref == "S" or coordinates_ref == "W":
        return f"-{coordinates[0]} degrees, -{coordinates[1]} minutes, -{coordinates[2]} seconds"
    return f"{coordinates[0]} degrees, {coordinates[1]} minutes, {coordinates[2]} seconds"


# def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
#      decimal_degrees = coordinates[0] + \
#                        coordinates[1] / 60 + \
#                        coordinates[2] / 3600
#
#      if coordinates_ref == "S" or coordinates_ref == "W":
#          decimal_degrees = -decimal_degrees
#
#      return decimal_degrees

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
    print("Source File: " + file)
    print(f'Make: {img.get("make")}')
    print(f'Model: {img.get("model")}')
    print(f'Original Date/Time: {img.get("datetime_original")}')
    # print(f'Latitude: {img.get("gps_latitude")}')
    # print(f'Longitude: {img.get("gps_longitude")}')

    print(f"Latitude: {format_dms_coordinates(img.gps_latitude, img.gps_latitude_ref)} ")
    print(f"Longitude: {format_dms_coordinates(img.gps_longitude, img.gps_longitude_ref)} ")
    # print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(img.gps_latitude, img.gps_latitude_ref)}")
    # print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(img.gps_longitude, img.gps_longitude_ref)}\n")

  except (IndexError) as e:
      print ("Error! - No Image File Specified!")
  except (FileNotFoundError, IOError) as e:
      print ("Error! - File Not Found!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
