# Password

การวัดระดับความแข็งแรงของ Password สามารถทำได้หลายวิธี วิธีที่ได้รับความนิยมวิธีหนึ่งคือการหาค่า Entropy ของ Password
โดยสูตรการคำนวณหาค่า Entropy เป็นดังนี้





ค่า E คือค่า Entropy ของ Password มีหน่วยเป็นบิต
R คือค่าขนาดของ Pool
L คือค่าขนาดความยาวของ Password

![](https://ejudge.it.kmitl.ac.th/uploads/1691234840_Screenshot%202566-08-05%20at%2018.27.04.png)

ยกตัวอย่างเช่น

ตัวอย่างที่ 1 Password คือ incorrect
จะมีค่า R = 26 เนื่องจาก Password incorrect มีตัวพิมพ์เล็กภาษาอังกฤษ (a-z) เพียงอย่างเดียว ซึ่งมีความเป็นไปได้ทั้งหมด 26 ตัว
ค่า L มีค่า 9 เนื่องจากมีความยาวของ Password 9 ตัว

ตัวอย่างที่ 2 Password คือ Incorrect
จะมีค่า R = 52 เนื่องจาก Password Incorrect มีตัวพิมพ์เล็ก (a-z) และตัวพิมพ์ใหญ่ภาษาอังกฤษ (A-Z) ซึ่งมีความเป็นไปได้รวมกันทั้งหมด 52 ตัว (26 + 26)
ค่า L มีค่า 9 เนื่องจากมีความยาวของ Password 9 ตัว

ตัวอย่างที่ 3 Password คือ IncoRRect77
จะมีค่า R = 62 เนื่องจาก Password IncoRRect77 มีตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ภาษาอังกฤษและมีตัวเลขซึ่งมีค่าความเป็นไปได้อีก 10 ค่า (0-9) รวมทั้งหมด 62 ตัว
ค่า L มีค่า 11 เนื่องจากมีความยาวของ Password 11 ตัว

ตัวอย่างที่ 4 Password คือ IncoRRect77=@+
จะมีค่า R = 94 เนื่องจาก Password IncoRRect77=@+มีตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ภาษาอังกฤษและมีตัวเลขซึ่งมีค่าความเป็นไปได้อีก 10 ค่า (0-9) และอักขระพิเศษ (Printable) อีก 32 ตัว เช่น =+#$%^&*@_! และอื่นๆอีกหลายตัว (ดูตารางด้านล่างประกอบ) รวมทั้งหมด ​94 ตัว
ค่า L มีค่า 14 เนื่องจากมีความยาวของ Password 14 ตัว

ค่า Entropy ที่คำนวณได้ให้ปัดเศษทิ้งเสมอ เช่นหากคำนวณได้เป็น 42.9 ให้ปัดเศษทิ้ง และจะมีค่าเป็น 42 บิต
ระดับความแข็งแรงของ Password จะขึ้นกับค่า Entropy และเป็นไปดังรูปด้านล่าง



จงเขียนโปรแกรมรับ Password และหาค่า Entropy และระดับความแข็งแรงของ Password
รูปด้านล่างเป็นตารางอักขระพิเศษ 32 ตัว บน Keyboard


![](https://ejudge.it.kmitl.ac.th/uploads/1691235586_Screenshot%202566-08-05%20at%2018.38.57.png)

![](https://ejudge.it.kmitl.ac.th/uploads/1691735955_Screenshot%202566-08-11%20at%2013.36.07.png)

### Input Specification

เป็นข้อความ String 1 บรรทัดที่เป็นตัวอักษรภาษาอังกฤษตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ หรือมีตัวเลข หรือมีอักขระพิเศษ ที่ Printable (ไม่มี Whitespace)

### Output Specification

2 บรรทัด
บรรทัดที่ 1 เป็นค่า Entropy มีเป็นจำนวนเต็ม หน่วยเป็นบิต
บรรทัดที่ 2 ระดับความแข็งแรงของ Password



### Test Case 1

**Input**

```
incorrect
```
**Expected Output**

```
42
Reasonable
```


### Test Case 2

**Input**

```
incorrect
```
**Expected Output**

```
42
Reasonable
```


### Test Case 3

**Input**

```
IncoRRect77
```
**Expected Output**

```
65
Strong
```


### Test Case 4

**Input**

```
###!PasswordInwZa007!###
```
**Expected Output**

```
157
Very Strong
```
