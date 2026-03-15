import re

path = 'android/app/build.gradle'
with open(path, 'r') as f:
    content = f.read()

# versionCode -> min 4
def bump_code(m):
    current = int(m.group(1))
    new = max(current + 1, 4)
    return 'versionCode ' + str(new)
content = re.sub(r'versionCode\s+(\d+)', bump_code, content)

# versionName -> min 1.03
def bump_name(m):
    v = float(m.group(1))
    new_v = max(round(v + 0.01, 2), 1.03)
    return 'versionName "' + format(new_v, '.2f') + '"'
content = re.sub(r'versionName\s+"([0-9.]+)"', bump_name, content)

with open(path, 'w') as f:
    f.write(content)

print("versionCode and versionName incremented")
