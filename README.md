# DonationDepartmentTelHashomer
## תיאור כללי
מחלקת התרומות של בית החולים שיבא – תל השומר אחראית על גיוס וניהול תרומות לתמיכה בפעילות הרפואית, המחקרית והקהילתית של בית החולים. המחלקה פועלת על מנת לחבר בין תורמים פרטיים, ארגונים, ועמותות לבין צרכים שונים של בית החולים, כגון רכישת ציוד רפואי מתקדם, מימון מחקרים חדשניים, שיפור תנאי האשפוז ושירותים נוספים למטופלים. מחלקת התרומות בתל השומר פועלת מתוך מחויבות לרווחת המטופלים ושיפור השירותים הרפואיים, תוך טיפוח קשרים ארוכי טווח עם תורמים ותומכים מכל רחבי העולם.
הישויות במערכת ניהול התרומות
- **תרומות (Donations)** – כל תרומה נרשמת במערכת עם פרטים כמו סכום ומועד התרומה ואמצעי התשלום. תרומה יכולה להיות מיועדת לפרוייקט ספציפי או ניתן לפצל אותה בין המחלקות.  
- **תורמים (Donors)** – אנשים פרטיים, חברות, קרנות ועמותות התורמים לבית החולים. לכל תורם נשמרים פרטי הקשר שלו, אך ניתן לשמור על אנונימיות. ניתן לתרום דרך מגייס ממחלקת התרומות, וניתן לתרום באופן עצמאי. 
- **אירועים (Events)** – אירועי גיוס כספים והוקרה לתורמים שנערכים על ידי מחלקת התרומות. אירועים אלו מסייעים לגיוס משאבים ותורמים נוספים, ומחזקים את הקשר בין התורמים לבית החולים.
- **פרויקטים (Projects)** – יוזמות ייחודיות בבית החולים שמקבלות מימון מתרומות, כגון הקמת מחלקות חדשות, מחקרים רפואיים, או תוכניות לשיפור רווחת המטופלים. צוות מחלקת התרומות מגייסים כספים לביצוע הפרויקטים. כל תרומה לפרויקט מיועדת אליו, ולא ניתן לחלק אותה למספר יעדים. 
- **צוות (Staff)** – אנשי הצוות במחלקת התרומות שאחראים על תפעול המערכת ותקשורת עם תורמים למטרת גיוס כספים למחלקות בית החולים ולפרויקטים מיוחדים כמו הקמת אגף שיקום חדש. לעיתים הם מארגנים אירועי התרמה כדי לגייס תורמים נוספים.
- **מחלקות (Departments)** – מחלקות בית החולים הנהנות מהתרומות, כגון אונקולוגיה, ילדים, שיקום ועוד. לכל מחלקה יש יעד גיוס תרומות שנתי.

##  דיאגרמא ה-ERD


## דיאגרמא ה-DSD


