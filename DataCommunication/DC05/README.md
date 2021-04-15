# CNU-2week_practice

## commit할 경우 반드시 comment에 자신의 학번을 넣어주시기 바랍니다!!

## 충남대학교 데이터통신 02분반 5주차 과제 Data Over Sound - 소리 재생
- soundEncode.py파일을 기반으로 과제 진행할 것!
- autograding이 이루어지기 때문에 push할 경우 파일 이름은 변경하지 말고 진행!
  - 파일 이름 변경시 채점이 이루어지지 않음.

### input/output example
```
# python3 test_input.py --> input: hello // output: hello world!
# below test_input.py code
str_input = input()
print(f'{str_input} world!')
```
- input()으로 입력을 받을 수 있도록 코드 작성

### 해당 과제에서의 input/output example
```
>> input
hi
>> output
3072
2560
3328
2048
3840
4096
1024
2816
1024
4864
3584
```
- handshake start/end frequency는 출력하지 않음

### 주의 사항!
- Github Classroom 자동 채점을 사용하기 위해 soundEncode.py에서 수정해야할 부분 설명
  - 2번째 줄 import pyaudio 제거
  - 15번째 줄 함수를 14번째 줄 함수 형태로 변경 (매개변수 1개로 감소)
  - 26번째 줄부터 30번째 줄까지 제거
- 해당 코드들은 모두 소리를 내기 위한 코드로 Github Classroom을 통한 자동 채점에서는 필요없음
  - 입력과 출력 기능만을 사용할 것
