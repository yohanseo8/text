with open("test.txt","r",encoding="utf-8")as file:
	lines=file.readlines()

print(lines)

for line in lines: #리스트 반복문
	print(line.strip()) #공백 삭제

with open("test.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")


while True:
	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

	if memo.lower()=="q":
		break
	
	with open("memo.txt","a",encoding="utf-8")as file:
		file.write(memo+"\n")
	
	print("메모 저장이 완료되었습니다.")