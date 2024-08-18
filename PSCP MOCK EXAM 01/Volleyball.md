# Volleyball




![](https://ejudge.it.kmitl.ac.th/uploads/1662790258_volleyball.jpeg)

กติกา Volleyball จะเล่นกัน 5 set ทีมใดชนะได้ 3 set ก่อน จะเป็นผู้ชนะ โดย set ที่ 1 ถึง 4 จะแข่งกันโดยหากทีมใดได้ 25 คะแนนก่อน จะเป็นผู้ชนะใน set นั้น แต่ Set ที่ 5 ทีมใดได้ 15 คะแนนก่อนจะเป็นผู้ชนะ


อย่างไรก็ตามการชนะกันแต่ละ Set ยังมีข้อกำหนดว่าจะต้องชนะกันอย่างน้อย 2 คะแนน ซึ่งหมายความว่าใน set ที่ 1 ถึง 4 หากทั้ง 2 ทีมได้คะแนน 24 คะแนน เท่ากัน จะต้องแข่งกันต่อจนกว่าจะมีคะแนนต่างกัน 2 คะแนน กติกานี้เราเรียกว่า การดิว ดังนั้นหากมีการดิว คะแนนในการชนะใน set ที่ 1 ถึง 4 จะมีได้หลายแบบ เช่น 26 ต่อ 24 คะแนน หรือ 30 ต่อ 28 คะแนน เป็นต้น


ใน set ที่ 5 เราจะดิวกันที่ 14 คะแนน ดังนั้นถ้ามีการดิวกันใน set ที่ 5 การชนะใน set ที่ 5 จะมีคะแนนได้หลายแบบเช่น 16 ต่อ 14 คะแนน หรือ 20 ต่อ 18 คะแนน เป็นต้น


หากมีการบันทึกคะแนนตั้งแต่เริ่มแข่งในรูปแบบของ String ที่มีตัวอักษร 2 แบบคือ A กับ B โดยบันทึก A หาก A เป็นผู้ชนะในคะแนนนั้น และบันทึก B หาก B เป็นผู้ชนะในคะแนนนั้น เช่น



ตัวอย่างที่ 1: "AABAABA" จะหมายความว่าตอนนี้ A กับ B กำลังแข่งกันใน set ที่ 1 โดย A มีคะแนนนำ B อยู่ 5 ต่อ 2 คะแนน และการแข่งขันยังไม่จบ

ตัวอย่างที่ 2: "AABABABAABBBBAAABBABBBBBAAAABBBBBABABAABBBBBBBBBBABBA" จะหมายความว่า B ชนะใน set ที่ 1 ด้วยคะแนน 25 ต่อ 18 คะแนน และกำลังเล่นใน set ที่ 2 โดย B กำลังนำ A อยู่ 8 ต่อ 2 คะแนน และการแข่งขันยังไม่จบ

ตัวอย่างที่ 3: "AABABABAABBBBAAABBABBBBBAAAABBBBBBBBBABAAAAAAAAAABABBBAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBABAAAAABBBBABABABABBABABABABABABABABAABBBBBBBB" จะหมายความว่า B ชนะใน set ที่ 1 ด้วยคะแนน 28 ต่อ 26 คะแนน และ A ชนะใน set ที่ 2 ด้วยคะแนน 25 ต่อ 0 คะแนน และ B ชนะใน set ที่ 3 ด้วยคะแนน 25 ต่อ 1 คะแนน และ B ชนะใน set ที่ 4 ด้วยคะแนน 25 ต่อ 19 คะแนน ผลการแข่งขันสรุปได้ว่า B ชนะ A ไป 3 ต่อ 1 set

จงเขียนโปรแกรมรับค่า String และแสดงผลการแข่งขันในปัจจุบันแยกตาม set หากการแข่งขันทราบผลการแข่งขันว่าทีมใดเป็นผู้ชนะแล้ว ให้แสดงผลผู้ชนะ และผลการแข่งขันด้วย (ดูตัวอย่างประกอบ)

#Sample Case 1-3 เป็นตัวอย่าง 1-3 ด้านบน

### Input Specification

1 บรรทัด

บรรทัดที่ 1: เป็นข้อความ String ที่มีตัวอักษร A หรือ B เรียงไปเรื่อยๆ มีความยาวอย่างน้อย 0 ตัวอักษร

### Output Specification

มีหลายบรรทัด สูงสุด 6 บรรทัด โดย 5 บรรทัดแรก (อาจจะไม่มีครบ 5 บรรทัดก็ได้ขึ้นกับข้อมูลที่รับเข้ามา)
จะมีรูปแบบ

Set 1: A (คะแนนของ A) | B (คะแนนของ B)
Set 2: A (คะแนนของ A) | B (คะแนนของ B)
Set 3: A (คะแนนของ A) | B (คะแนนของ B)
Set 4: A (คะแนนของ A) | B (คะแนนของ B)
Set 5: A (คะแนนของ A) | B (คะแนนของ B)

บรรทัดสุดท้ายจะเป็นข้อความใดหนึ่งจาก 3 บรรทัดต่อไปนี้

A won จำนวน set ที่ A ชนะ: จำนวน set ที่ B ชนะ set

B won จำนวน set ที่ B ชนะ: จำนวน set ที่ A ชนะ set

The game has not finished yet.


** ถ้ายังไม่ได้เริ่มการแข่งขัน หรือ จบ Set ไปแล้วพอดี และยังสรุปไม่ได้ว่าใครเป็นผู้ชนะ โดยที่ยังไม่มีข้อมูลการแข่งขันใน Set ต่อไป ให้แสดงคะแนนเริ่มต้น (0 คะแนน) ของ Set ต่อไปไว้ด้วย ดังตัวอย่างใน Sample case 4




### Test Case 1

**Input**

```
AABAABA
```
**Expected Output**

```
Set 1: A (5) | B (2)
The game has not finished yet.
```


### Test Case 2

**Input**

```
AABAABA
```
**Expected Output**

```
Set 1: A (5) | B (2)
The game has not finished yet.
```


### Test Case 3

**Input**

```
AABABABAABBBBAAABBABBBBBAAAABBBBBABABAABBBBBBBBBBABBA
```
**Expected Output**

```
Set 1: A (18) | B (25)
Set 2: A (2) | B (8)
The game has not finished yet.
```


### Test Case 4

**Input**

```
AABABABAABBBBAAABBABBBBBAAAABBBBBBBBBABAAAAAAAAAABABBBAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBABAAAAABBBBABABABABBABABABABABABABABAABBBBBBBB
```
**Expected Output**

```
Set 1: A (26) | B (28)
Set 2: A (25) | B (0)
Set 3: A (1) | B (25)
Set 4: A (19) | B (25)
B won 3:1 set
```


### Test Case 5

**Input**

```
BBAABBAABAABABBABABABAABBABBABAAAABBABBABBABABAABABB
```
**Expected Output**

```
Set 1: A (25) | B (27)
Set 2: A (0) | B (0)
The game has not finished yet.
```
