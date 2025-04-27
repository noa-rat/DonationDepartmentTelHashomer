-- Constraints

-- בטבלת האירועים: הוסף אילוץ unique (ערך ייחודי) עבור e_name, e_date, e_location

ALTER TABLE FundraisingEvent
ADD CONSTRAINT unique_event_details
UNIQUE (e_name, e_date, e_location);

--  אי אפשר שיהיה לפרוייקט תאריך התחלה יותר מאוחר מתאריך סיום
ALTER TABLE Project
ADD CONSTRAINT project_end_after_start
CHECK (end_date IS NULL OR end_date >= start_date);

-- בטבלת אנשי הצוות: שכר של איש צוות חייב להיות מספר חיובי.
ALTER TABLE staffmember
ADD CONSTRAINT positive_salary
CHECK (salary > 0);
