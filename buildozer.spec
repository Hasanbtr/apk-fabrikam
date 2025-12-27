[app]
title = Sistem Servisi
package.name = mysystemapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Plyer kütüphanesi kamera/sistem erişimi için şarttır
requirements = python3,kivy,plyer

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

# İzinler (Kamera ve İnternet)
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
