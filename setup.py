from setuptools import setup

APP = ['run.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['cv2', 'insightface', 'customtkinter', 'PIL'],
    'plist': {
        'CFBundleName': 'DeepLiveCam',
        'CFBundleDisplayName': 'Deep Live Cam',
        'CFBundleIdentifier': 'com.fespinoza.deeplivecam',
        'CFBundleVersion': '1.0.0',
        'NSCameraUsageDescription': 'Esta aplicación requiere acceso a la cámara para realizar sustitución de rostros en tiempo real.',
    },
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)