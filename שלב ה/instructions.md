# DonationDepartmentTelHashomer
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

![main](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/main.png)

עמוד המעבר לעדכון טבלאות:

![manage](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/manage.png)

אחד מעמודי ה-CRUD:

![donor](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/donor.png)

ביצוע create לדוגמה:

![create](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/create.png)

הפעלת שאילתא:

![select](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/select.png)

הפעלת הפונקציה + פרוצדורה:

![auto](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/auto.png)

![before_changes2](https://raw.githubusercontent.com/noa-rat/DonationDepartmentTelHashomer/main/שלב%20ד/before_changes1.png)
