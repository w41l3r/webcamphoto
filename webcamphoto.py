import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

ret, frame = cap.read()

if not ret:
    print("Erro ao capturar o frame.")
    exit()

cv2.imwrite("foto.jpg", frame)

print("Foto tirada com sucesso!")

cap.release()
