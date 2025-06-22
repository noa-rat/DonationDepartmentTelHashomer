# Donations Department + Maternity Ward Tel HaShomer Sheba Hospital
## שער
**מגישות:** עדינה לב ונעה רט

**מערכת:** בית החולים שיבא – תל השומר

**יחידה:** מחלקת התרומות ובהמך מחלקת יולדות


# שלב א

## תוכן העניינים
1. [תיאור כללי](#תיאור-כללי)
2. [דיאגרמת ה-ERD](#דיאגרמת-ה-ERD)
3. [דיאגרמת ה-DSD](#דיאגרמת-ה-DSD)
4. [הכנסת נתונים מקבצים](#הכנסת-נתונים-מקבצים)
5. [הכנסת נתונים מ-mockaroo](#הכנסת-נתונים-מ-mockaroo)
6. [הכנסת נתונים עם python](#הכנסת-נתונים-עם-python)
7. [גיבוי נתונים](#גיבוי-נתונים)
8. [שחזור נתונים](#שחזור-נתונים)
   
## תיאור כללי
מחלקת התרומות של בית החולים שיבא – תל השומר אחראית על גיוס וניהול תרומות לתמיכה בפעילות הרפואית, המחקרית והקהילתית של בית החולים. המחלקה פועלת על מנת לחבר בין תורמים פרטיים, ארגונים, ועמותות לבין צרכים שונים של בית החולים, כגון רכישת ציוד רפואי מתקדם, מימון מחקרים חדשניים, שיפור תנאי האשפוז ושירותים נוספים למטופלים. מחלקת התרומות בתל השומר פועלת מתוך מחויבות לרווחת המטופלים ושיפור השירותים הרפואיים, תוך טיפוח קשרים ארוכי טווח עם תורמים ותומכים מכל רחבי העולם.
הישויות במערכת ניהול התרומות
- **תרומות (Donations)** – כל תרומה נרשמת במערכת עם פרטים כמו סכום ומועד התרומה ואמצעי התשלום. תרומה יכולה להיות מיועדת לפרוייקט ספציפי או ניתן לפצל אותה בין המחלקות.  
- **תורמים (Donors)** – אנשים פרטיים, חברות, קרנות ועמותות התורמים לבית החולים. לכל תורם נשמרים פרטי הקשר שלו, אך ניתן לשמור על אנונימיות. ניתן לתרום דרך מגייס ממחלקת התרומות, וניתן לתרום באופן עצמאי. 
- **אירועים (Events)** – אירועי גיוס כספים והוקרה לתורמים שנערכים על ידי מחלקת התרומות. אירועים אלו מסייעים לגיוס משאבים ותורמים נוספים, ומחזקים את הקשר בין התורמים לבית החולים.
- **פרויקטים (Projects)** – יוזמות ייחודיות בבית החולים שמקבלות מימון מתרומות, כגון הקמת מחלקות חדשות, מחקרים רפואיים, או תוכניות לשיפור רווחת המטופלים. צוות מחלקת התרומות מגייסים כספים לביצוע הפרויקטים. כל תרומה לפרויקט מיועדת אליו, ולא ניתן לחלק אותה למספר יעדים. 
- **צוות (Staff)** – אנשי הצוות במחלקת התרומות שאחראים על תפעול המערכת ותקשורת עם תורמים למטרת גיוס כספים למחלקות בית החולים ולפרויקטים מיוחדים כמו הקמת אגף שיקום חדש. לעיתים הם מארגנים אירועי התרמה כדי לגייס תורמים נוספים.
- **מחלקות (Departments)** – מחלקות בית החולים הנהנות מהתרומות, כגון אונקולוגיה, ילדים, שיקום ועוד. לכל מחלקה יש יעד גיוס תרומות שנתי.

## דיאגרמת ה-ERD
![ERD](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/ERD.png)

## דיאגרמת ה-DSD
![DSD](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/RelationalSchema.png)


## הכנסת נתונים מקבצים
![csv](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/inset_from_csv.jpg)

## הכנסת נתונים מ-mockaroo
![mocaroo](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/mockarooFiles/Donations_Mockaroo.jpg)

## הכנסת נתונים עם python
![python](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/Programming/insert_to_pgadmin_output.jpg)

## גיבוי נתונים
![גיבוי](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/backup_image.png)

## שחזור נתונים
![שחזור](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20א/reconstruction_image.png)


# שלב ב

# שאילתאות, אילוצים, rollback + commit

## תוכן העניינים
1. [שאילתא 1](#שאילתא-1)
2. [שאילתא 2](#שאילתא-2)
3. [שאילתא 3](#שאילתא-3)
4. [שאילתא 4](#שאילתא-4)
5. [שאילתא 5](#שאילתא-5)
6. [שאילתא 6](#שאילתא-6)
7. [שאילתא 7](#שאילתא-7)
8. [שאילתא 8](#שאילתא-8)
9. [מחיקה 1](#מחיקה-1)
10. [מחיקה 2](#מחיקה-2)
11. [מחיקה 3](#מחיקה-3)
12. [עדכון 1](#עדכון-1)
13. [עדכון 2](#עדכון-2)
14. [עדכון 3](#עדכון-3)
15. [אילוץ 1](#אילוץ-1)
16. [אילוץ 2](#אילוץ-2)
17. [אילוץ 3](#אילוץ-3)
18. [RollbackCommit](#RollbackCommit)
 
## שאילתא 1
**תיאור:** תורמים שתרמו למחלקות (ולא לפרויקטים) בהוראת קבע אך הם אינם חברים.
![SELECT1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_1.png)

## שאילתא 2
**תיאור:** אנשי צוות לפי כמות התרומות שגייסו לפרויקטים שהסתיימו, בסדר יורד (כולל עמודה של הסכומים).
![SELECT2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_2.png)

## שאילתא 3
**תיאור:** רשימת התורמים שתרמו תוך חודש מההשתתפות באירוע.
![SELECT3](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_3_0.png)
![SELECT3](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_3.png)

## שאילתא 4
**תיאור:** רשימת כל המחלקות וסכום התרומות שקיבלו בשלוש שנים האחרונות.
![SELECT4](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_4.png)

## שאילתא 5
**תיאור:** מציג לכל איש צוות את מספר התורמים שהביא לאירועים, כמה מהם תרמו בפועל, ואת שיעור ההצלחה באחוזים.
![SELECT5](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_5_0.png)
![SELECT5](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_5.png)

## שאילתא 6
**תיאור:** תורמים שתרמו יותר לפרויקטים מאשר למחלקות ממוין לפי גובה סכום התרומות לפרויקטים.
![SELECT6](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_6_0.png)
![SELECT5](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_6.png)

## שאילתא 7
**תיאור:** רשימת תורמים שתרמו יותר מ-60% מהכספים שגויסו למחלקה ספציפית.
![SELECT7](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא7_new.png)

## שאילתא 8
**תיאור:** מציג לכל אירוע לאיזו מחלקה או פרויקט הוא התרים הכי הרבה, כולל הסכום.
![SELECT8](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_8_0.png)
![SELECT5](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא_8.png)

## מחיקה 1
**תיאור:** מחק כל חבר צוות שלא הביא תורמים, לא ארגן אירועים ואינו "מנהל".

**לפני**
![DELETE11](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_1_לפני.png)

**הרצה**
![DELETE12](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_1_הרצה.png)

**אחרי**
![DELETE13](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_1_אחרי.png)

## מחיקה 2
**תיאור:** מחק פרויקטים שבהם התרומות שהתקבלו היו פחות מ-5% מיעד הגיוס והם מסומנים כ"ongoing" אך תאריך ההתחלה חלף לפני שנה לפחות.

**לפני**
![DELETE21](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_2_לפני.png)

**הרצה**
![DELETE22](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/DELETE2_הרצה.png)

**אחרי**
![DELETE23](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_2_אחרי.png)

## מחיקה 3
**תיאור:** מחק תורמים שבשנתיים האחרונות תרמו רק פעם אחת (או בכלל לא) ולא השתתפו בשום אירוע.

**לפני**
![DELETE31](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_3_לפני.png)

**הרצה**
![DELETE32](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_3_הרצה.png)

**אחרי**
![DELETE33](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/דליט_3_אחרי.png)

## עדכון 1
**תיאור:** להעלות ב-5% את שכרם של עשרת אנשי הצוות שהביאו את סכום התרומות הגבוה ביותר בחצי השנה האחרונה.

**לפני**
![UPDATE11](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_1_לפני.png)

**הרצה**
![UPDATE12](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_1_הרצה.png)

**אחרי**
![UPDATE13](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_1_אחרי.png)

## עדכון 2
**תיאור:** להפוך תורמים שתרמו לפחות 10,000 ש"ח והשתתפו לפחות ב-2 אירועים בשנה האחרונה לחברים.

**לפני**
![UPDATE21](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_2_לפני.png)

**אחרי**
![UPDATE22](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_2_אחרי.png)

## עדכון 3
**תיאור:** לסמן את הפרויקטים שהגיעו ליעד הגיוס שלהם כסגורים.

**לפני**
![UPDATE31](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_3_לפני.png)

**הרצה**
![UPDATE32](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_3_הרצה.png)

**אחרי**
![UPDATE33](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/עדכון_3_אחרי.png)

## אילוץ 1
**תיאור:** הוסף אילוץ unique (ערך ייחודי) עבור e_name, e_date, e_location.

**הרצה**
![CONSTRAINT11](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/אילוץ_1_הרצה.png)

**דוגמה לשגיאה**
![CONSTRAINT12](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/אילוץ_1_שגיאה.png)

## אילוץ 2
**תיאור:** אי אפשר שיהיה לפרוייקט תאריך התחלה יותר מאוחר מתאריך הסיום.

**הרצה**
![CONSTRAINT21](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/אילוץ_2_הרצה.png)

**דוגמה לשגיאה**
![CONSTRAINT22](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/אילוץ_2_שגיאה.png)


## אילוץ 3
**תיאור:** שכר של איש צוות חייב להיות מספר חיובי.

**הרצה**
![CONSTRAINT31](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/אילוץ_3_הרצה.png)

**דוגמה לשגיאה**
![CONSTRAINT32](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/אילוץ_3_שגיאה.png)


## RollbackCommit

![ROLLBACKCOMMIT1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/RollbackCommit1_new.png)

![ROLLBACKCOMMIT2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/RollbackCommit2_new.png)

![ROLLBACKCOMMIT3](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/RollbackCommit3_new.png)


# שלב ג
# אינטגרציה
## תוכן עניינים
1. [תרשימים](#תרשימים)
2. [החלטות האינטגרציה](#החלטות_האינטגרציה)
4. [תהליך האינטגרציה](#תהליך_האינטגרציה)
5. [מבטים ושאילתות](#מבטים_ושאילתות)

## תרשימים
**תרשים ה-DSD של מחלקת יולדות:**
![DSD](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/DSD.png)

**תרשים ה-ERD של מחלקת יולדות:**
![ERD](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/ERD.png)

**תרשים ה-DSD המשותף:**
![IntegratedDSD](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/IntegratedDSD.png)

**תרשים ה-ERD המשותף:**
![IntegratedERD](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/IntegratedERD.png)

## החלטות האינטגרציה
תחילה יצירנו ישות חדשה בשם person שמכילה מידע כללי על אנשים בעולם.

הוספנו 2 ישויות חדשות שיורשות מ-person, האחת היא staffMember שמייצגת כלל אנשי הצוות שעובדים בבית החולים, והשניה היא patient שמייצגת את כלל המטופלים בבית החולים. בנוסף הפכנו את donor לישות יורשת מ-person.

הפכנו את doctor ו-nurse לישויות יורשות מ-staffMember. את הישות staffMember המקורית שלנו שינינו ל-fundraiser והפכנו גם אותה לישות יורשת מהישות staffMember החדשה.

כמו כן, הפכנו את mother ו-baby לישויות יורשות מ-patient.
בבסיס נתונים המקורי של מחלקת יולדות, היה מפתח זר של doctor_id שהיה אחד מהתכונות של mother. הפכנו את המפתח הזר הזה להיות תכונה של הישות patient, כלומר לכלל המטופלים יש רופא מטפל, כולל baby.
בנוסף, בבסיס נתונים המקורי של מחלקת יולדות, היה מפתח זר של room_number שהיה אחד מהתכונות של mother. הפכנו את המפתח הזר הזה להיות תכונה של הישות patient, כלומר לכלל המטופלים יש חדר לשהות בו. 

הוספנו מפתח זר של d_name (של הישות מחלקה) ל-staffMember כדי שנוכל לדעת באיזה מחלקה כל איש צוות עובד (כמובן בחרנו להגדיר את המחלקה של כל fundraiser להיות Donations Department).
וכן הוספנו מפתח זר של d_name (של הישות מחלקה) ל-room כדי שנוכל לדעת באיזה מחלקה נמצא כל חדר, והפכנו את room להיות ישות חלשה של department כי לא יתכן חדר שלא נמצא באחת המחלקות.

הוספנו תכונה אופציונלית לישות towards (הישות שמקשרת בין donation ו-department, כלומר לאילו מחלקות מיועדת התרומה) של המפתח של room שהוא (room_number, d_name) שיורה האם התרומה מיועדת לחדר מסוים (לבנייתו או לשיפוצו).

## תהליך האינטגרציה
קודם כל הוספנו את הטבלאות החדשות שלא היו בשני הפרוייקטים.

את טבלאות הקיימות שרצינו להפוך להיות טבלאות יורשות יצרנו מחדש, כי אי אפשר ב-pgadmin לכתוב פקודה להוסיף את הירושה, אלא צריך ליצור מחדש. העברנו את כל הנתונים מהטבלאות הישנות לטבלאות החדשות, וכמובן הוספנו עמודות חדשות אם היה צורך.

בהעברה, כל ה-id-ים הקיימים הפכו להיות ה-person_id וכל ה-id-ים החדשים (employee_id, patient_id) נוצרו אוטומטית עם sequence. כאשר העברנו את הנתונים היינו צריכות לפעמים לשנות את ה-person_id אם היו חפיפות בין טבלאות יורשות. במידה וזה קרה, יצרנו טבלת עזר לעשות מיפוי בין ה-person_id הישן וה-person_id החדש (שנבחר על ידי sequence). אחרי שיצרנו את טבלאות המיפוי, שנינו את הperson_id והמפתחות הזרים בהתאם.

רצינו שלכל patient יהיה את האופציה של medicine כי כל מטופל יכול לקבל תרופה ולא רק יולדות, לכן היה צריך להחליף את המפתח הזר ב-prescription מ-mother_id ל-patient_id. זה גרם לבעיה, בגלל שלא יכולנו לשים את המפתח הזר של טבלת האב, לכן הוספנו טבלת עזר שמכילה את כל ה-patient_id-ים, כתבנו פונקציות הוספה ומחיקה של patient_id מהטבלה הזו, ויצרנו trigger-ים ביצירה ובמחיקה של mother או baby לקרוא לפונקציות האלו. לאחר מכן עשינו שהמפתח הזר של prescription יפנה לאותה טבלת העזר.

לבסוף, דאגנו שכל המפתחות זרים יפנו לישות הנכונה.    

## מבטים ושאילתות
**תיאור ה-view מצד מחלקת התרומות:** ה-view מכיל את רוב המידע עבור כל תרומה: נתוני התרומה, התורם, המתרים, יעד התרומה ועוד.

**שליפת נתונים מה-view:**
![view1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/view1.png)
**שאילתא 1:**
תיאור: השאילתא מחזירה את סכום התרומות של כל תורם.
![view1select1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/view1select1.png)
**שאילתא 2:**
תיאור: השאילתא מחזירה את מספר המשתתפים בכל אירוע התרמה.
![view1select2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/view1select2.png)
**תיאור ה-view מצד מחלקת היולדות:** ה-view מכיל את המידע הבסיסי עבור כלל ה-persons שממחלקת היולדות, סוג ה-person ומפתחות זרים.

**שליפת נתונים מה-view:**
![view2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/view2.png)
**שאילתא 1:**
תיאור: השאילתא מחזירה את כל התינוקות של כל יולדת.
![view2select1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/view2select1.png)
**שאילתא 2:**
תיאור: השאילתא מחזירה את כל היולדות המטופלות ע"י כל רופא.
![view2select2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ג/view2select2.png)

# שלב ד
# תכניות

## תוכן עניינים
1. [תוכנית ראשית 1](#תוכנית_ראשית_1)
2. [תוכנית ראשית 2](#תוכנית_ראשית_2)
3. [טריגר 1א](#טריגר_1א)
4. [טריגר 1ב](טריגר_1ב)
5. [טריגר 2](טריגר_2)

## תוכנית ראשית 1
**תיאור מילולי:** 
הקוד מקבל את המידע הבא על כל חדר בבית החולים:
1. אם יש בו מטופלים, האם הוקצתה לו אחות?
2. מהי התפוסה המקסימלית ומהי התפוסה הנוכחית?
לאחר מכן, אם יש חדר עם דיירים שאין לו אחות שהוקצתה לו, יש להקצות אחות אם קיימת אחת זמינה. בנוסף, אם יש חדר שיש בו יותר מטופלים מהמקסימום, יש להקצות מטופלים מיותרים לחדרים אחרים בבמחלקה אם יש מקום פנוי.

**הקוד:**
```sql
DO $$
DECLARE
    room_cur REFCURSOR;
    rec RECORD;
BEGIN
    -- Call function to get the refcursor
    room_cur := get_room_occupancy_info();

    -- Fetch all from the cursor and print room info
    LOOP
        FETCH room_cur INTO rec;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE 'Room % in Dept %: Capacity=%, Occupancy=%, Nurse Assigned=%',
            rec.room_number, rec.d_name, rec.capacity, rec.current_occupancy, rec.nurse_assigned;
    END LOOP;
    CLOSE room_cur;

    -- Call the procedure to assign nurses and move patients
    CALL assign_nurses_to_unassigned_rooms();

    RAISE NOTICE 'Nurses assigned and patients shifted if needed.';
END;
$$ LANGUAGE plpgsql;
```


**צילום מסך לפני הרצת התוכנית:**

![before_changes2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/before_changes1.png)

**צילום מסך של הרצת התוכנית:**

![run_main_program2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/run_main_program1.png)


**צילום מסך אחרי הרצת התוכנית:**

![after_changes2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/after_changes1.png)

### הפונקציה get_room_occupancy_info():

**תיאור מילולי:** 

פונקציה שמחזירה את המידע הנוגע לחדר מסוים: המחלקה שלו, תפוסה מקסימלית, תפוסה נוכחית, ו-true/false אם מוקצית לו אחות

**הקוד:** 

```sql
CREATE OR REPLACE FUNCTION get_room_occupancy_info()
RETURNS REFCURSOR AS $$
DECLARE
    ref refcursor := 'room_cursor';
BEGIN
    OPEN ref FOR
    SELECT 
        r.room_number,
        r.d_name,
        r.capacity,
        COUNT(p.patient_id) AS current_occupancy,
        CASE 
            WHEN EXISTS (
                SELECT 1 FROM nurse_room nr 
                WHERE nr.room_number = r.room_number AND nr.d_name = r.d_name
            )
            THEN TRUE ELSE FALSE 
        END AS nurse_assigned
    FROM room r
    LEFT JOIN patient p 
        ON p.room_number = r.room_number AND p.d_name = r.d_name
    GROUP BY r.room_number, r.d_name, r.capacity;

    RETURN ref;
END;
$$ LANGUAGE plpgsql;
```


### הפרוצדורה assign_nurses_to_unassigned_rooms():

**תיאור מילולי:** 

פרוצדורה לארגון החדרים: אם מספר הדיירים הנוכחי גדול מהמספר המקסימלי, יש להחליף חדרים אם יש מקום פנוי במחלקה. אם אין אחות שהוקצתה לחדר, יש להקצות אותה במידת האפשר.

**הקוד:**

```sql
CREATE OR REPLACE PROCEDURE assign_nurses_to_unassigned_rooms()
LANGUAGE plpgsql
AS $$
DECLARE
    cur_room CURSOR FOR
        SELECT r.room_number, r.d_name, r.capacity, COUNT(p.patient_id) AS occupancy
        FROM room r
        LEFT JOIN patient p ON r.room_number = p.room_number AND r.d_name = p.d_name
        GROUP BY r.room_number, r.d_name, r.capacity;

    rec_room RECORD;
    nurse_id INT;
    extra_patients INT;
    cur_patient RECORD;
    alt_room INT;
BEGIN
    OPEN cur_room;
    LOOP
        FETCH cur_room INTO rec_room;
        EXIT WHEN NOT FOUND;

        -- Assign a nurse if none is assigned yet
        IF NOT EXISTS (
            SELECT 1 FROM nurse_room nr
            WHERE nr.room_number = rec_room.room_number AND nr.d_name = rec_room.d_name
        ) THEN
            SELECT employee_id INTO nurse_id
            FROM nurse
            WHERE d_name = rec_room.d_name
            LIMIT 1;

            IF nurse_id IS NOT NULL THEN
                INSERT INTO nurse_room(nurse_id, room_number, d_name)
                VALUES (nurse_id, rec_room.room_number, rec_room.d_name);
            ELSE
                RAISE NOTICE 'No nurse available for room % in department %.',
                    rec_room.room_number, rec_room.d_name;
            END IF;
        END IF;

        -- Check for over-occupancy
        IF rec_room.occupancy > rec_room.capacity THEN
            extra_patients := rec_room.occupancy - rec_room.capacity;

            -- Fetch extra patients to move
            FOR cur_patient IN
                SELECT patient_id, person_id FROM patient
                WHERE room_number = rec_room.room_number AND d_name = rec_room.d_name
                ORDER BY admission_date DESC
                LIMIT extra_patients
            LOOP
                -- Find another room in same department with available space
                SELECT available_room.room_number INTO alt_room
                FROM (
                    SELECT r.room_number, r.capacity, COUNT(p.patient_id) AS current_occupancy
                    FROM room r
                    LEFT JOIN patient p ON r.room_number = p.room_number AND r.d_name = p.d_name
                    WHERE r.d_name = rec_room.d_name
                      AND r.room_number != rec_room.room_number
                    GROUP BY r.room_number, r.capacity
                    HAVING COUNT(p.patient_id) < r.capacity
                    ORDER BY r.capacity - COUNT(p.patient_id) DESC
                    LIMIT 1
                ) AS available_room;

                IF alt_room.room_number IS NOT NULL THEN
                    -- Move patient to alternative room
                    UPDATE patient
                    SET room_number = alt_room.room_number
                    WHERE patient_id = cur_patient.patient_id;

                    RAISE NOTICE 'Moved patient % to room % in department %.',
                        cur_patient.patient_id, alt_room.room_number, rec_room.d_name;
                ELSE
                    RAISE NOTICE 'No alternative room with space found for patient % in department %.',
                        cur_patient.patient_id, rec_room.d_name;
                END IF;
            END LOOP;
        END IF;
    END LOOP;
    CLOSE cur_room;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'An error occurred: %', SQLERRM;
END;
$$;
```


## תוכנית ראשית 2
**תיאור מילולי:** התוכנית מפעילה פונקציה שמחזירה את כל המחלקות שעוד לא גייסו מספיק תרומות כדי לעמוד ביעד התקציב שלהן, ואז מפעילה פרוצדורה בלולאה על כל אחת מהמחלקות שמוסיפה אירוע חדש לגיוס תרומות לאותה מחלקה ומתאמת מגייס תרומות פנוי שיארגן את האירוע.

**הקוד**

```sql
DO $$
DECLARE
    dept RECORD;
    count_departments INT := 0;
BEGIN
    RAISE NOTICE 'Starting donation check and event creation...';

    FOR dept IN SELECT * FROM get_departments_below_budget() LOOP
        count_departments := count_departments + 1;
        RAISE NOTICE 'Handling department: %', dept.department_name;
        CALL create_fundraisingEvent_for_department(dept.department_name);
        COMMIT;
    END LOOP;

    IF count_departments = 0 THEN
        RAISE NOTICE 'All departments have reached their fundraising goals.';
    ELSE
        RAISE NOTICE 'Processed % departments with unmet fundraising goals.', count_departments;
    END IF;
END $$;
```


**צילום מסך לפני הרצת התוכנית:**

![before_changes1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/before_changes2.png)

**צילום מסך של הרצת התוכנית:**

![run_main_program1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/run_main_program2.png)


**צילום מסך אחרי הרצת התוכנית:**

![after_changes1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/after_changes2.png)

### הפונקציה get_departments_below_budget():

**תיאור מילולי:** 

להחזיר את כל המחלקות שאין להן מספיק כספי תרומות כדי לעמוד בתקציב השנתי הנדרש להן לפעול.

**הקוד:** 

```sql
CREATE OR REPLACE FUNCTION get_departments_below_budget()
RETURNS TABLE (
    department_name VARCHAR,
    total_donations NUMERIC,
    required_budget NUMERIC
) AS $$
DECLARE
    rec_dept RECORD;
    total_donations NUMERIC;
BEGIN
    FOR rec_dept IN SELECT d_name, d_yearly_budget, d_funds_allocated FROM department LOOP

        -- Calculate total donations for current year
        SELECT COALESCE(SUM(d.d_amount), 0)
        INTO total_donations
        FROM donation d
        JOIN towards t ON d.donation_id = t.donation_id AND d.donor_id = t.donor_id
        WHERE t.d_name = rec_dept.d_name
          AND EXTRACT(YEAR FROM d.d_date) = EXTRACT(YEAR FROM CURRENT_DATE);

        -- Return row if donations are below expected budget
        IF total_donations < (rec_dept.d_yearly_budget - rec_dept.d_funds_allocated) THEN
            department_name := rec_dept.d_name;
            required_budget := rec_dept.d_yearly_budget - rec_dept.d_funds_allocated;
            get_departments_below_budget.total_donations := total_donations;
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
```

### הפרוצדורה create_fundraisingEvent_for_department():

**תיאור מילולי:** 

עבור כל המחלקות שלא קיבלו מספיק כספים באמצעות תרומות בשנה הקלנדרית הזו כדי לפעול, יש ליצור אירוע גיוס כספים למען המחלקה ולמנות גיוס תרומות לארגון.

**הקוד:**

```sql
CREATE OR REPLACE PROCEDURE create_fundraisingEvent_for_department(dept_name VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE
    new_event_id INT;
    fundraiser_id INT;
    proposed_date DATE := CURRENT_DATE + INTERVAL '1 month';
    proposed_location VARCHAR;
BEGIN
    RAISE NOTICE 'Handling department: %', dept_name;

    -- נסה למצוא תאריך ומיקום פנויים בלולאה
    LOOP
        -- מצא מיקום פנוי בחודש הבא
        SELECT l.location_name INTO proposed_location
        FROM (
            SELECT DISTINCT e_location AS location_name
            FROM fundraisingEvent
            WHERE e_location IS NOT NULL
        ) l
        WHERE NOT EXISTS (
            SELECT 1
            FROM fundraisingEvent fe
            WHERE fe.e_date = proposed_date
              AND fe.e_location = l.location_name
        )
        LIMIT 1;

        -- אם נמצא מיקום פנוי – צא מהלולאה
        IF proposed_location IS NOT NULL THEN
            EXIT;
        END IF;

        -- אחרת – עבור לשבוע הבא
        proposed_date := proposed_date + INTERVAL '7 day';

        -- תנאי עצירה: לא לחפש מעבר לחצי שנה קדימה
        IF proposed_date > CURRENT_DATE + INTERVAL '6 month' THEN
            RAISE EXCEPTION 'No available location for department % within a year', dept_name;
        END IF;
    END LOOP;

    -- צור את האירוע
    INSERT INTO fundraisingEvent (e_date, e_name, e_location)
    VALUES (proposed_date, 'Auto-generated event for department ' || dept_name, proposed_location)
    RETURNING e_id INTO new_event_id;

    -- מצא מגייס שאינו מארגן אירוע אחר
    SELECT f.employee_id INTO fundraiser_id
    FROM fundraiser f
    WHERE NOT EXISTS (
        SELECT 1 FROM organizes o
        WHERE o.fundraiser_id = f.employee_id
    )
    LIMIT 1;

    -- אם לא נמצא מגייס
    IF fundraiser_id IS NULL THEN
        RAISE EXCEPTION 'No available fundraiser to assign to department %', dept_name;
    END IF;

    -- קישור המגייס לארגון האירוע
    INSERT INTO organizes (fundraiser_id, e_id)
    VALUES (fundraiser_id, new_event_id);

    RAISE NOTICE 'Created event % on % at % for department %, assigned to fundraiser %',
        new_event_id, proposed_date, proposed_location, dept_name, fundraiser_id;
END;
$$;
```



# Triggers
## טריגר 1א
**תיאור מילולי:** 

כאשר מוסיפים מטופל, מקצה לו רופא באופן אוטומטי

**הקוד:** 

```sql
CREATE OR REPLACE FUNCTION assign_doctor_to_patient()
RETURNS TRIGGER AS $$
DECLARE
    assigned_doctor_id INT;
BEGIN
    SELECT d.employee_id
    INTO assigned_doctor_id
    FROM doctor d
    JOIN maximum_amount_of_patients m ON d.title = m.type_of_doctor
    WHERE d.d_name = NEW.d_name
    AND (
        SELECT COUNT(*)
        FROM patient p
        WHERE p.doctor_id = d.employee_id
          AND (p.release_date IS NULL OR p.release_date >= CURRENT_DATE)
    ) < m.max_patients
    LIMIT 1;

    IF assigned_doctor_id IS NULL THEN
        RAISE EXCEPTION 'No doctor available in department % with available capacity.', NEW.d_name;
    END IF;

    NEW.doctor_id := assigned_doctor_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_assign_doctor
BEFORE INSERT ON patient
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_patient();

CREATE TRIGGER trg_assign_doctor_mother
BEFORE INSERT ON mother
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_patient();

CREATE TRIGGER trg_assign_doctor_baby
BEFORE INSERT ON baby
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_patient();
```

## טריגר 1ב
**תיאור מילולי:** 

כאשר מוסיפים מטופל, מקצה לו חדר באופן אוטומטי

**הקוד:** 


```sql
CREATE OR REPLACE FUNCTION assign_room_to_patient()
RETURNS TRIGGER AS $$
DECLARE
    assigned_room_number INT;
BEGIN
    SELECT r.room_number
    INTO assigned_room_number
    FROM room r
    WHERE r.d_name = NEW.d_name
    AND (
        SELECT COUNT(*)
        FROM patient p
        WHERE p.room_number = r.room_number
          AND (p.release_date IS NULL OR p.release_date >= CURRENT_DATE)
    ) < r.capacity
    LIMIT 1;

    IF assigned_room_number IS NULL THEN
        RAISE EXCEPTION 'No room available in department % with available capacity.', NEW.d_name;
    END IF;

    NEW.room_number := assigned_room_number;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_assign_room_baby
BEFORE INSERT ON baby
FOR EACH ROW
EXECUTE FUNCTION assign_room_to_patient();

CREATE TRIGGER trg_assign_room_mother
BEFORE INSERT ON mother
FOR EACH ROW
EXECUTE FUNCTION assign_room_to_patient();

CREATE TRIGGER trg_assign_room_mother
BEFORE INSERT ON mother
FOR EACH ROW
EXECUTE FUNCTION assign_room_to_patient();
```

**צילום מסך של הוספת מטופל בלי רופא וחדר:**

![trigger1_insert](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/trigger1_insert.png)

**צילום מסך של המטופל שנוסף עם רופא וחדר:**

![trigger1_after](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/trigger1_after.png)


## טריגר 2
**תיאור מילולי:** 

כאשר מוסיפים מרשם (שכלל מטופל ותרופה), מקטינים את מלאי התרופה

**הקוד:**

```sql
CREATE OR REPLACE FUNCTION decrease_stock()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE medicine
    SET stock = stock - 1
    WHERE medicine_id = NEW.medicine_id;

    RETURN NEW; -- You must return NEW in a BEFORE or AFTER INSERT trigger
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_decrease_stock
BEFORE INSERT ON prescription
FOR EACH ROW
EXECUTE FUNCTION decrease_stock();
```

**צילום מסך של התרופה לפני שהוספנו עוד מרשם:**

![trigger2_before](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/trigger2_before.png)

**צילום מסך של המרשם שהוספנו:**

![trigger2_insert](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/trigger2_insert.png)

**צילום מסך של התרופה אחרי שהוספנו עוד מרשם:**

![trigger2_after](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/trigger2_after.png)


# שלב ה
# ממשק גרפי
## תוכן עניינים
1. [הוראות הפעלה](#הוראות_הפעלה)
2. [הכלים שבהם השתמשנו](#הכלים_שבהם_השתמשנו)
3. [צילומי מסך](#צילומי_מסך)

## הוראות הפעלה
**תחילה יש לערוך את קובץ הפייתון בשם db.py:**

- תחת "dbname", מלאו את שם בסיס הנתונים.
- תחת "user", מלא את שם המשתמש.
- תחת "password", מלא את הסיסמה.
- תחת "host", רשום "localhost".
- תחת "port" רשום את מספר ה-port שבו נמצא ה-postgres.

**לאחר מכן יש להריץ את הקובץ main_window.py:**

- להפעלת CRUD על הטבלאות של תרומות, תורמים, או פרוייקטים, נא לבחור "Manage" ולאחר מכן לבחור בטבלה הרלוונטית. כל אחת מהפעולות תתבצע באמעצות massege box ייעודי.
- להפעלת שאילתות, נא לבחור "Analyze" ולאחר מכן לבחור בשאילתא הרלוונטית. תוצאות השאילתא יופיעו בטבלה המופיעה בחלקו התחתון של המסך.
- להפעלת פונקציה + פרוצדורה, נא לבחור "Automate". הדפסות הפרוצדורה יופיעו בטבלה הימנית, ובטבלה השמאלית יתעדכנו השינויים.
  
## הכלים שבהם השתמשנו:

כדי להתממשק עם בסיס הנתונים, בחרנו להשתמש בספריה psycopg2 של Python, וכדי ליצור ממשק גרפי בחרנו להשתמש בספריה PyQt.

השימוש בספריות הנ"ל פשוט וידידותי, ומאפשר ביצוע חלק במינימום קוד.

## צילומי מסך

העמוד הראשי:

![main](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ה/main.png)

עמוד המעבר לעדכון טבלאות:

![manage](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ה/manage.png)

אחד מעמודי ה-CRUD:

![donor](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ה/donor.png)

ביצוע create לדוגמה:

![create](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ה/create.png)

הפעלת שאילתא:

![select](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ה/select.png)

הפעלת הפונקציה + פרוצדורה:

![auto](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ה/auto.png)

