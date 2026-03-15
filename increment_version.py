import re

path = 'android/app/build.gradle'
with open(path, 'r') as f:
    content = f.read()

# versionCode +1
def bump_code(m):
    return 'versionCode ' + str(int(m.group(1)) + 1)
content = re.sub(r'versionCode\s+(\d+)', bump_code, content)

# versionName +0.01 (örn: "1.00" -> "1.01")
def bump_name(m):
    v = float(m.group(1))
    new_v = round(v + 0.01, 2)
    return 'versionName "' + format(new_v, '.2f') + '"'
content = re.sub(r'versionName\s+"([0-9.]+)"', bump_name, content)

with open(path, 'w') as f:
    f.write(content)

print("versionCode and versionName incremented")
