from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

pattern = r'(\+7|8)?[\s|(]?[\s(]?(\d{3})[\s|)]?[)\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})\s*[(]?(доб.)?\s*(\d{4})?'
re_pattern = r'+7(\2)\3-\4-\5 \6\7'

con_list = []
for i in contacts_list:
     all = i[0].split() + i[1].split() + i[2].split() + i[3:]
     con_list.append(all)

for i in con_list:
     try:
          match = re.findall(pattern, i[-2])
          result = ''.join(match[0])
          re_logick = re.sub(pattern, re_pattern, result)
          i[-2] = re_logick
     except:
          pass


contacts_list = [['test']]

w = []
for i in con_list:
     for i2 in contacts_list:
          w.append(i2[0])
     if i[0] not in w:
          contacts_list.append(i)
          w.clear()
     else:
          for i3 in contacts_list:
               if i3[0] in i:
                    count = 0
                    ww = []
                    while count <= 8:
                         try:
                              if len(i3[count]) > 1 or len(i[count]) < 1:
                                   if i3[count] not in ww:
                                        ww.append(i3[count])
                         except:
                              pass
                         try:
                              if len(i3[count]) < 1 or len(i[count]) > 1:
                                   if i[count] not in ww:
                                        ww.append(i[count])
                         except:
                              pass
                         count += 1
          for i4 in contacts_list:
               if i[0] == i4[0]:
                    contacts_list.remove(i4)
                    contacts_list.append(ww)
contacts_list.pop(0)
contacts_list.pop(0)
pprint(contacts_list)


with open("phonebook.csv", "w") as f:

     datawriter = csv.writer(f, delimiter=',')

     datawriter.writerows(contacts_list)
