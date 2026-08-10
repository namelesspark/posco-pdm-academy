# 현재 경로에 있는 해당 파일이란걸 더 강조하는

# 만약 C:\Users\Nedpark\바탕화면\sample

import os

current_working_directory = os.getcwd()
print(current_working_directory)


file_list = os.listdir("Ipynb")
for file_name in file_list:
    print(file_name)

# =======================================
# 안전하게 파일 존재 확인
path = os.path.join("Python", "08_press.csv")
if os.path.exists(path):
    print("파일 있음", path)
# 데이터 폴더 안의 csv 파일을 찾고 싶을 때,