import re, os

vpath = 'android/variables.gradle'
if os.path.exists(vpath):
    with open(vpath, 'r') as f:
        content = f.read()
    content = re.sub(r'targetSdkVersion\s*=\s*\d+', 'targetSdkVersion = 35', content)
    content = re.sub(r'compileSdkVersion\s*=\s*\d+', 'compileSdkVersion = 35', content)
    with open(vpath, 'w') as f:
        f.write(content)
    print("variables.gradle patched to 35")

rpath = 'android/build.gradle'
if os.path.exists(rpath):
    with open(rpath, 'r') as f:
        content = f.read()
    content = re.sub(r"com\.android\.tools\.build:gradle:[0-9.]+", "com.android.tools.build:gradle:8.3.0", content)
    with open(rpath, 'w') as f:
        f.write(content)
    print("root build.gradle AGP patched")

wpath = 'android/gradle/wrapper/gradle-wrapper.properties'
if os.path.exists(wpath):
    with open(wpath, 'r') as f:
        content = f.read()
    content = re.sub(r'gradle-[0-9.]+-all\.zip', 'gradle-8.4-all.zip', content)
    content = re.sub(r'gradle-[0-9.]+-bin\.zip', 'gradle-8.4-bin.zip', content)
    with open(wpath, 'w') as f:
        f.write(content)
    print("gradle-wrapper patched to 8.4")
