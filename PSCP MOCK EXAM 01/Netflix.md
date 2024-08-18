# Netflix





ราคาค่าสมาชิกรายเดือนแบบ Package หรือ Plan แบบต่างๆของ Netflix ประเทศไทย จากข้อมูลที่ https://help.netflix.com/en/node/24926 เมื่อเดือน ก.ย. 2565 เป็นไปดังรูปนี้






หากรับความต้องการของผู้ที่ต้องการสมัครสมาชิก Netflix เข้ามา จงเขียนโปรแกรมเพื่อแนะนำ package (plan) สมาชิกที่เหมาะสมกับลูกค้ามากที่สุด (ตรงหรือเกินความต้องการทุกข้อ และมีราคาถูกที่สุด) โดยแสดงชื่อ Package และจำนวน Package นั้น รวมถึงราคาที่จ่ายทั้งหมด



หากมีหลาย package ที่แนะนำให้เรียงจาก package ที่มีราคาสูงที่สุดไปต่ำที่สุด





 

![](https://ejudge.it.kmitl.ac.th/uploads/1662792146_netflix.png)

![](https://ejudge.it.kmitl.ac.th/uploads/1662698423_Screen%20Shot%202565-09-09%20at%2011.38.33.png)

### Input Specification

มีจำนวน 7 บรรทัด แต่ละบรรทัดแสดงความต้องการขั้นต่ำที่ต้องการ ที่จะต้องมีอย่างน้อยตามที่กำหนดหรือผ่านทุกข้อ 



บรรทัดที่ 1 แสดง Number of screens you can watch on at the same time มีค่าเป็นจำนวนเต็มบวก

บรรทัดที่ 2 แสดง Number of phones or tablets you can have downloads on มีค่าเป็นจำนวนเต็มบวก

บรรทัดที่ 3 แสดง Unlimited movies, TV shows and mobile games มีค่าเป็น Yes หรือ No

บรรทัดที่ 4 แสดง Watch on your mobile phone and tablet มีค่าเป็น Yes หรือ No

บรรทัดที่ 5 แสดง Watch on your laptop and TV มีค่าเป็น Yes หรือ No

บรรทัดที่ 6 แสดง HD available มีค่าเป็น Yes หรือ No

บรรทัดที่ 7 แสดง Ultra HD available มีค่าเป็น Yes หรือ No



** Yes หมายความว่าต้องการ และ No หมายความว่าไม่ต้องการ

### Output Specification

มีได้หลายบรรทัด ในรูปแบบ ชื่อ Package x จำนวน Package (เป็นจำนวนเต็มบวก) ที่แนะนำ โดยเรียงจาก Package ที่มีราคาสูงที่สุดไปต่ำสุด

ชื่อ Package มีได้ 4 ชื่อ ได้แก่ Mobile, Basic, Standard และ Premium

บรรทัดสุดท้ายเป็นข้อความ Total = จำนวนเงินที่ต้องจ่ายตาม Package ที่แนะนำ THB



### Test Case 1

**Input**

```
1
1
Yes
Yes
No
No
No
```
**Expected Output**

```
Mobile x 1
Total = 99 THB
```


### Test Case 2

**Input**

```
1
1
Yes
Yes
No
No
No
```
**Expected Output**

```
Mobile x 1
Total = 99 THB
```


### Test Case 3

**Input**

```
2
1
Yes
Yes
Yes
Yes
No
```
**Expected Output**

```
Standard x 1
Total = 349 THB
```


### Test Case 4

**Input**

```
5
6
Yes
Yes
Yes
Yes
No
```
**Expected Output**

```
Premium x 1
Standard x 1
Total = 768 THB
```


### Test Case 5

**Input**

```
1
1
Yes
Yes
Yes
Yes
Yes
```
**Expected Output**

```
Premium x 1
Total = 419 THB
```


### Test Case 6

**Input**

```
3
2
No
No
No
No
No
```
**Expected Output**

```
Mobile x 3
Total = 297 THB
```


### Test Case 7

**Input**

```
1
1
Yes
No
No
No
No
```
**Expected Output**

```
Mobile x 1
Total = 99 THB
```


### Test Case 8

**Input**

```
15
14
Yes
Yes
Yes
No
No
```
**Expected Output**

```
Premium x 4
Total = 1676 THB
```


### Test Case 9

**Input**

```
13
1
Yes
Yes
Yes
No
No
```
**Expected Output**

```
Premium x 3
Basic x 1
Total = 1536 THB
```
