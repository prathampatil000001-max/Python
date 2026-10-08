# Q11. File Type Detector
# Take a file extension as input:

# pdf
# jpg
# png
# mp3
# mp4
# Display the type of file.

# Example:

# pdf → Document
# jpg → Image
# png → Image
# mp3 → Audio
# mp4 → Video

choice=(input("Enter a extention pdf ,jpj, png , mp3,mp4:"))
match choice:
    case "pdf":
        print("Document")
    case "jpg":
        print("Image")
    case "png":
        print("Image")
    case "mp3":
        print("Audio")
    case "mp4":
        print("Video")
    case _:
        print("Invalid case")