@echo off
echo Preparation de l'environnement...
set JAVA_HOME=C:\Program Files\Java\jdk-21.0.11
set PATH=%JAVA_HOME%\bin;%PATH%

echo.
echo Deplacement vers le dossier du SDK Ren'Py...
cd ..

echo.
echo Lancement de la compilation de l'APK (cela peut prendre quelques minutes)...
.\lib\py3-windows-x86_64\python.exe .\renpy.py launcher android_build laurald-Renpy-Escape-game

echo.
echo === Dernier APK genere ===
dir .\rapt\bin\*.apk /O:-D /T:W | findstr ".apk"

echo.
echo Compilation terminee !
pause
