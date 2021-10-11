from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import FormularioRegistro
import cv2
import os
import imutils
import numpy as np
# Create your views here.

def crearUsuario(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect("caras")
    else:
        form = FormularioRegistro()
    return render(request, 'usuario/registrar.html', {'form': form})




def RegistroCaras(request):
    #model = User
    nombre = User.objects.all().last()
    #contexto = {'mascotas':mascota}
    #aaa = input(" Escriba su nombre de usuario: ")
    personName =  nombre
    
    dataPath = 'D:/PythonProjects/refugio/refugio/media/perfil'#Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + personName
    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
    
        faces = faceClassif.detectMultiScale(gray,1.3,5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)
    
        k =  cv2.waitKey(1)
        if k == 27 or count >= 50:
            break
    cap.release()
    cv2.destroyAllWindows()

    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')
        for fileName in os.listdir(personPath):
            #print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName,0))
            image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
        label = label + 1

    #joseprint('Labels= ',labels)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))

    face_recognizer.write('modeloEigenFace.xml')
    print("Modelo almacenado...")
    return(request,)

       

    #comparacion(imagen1,imagen2)

    

    #return render(request, 'usuario/caras.html')'''