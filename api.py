import re
import pandas as pd

f = open("data/_ilo5_resourcedefns.md", "r")

def clean_data(s):
    s = s.replace('```','')
    s = re.sub("^\|", "", s, )
    s = re.sub("\|$", "", s, )
    s = re.sub("\|", ":", s, )
    return s


def get_lines():
    s = clean_data(line)
    while True:
        n = clean_data(next(f))
        if re.match("^ *$", n):
            return s.rstrip()
        s = s + n


resource = str()
uri = str()
description = str()

df = pd.DataFrame(columns=['Resource', 'Member', 'URI', 'ReadOnly', 'Type', 'Values', 'Description'])

for line in f:
    if line.startswith("## "):
        resource = line.split(".")
        resource = resource[len(resource)-1].strip()
        print(resource)
        uri = str()
        description = str()
        member = str()
        type = str()
        readonly = str()
        values = str()

    if re.match("^\|\`\`\`/redfish.*", line):
        uri = get_lines()

    if re.match("(^### .*|^\*\*\D)", line):
        mem = line
        line = next(f)
        while True:
            if re.match("^\*\*\D", line):
                mem = mem + line
                line = next(f)
            else:
                break

        member = re.sub("^### (.*)", r"\1", mem).rstrip()
        member = member.replace('**', '')

        if re.match("(Member of|^A reference to)", line):
            line = next(f)
            line = next(f)
            if re.match("^\|", line):
                spec = get_lines()
                description = re.search(".*Description *: *(.*)", spec)
                if description: description = description.group(1)
                type = re.search(".*Type *: *(.*)", spec)
                if type: type = type.group(1)
                readonly = re.search(".*Read Only *: *(.*)", spec)
                if readonly: readonly = readonly.group(1)

                df = df.append({'Resource': resource,
                                'URI': uri,
                                'Member': member,
                                'Description': description,
                                'Type': type,
                                'ReadOnly': readonly},
                                ignore_index=True)
                row = len(df)
            else:
                df = df.append({'Resource': resource,
                                'Member': member},
                                ignore_index=True)
                continue



    if re.match("^\|Value\|Description", line):
        line = next(f)
        line = next(f)
        values = get_lines()
        df.loc[row-1, 'Values'] = values

df.to_excel("data/api.xlsx", index=False)
f.close()
