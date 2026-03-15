import re

path = 'android/app/build.gradle'
with open(path, 'r') as f:
    content = f.read()

# versionCode -> 3
def bump_code(m):
    current = int(m.group(1))
    new = max(current + 1, 3)
    return 'versionCode ' + str(new)
content = re.sub(r'versionCode\s+(\d+)', bump_code, content)

# versionName -> "1.02"
def bump_name(m):
    v = float(m.group(1))
    new_v = max(round(v + 0.01, 2), 1.02)
    return 'versionName "' + format(new_v, '.2f') + '"'
content = re.sub(r'versionName\s+"([0-9.]+)"', bump_name, content)

with open(path, 'w') as f:
    f.write(content)

print("versionCode and versionName incremented")
