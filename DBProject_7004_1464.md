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

# DonationDepartmentTelHashomer

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
![SELECT7](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/שאילתא7.png)

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

![ROLLBACKCOMMIT1](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/RollbackCommit1.png)

![ROLLBACKCOMMIT2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/RollbackCommit2.png)

![ROLLBACKCOMMIT3](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ב/RollbackCommit3.png)
