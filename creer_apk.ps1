$RenpySdkPath = "C:\Users\Pierre\Downloads\Nouveau dossier (3)\renpy-8.5.2-sdk"
$GameName = "laurald-Renpy-Escape-game"

Write-Host "Preparation de l'environnement Java..."
$env:JAVA_HOME = "C:\Program Files\Java\jdk-21.0.11"
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

Write-Host "Deplacement vers le dossier SDK..."
Set-Location $RenpySdkPath

Write-Host "Lancement de la compilation Android (cela peut prendre quelques minutes)..."
.\lib\py3-windows-x86_64\python.exe .\renpy.py launcher android_build $GameName

Write-Host "`nDernier APK genere :"
Get-ChildItem -Path ".\rapt\bin" -Filter "*.apk" | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Format-List Name, Length, LastWriteTime

Write-Host "Termine !"
Read-Host -Prompt "Appuyez sur Entree pour quitter..."
