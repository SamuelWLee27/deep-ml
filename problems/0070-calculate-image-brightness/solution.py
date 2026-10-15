
def calculate_brightness(img):
	
	if not img:
		return -1

	length = len(img[0])

	brightness_sum = 0
	pixel_count = 0

	for row in img:
		if isinstance(row, int):
			return -1
			
		if length != len(row):
			return  -1
		
		for pixel in row:
			if pixel < 0 or pixel > 255:
				return -1
			pixel_count += 1
			brightness_sum += pixel

	return round(brightness_sum/pixel_count, 2)
	
