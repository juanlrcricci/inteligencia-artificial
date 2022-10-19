import cv2

img = cv2.imread('images/persona0_grey/angry.png')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(grey)
rows, cols = grey.shape
print(grey.shape)

lista = []

for i in range(rows):
    lista.append(1)
    for j in range(cols):
        k = img[i, j][0]
        lista.append(k)