## סקריפט ליצירת הטבלאות
```sql
CREATE TABLE IF NOT EXISTS public."Donations"
(
    donation_id integer NOT NULL,
    donor_id integer NOT NULL,
    donation_date date NOT NULL,
    donation_amount double precision NOT NULL,
    donation_method payment_method NOT NULL,
    project_id integer,
    CONSTRAINT "Donations_pkey" PRIMARY KEY (donation_id, donor_id),
    CONSTRAINT donor_id FOREIGN KEY (donor_id)
        REFERENCES public."Donors" (donor_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT project_id FOREIGN KEY (project_id)
        REFERENCES public."Projects" (project_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

CREATE TABLE IF NOT EXISTS public."Departments"
(
    dept_name text COLLATE pg_catalog."default" NOT NULL,
    contact_email text COLLATE pg_catalog."default" NOT NULL,
    contact_phone bigint NOT NULL,
    year_money_allocated double precision NOT NULL,
    year_budget double precision NOT NULL,
    CONSTRAINT "Departments_pkey" PRIMARY KEY (dept_name)
)

CREATE TABLE IF NOT EXISTS public."Donors"
(
    donor_id integer NOT NULL,
    member boolean NOT NULL,
    total_donations integer NOT NULL,
    email text COLLATE pg_catalog."default",
    phone_number text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    staff_id integer,
    CONSTRAINT "Donors_pkey" PRIMARY KEY (donor_id),
    CONSTRAINT staff_id FOREIGN KEY (staff_id)
        REFERENCES public."Staff" (staff_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

CREATE TABLE IF NOT EXISTS public."Events"
(
    event_name text COLLATE pg_catalog."default" NOT NULL,
    event_date date NOT NULL,
    event_location text COLLATE pg_catalog."default" NOT NULL,
    funds_raised double precision,
    CONSTRAINT "Events_pkey" PRIMARY KEY (event_name, event_date, event_location)
)

CREATE TABLE IF NOT EXISTS public."Projects"
(
    project_id integer NOT NULL,
    project_name text COLLATE pg_catalog."default" NOT NULL,
    project_description text COLLATE pg_catalog."default",
    start_date date,
    end_date date,
    fundraising_goal bigint,
    funds_raised double precision,
    project_status project_status,
    CONSTRAINT "Projects_pkey" PRIMARY KEY (project_id)
)

CREATE TABLE IF NOT EXISTS public."Staff"
(
    staff_id integer NOT NULL,
    "position" text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    phone_number bigint NOT NULL,
    salary double precision NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Staff_pkey" PRIMARY KEY (staff_id)
)

CREATE TABLE IF NOT EXISTS public."connected to"
(
    staff_id integer NOT NULL,
    project_id integer NOT NULL,
    CONSTRAINT "connected to_pkey" PRIMARY KEY (staff_id, project_id),
    CONSTRAINT project_id FOREIGN KEY (project_id)
        REFERENCES public."Projects" (project_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT staff_id FOREIGN KEY (staff_id)
        REFERENCES public."Staff" (staff_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS public.organizes
(
    staff_id integer NOT NULL,
    event_name text COLLATE pg_catalog."default" NOT NULL,
    event_date date NOT NULL,
    event_location text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT organizes_pkey PRIMARY KEY (staff_id, event_name, event_date, event_location),
    CONSTRAINT event_location FOREIGN KEY (event_name, event_date, event_location)
        REFERENCES public."Events" (event_name, event_date, event_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT staff_id FOREIGN KEY (staff_id)
        REFERENCES public."Staff" (staff_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS public."participates in"
(
    donor_id integer NOT NULL,
    event_name text COLLATE pg_catalog."default" NOT NULL,
    event_date date NOT NULL,
    event_location text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "participates in_pkey" PRIMARY KEY (donor_id, event_name, event_date, event_location),
    CONSTRAINT donor_id FOREIGN KEY (donor_id)
        REFERENCES public."Donors" (donor_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT event_location FOREIGN KEY (event_name, event_date, event_location)
        REFERENCES public."Events" (event_name, event_date, event_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS public."raises for"
(
    staff_id integer NOT NULL,
    dept_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "raises for_pkey" PRIMARY KEY (staff_id, dept_name),
    CONSTRAINT dept_name FOREIGN KEY (dept_name)
        REFERENCES public."Departments" (dept_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT staff_id FOREIGN KEY (staff_id)
        REFERENCES public."Staff" (staff_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS public.towards
(
    donation_id integer NOT NULL,
    donor_id integer NOT NULL,
    dept_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT towards_pkey PRIMARY KEY (donation_id, donor_id, dept_name),
    CONSTRAINT dept_name FOREIGN KEY (dept_name)
        REFERENCES public."Departments" (dept_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT donor_id FOREIGN KEY (donation_id, donor_id)
        REFERENCES public."Donations" (donation_id, donor_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

```

## כמה מהטבלאות עם נתונים
