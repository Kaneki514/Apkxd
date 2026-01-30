[app]

# Título de la aplicación
title = CruzRaya

# Nombre del paquete (sin espacios, minúsculas)
package.name = cruzraya

# Dominio del paquete (para Android/iOS)
package.domain = org.cruzraya

# Directorio del código fuente
source.dir = .

# Extensiones de archivos a incluir
source.include_exts = py,png,jpg,jpeg,json,ttf,otf,wav,mp3,ogg

# Archivos/directorios a excluir
source.exclude_dirs = tests, bin, venv, docs, .buildozer, .git, __pycache__
source.exclude_patterns = *.pyc, *.pyo, *.pyd, *.so, *.a, *.log, .gitignore, README.md, LICENSE, build/, dist/

# Versión de la aplicación
version = 1.0

# Requirements (incluye kivy aunque no lo uses, ayuda con compatibilidad)
requirements = python3,kivy==2.1.0,pygame==2.1.2,android

# Permisos de Android (ajusta según necesites)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, VIBRATE

# Versiones de API de Android
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.ndk_api = 21

# Arquitecturas
android.archs = arm64-v8a, armeabi-v7a

# Bootstrap para Pygame (IMPORTANTE)
android.bootstrap = sdl2  # Pygame funciona mejor con SDL2 bootstrap

# Punto de entrada para Android
android.entrypoint = org.kivy.android.PythonActivity

# Actividad principal
android.activity_class_name = org.kivy.android.PythonActivity

# No usar almacenamiento privado (mejor compatibilidad con Pygame)
android.private_storage = False

# Permite backup
android.allow_backup = True

# Pantalla completa
fullscreen = 1

# Orientación
orientation = portrait

# Log level para debug
android.logcat_filters = *:S python:D

# Características
android.features = android.hardware.touchscreen

# Icono y splash (descomenta y crea estos archivos si los tienes)
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# Color del splash screen
android.presplash_color = #000000

# Servicios (si necesitas servicios en segundo plano)
# services = CruzRayaService:main.py

# Modo de lanzamiento
android.manifest.launch_mode = singleTop

# Mantener pantalla encendida
android.wakelock = False

# Dependencias de Gradle (necesarias para compatibilidad)
android.gradle_dependencies = 'com.google.android.material:material:1.6.0'

# Habilitar AndroidX
android.enable_androidx = True

# Opciones de compilación
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# Repositorios de Gradle
android.add_gradle_repositories = "maven { url 'https://jitpack.io' }"

# Opciones de empaquetado
android.add_packaging_options = "exclude 'META-INF/DEPENDENCIES'", "exclude 'META-INF/NOTICE'", "exclude 'META-INF/LICENSE'", "exclude 'META-INF/LICENSE.txt'", "exclude 'META-INF/NOTICE.txt'"

# Bibliotecas nativas (si tienes .so files)
# android.add_libs_armeabi_v7a = libs/armeabi-v7a/*.so
# android.add_libs_arm64_v8a = libs/arm64-v8a/*.so

# Recursos adicionales
# android.add_resources = data/icon.png:drawable/icon

# Metadatos de la aplicación
android.meta_data = android.app.lib_name=cruzraya

# Ajustes para Pygame específicamente
android.extra_manifest_xml = <?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- Permisos adicionales si son necesarios -->
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    
    <!-- Configuración de hardware -->
    <uses-feature android:name="android.hardware.touchscreen" android:required="true" />
    <uses-feature android:glEsVersion="0x00020000" android:required="true" />
    
    <!-- Configuración de compatibilidad -->
    <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="31" />
    
    <!-- Soporte para pantallas grandes -->
    <supports-screens
        android:smallScreens="true"
        android:normalScreens="true"
        android:largeScreens="true"
        android:xlargeScreens="true"
        android:anyDensity="true" />
</manifest>

[buildozer]

# Nivel de log (0=error, 1=info, 2=debug)
log_level = 2

# Advertencia al ejecutar como root
warn_on_root = 1

# Directorios de build
build_dir = ./.buildozer
bin_dir = ./bin

# Configuración específica para desarrollo
# --------------------------------------------------

# Para desarrollo rápido, descomenta estas líneas:
# android.accept_sdk_license = True
# android.skip_update = False

# Si tienes SDK y NDK instalados localmente, especifica las rutas:
# android.sdk_path = /path/to/android/sdk
# android.ndk_path = /path/to/android/ndk

# Configuración de python-for-android
p4a.branch = master
p4a.url = https://github.com/kivy/python-for-android.git

# Si necesitas recetas personalizadas para pygame
# p4a.local_recipes = ./recipes

# Hooks personalizados (si los necesitas)
# p4a.hook = ./hooks

# --------------------------------------------------
# PERFILES ESPECIALES (descomenta según necesites)
# --------------------------------------------------

# [app:source.exclude_patterns@debug]
# *.pyc
# *.pyo

# [app@release]
# android.release_artifact = apk
# android.allow_backup = false

# [app@demo]
# title = CruzRaya (Demo)
# android.permissions = INTERNET

# --------------------------------------------------
# CONFIGURACIÓN PARA iOS (si eventualmente necesitas)
# --------------------------------------------------

# ios.kivy_ios_url = https://github.com/kivy/kivy-ios
# ios.kivy_ios_branch = master
# ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
# ios.ios_deploy_branch = 1.10.0
# ios.codesign.allowed = false
