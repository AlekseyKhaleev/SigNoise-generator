from PIL import Image, ImageDraw, ImageFilter

# Создаем новое изображение 16x16 с белым фоном
image = Image.new('1', (16, 16), "white")
draw = ImageDraw.Draw(image)

# Рисуем две диагонали. Помните, что система координат изображения начинается в верхнем левом углу.
draw.line((0, 0, 15, 15), fill="black")  # От верхнего левого угла до нижнего правого
draw.line((0, 15, 15, 0), fill="black")  # От нижнего левого угла до верхнего правого

# Применяем медианный фильтр
filtered_image = image.filter(ImageFilter.MedianFilter(size=3))

# Сохраняем исходное и отфильтрованное изображения
image.save("original.png")
filtered_image.save("filtered.png")