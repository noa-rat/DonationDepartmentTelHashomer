-- ================================ VIEW 1 ===============================
-- מבט מצד מחלקת היולדות
CREATE OR REPLACE VIEW public.view_selected_persons AS
SELECT
    p.*,
    'Baby' AS person_type,
b.patient_id AS internal_id,
    b.mother_id,
    b.doctor_id
FROM public.person p
LEFT JOIN public.baby b ON p.person_id = b.person_id

UNION ALL

SELECT
    p.*,
    'Mother' AS person_type,
m.patient_id AS internal_id,
    NULL::INTEGER AS mother_id,
    m.doctor_id
FROM public.person p
LEFT JOIN public.mother m ON p.person_id = m.person_id

UNION ALL

SELECT
    p.*,
    'Doctor' AS person_type,
d.employee_id AS internal_id,
    NULL::INTEGER AS mother_id,
    NULL::INTEGER AS doctor_id
FROM public.person p
LEFT JOIN public.doctor d ON p.person_id = d.person_id

UNION ALL

SELECT
    p.*,
    'Nurse' AS person_type,
n.employee_id AS internal_id,
NULL::INTEGER AS mother_id,
    NULL::INTEGER AS doctor_id
FROM public.person p
LEFT JOIN public.nurse n ON p.person_id = n.person_id;

-- כל התינוקות של כל יולדת
SELECT
    m.person_id AS mother_id,
    m.name AS mother_name,
    b.person_id AS baby_id,
    b.name AS baby_name
FROM
    view_selected_persons m
JOIN
    view_selected_persons b
    ON b.mother_id = m.person_id
WHERE
    m.person_type = 'Mother'
    AND b.person_type = 'Baby';

-- כל היולדות שמטופלות ע"י כל רופא
SELECT
    d.person_id AS doctor_id,
    d.name AS doctor_name,
    m.person_id AS mother_id,
    m.name AS mother_name
FROM
    view_selected_persons d
JOIN
    view_selected_persons m
    ON m.doctor_id = d.internal_id
WHERE
    d.person_type = 'Doctor'
    AND m.person_type = 'Mother';


-- ============================= VIEW 2 =========================
-- מבט מצד מחלקת התרומות
CREATE OR REPLACE VIEW donation_overview AS
SELECT
    d.donation_id,                                -- מזהה התרומה
    d.d_amount,                                   -- סכום התרומה
    d.d_date,                                     -- תאריך התרומה

    donor.donor_id,                               -- מזהה התורם
    person_d.name AS donor_name,                  -- שם התורם

    fundraiser.employee_id AS fundraiser_id,      -- מזהה המתרים
    person_f.name AS fundraiser_name,             -- שם המתרים

    fe.e_id AS event_id,                          -- מזהה האירוע
    fe.e_name AS event_name,

    CASE
        WHEN d.p_id IS NOT NULL THEN 'Project'
        ELSE 'Department'
    END AS donation_target,                       -- סוג היעד

    CASE
        WHEN d.p_id IS NOT NULL THEN p.p_name
        ELSE t.d_name
    END AS target_name                             -- שם היעד

FROM
    donation d
    LEFT JOIN donor ON d.donor_id = donor.donor_id
    LEFT JOIN person person_d ON donor.person_id = person_d.person_id

    LEFT JOIN fundraiser ON donor.fundraiser_id = fundraiser.employee_id
    LEFT JOIN person person_f ON fundraiser.person_id = person_f.person_id

    LEFT JOIN fundraisingevent fe ON d.e_id = fe.e_id
    LEFT JOIN project p ON d.p_id = p.p_id
    LEFT JOIN towards t ON d.donation_id = t.donation_id;

-- סכום התרומות של כל תורם
SELECT
    donor_name,                         -- שם התורם
    SUM(d_amount) AS total_donations    -- סכום כל התרומות של התורם
FROM donation_overview
GROUP BY donor_id, donor_name -- מקבץ לפי מזהה ושם התורם
ORDER BY total_donations DESC;

-- כמה תורמים באו לכל אירוע התרמה
SELECT
event_id, event_name,
COUNT(donor_id) AS amount_of_participants
FROM donation_overview
WHERE event_id IS NOT NULL
GROUP BY event_id, event_name
ORDER BY amount_of_participants DESC;