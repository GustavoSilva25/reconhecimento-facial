import face_recognition
import cv2
import os

# Carregar todas as imagens da pasta 'known_faces'
known_face_encodings = []
known_face_names = []

path = 'known_faces'
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image = face_recognition.load_image_file(f"{path}/{filename}")
        encoding = face_recognition.face_encodings(image)
        if encoding:  # garante que há rosto
            known_face_encodings.append(encoding[0])
            known_face_names.append(os.path.splitext(filename)[0])  # nome do arquivo = nome da pessoa

# Inicializar a câmera
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # mais rápido
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detectar rostos e calcular encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        # Redimensionar coordenadas para o frame original
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow('Reconhecimento Facial', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
