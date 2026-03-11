import re, os

rpath = 'android/build.gradle'
with open(rpath, 'r') as f:
    content = f.read()

if 'resolutionStrategy' not in content:
    fix = (
        "\nallprojects {\n"
        "    configurations.all {\n"
        "        resolutionStrategy {\n"
        "            force 'org.jetbrains.kotlin:kotlin-stdlib:1.8.10'\n"
        "            force 'org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.8.10'\n"
        "            force 'org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.8.10'\n"
        "        }\n"
        "    }\n"
        "}\n"
    )
    content += fix
    with open(rpath, 'w') as f:
        f.write(content)
    print("Kotlin resolutionStrategy added")
else:
    print("Already has resolutionStrategy")
