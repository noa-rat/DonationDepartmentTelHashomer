-- SELECT Queries

-- תורמים שתרמו למחלקות (ולא לפרויקטים) בהוראת קבע אך הם אינם חברים
SELECT d.donor_id,
(SELECT don_name
 FROM Donor
 WHERE Donor.donor_id = d.donor_id)
AS donor_name
FROM Donation d
-- תרמו בהוראת קבע
WHERE d.d_method = 'standing_order' 
	-- אינם חברים
AND (SELECT is_member
	FROM Donor
	WHERE Donor.donor_id = d.donor_id) = false
-- לא קיימת תרומה שלהם לפרויקט
AND NOT EXISTS
(SELECT p_id
 FROM Donation d2
 WHERE d2.donor_id = d.donor_id
 AND d2.p_id IS NOT NULL);
 
-- אנשי צוות לפי כמות התרומות שגייסו לפרויקטים שהסתיימו, בסדר יורד (כולל עמודה של הסכומים).
SELECT  s.s_id,  s.first_name,  s.last_name,
	-- מספר התרומות של התורמים של איש הצוות
	(SELECT COUNT(*)
	FROM Donation d
	WHERE d.donor_id IN
		(SELECT don.donor_id
		FROM Donor don
		WHERE don.s_id = s.s_id)
		-- תרומות לפרויקטים שהסתיימו
	AND d.p_id IN
		(SELECT p.p_id
		FROM Project p
		WHERE p.status = 'closed'))
	AS closed_project_donations
FROM StaffMember s
ORDER BY closed_project_donations DESC; -- מיון בסדר יורד לפי מספר התרומות

--  רשימת התורמים שתרמו תוך חודש מההגעה לאירוע.
SELECT don.donor_id, don.don_name
FROM donor don
-- תורמים שהשתתפו באירוע
WHERE don.donor_id IN (
	SELECT p.donor_id
	FROM participates_in p
	WHERE p.e_id IN (
	SELECT f.e_id
	FROM fundraisingevent f
	WHERE f.e_id IN (
		SELECT d.e_id
		FROM donation d
		WHERE
			-- תרומות של אותם תורמים
			don.donor_id = d.donor_id
			-- שהתבצעו מאוחר יותר באותו החודש
		AND
		(
			EXTRACT(YEAR FROM d.d_date) = EXTRACT(YEAR FROM f.e_date)
			AND EXTRACT(MONTH FROM d.d_date) = EXTRACT(MONTH FROM f.e_date)
			AND EXTRACT(DAY FROM d.d_date) >= EXTRACT(DAY FROM f.e_date)
		)
		--שהתבצעו בחודש שלאחר מכן (באותה השנה)י
		OR
		(
			EXTRACT(YEAR FROM d.d_date) = EXTRACT(YEAR FROM f.e_date)
			AND EXTRACT(MONTH FROM d.d_date) = EXTRACT(MONTH FROM f.e_date) + 1
			EXTRACT(DAY FROM d.d_date) <= EXTRACT(DAY FROM f.e_date)
		)
		--שהתבצעו בחודש שלאחר מכן בשנה הבאה (בינואר)י
		OR 
		(
			EXTRACT(MONTH FROM f.e_date) = 12
			AND EXTRACT(MONTH FROM d.d_date) = 1
			AND EXTRACT(YEAR FROM d.d_date) = EXTRACT(YEAR FROM f.e_date) + 1
			EXTRACT(DAY FROM d.d_date) <= EXTRACT(DAY FROM f.e_date)
		)
	)
)));

-- רשימת כל המחלקות וסכום התרומות שקיבלו בשלוש שנים האחרונות
SELECT d_name,
	-- סכום הכספים שנתרמו באותה השנה
	SUM(
		CASE
		WHEN EXTRACT(YEAR FROM d_date) = EXTRACT(YEAR FROM CURRENT_DATE) 
		THEN d_amount ELSE 0 
		END
        ) AS total_current_year,
	-- סכום הכספים שנתרמו שנה לפני כן
	SUM(
		CASE
		WHEN EXTRACT(YEAR FROM d_date) = EXTRACT(YEAR FROM CURRENT_DATE) - 1 
		THEN d_amount ELSE 0
		END
        ) AS total_last_year,
	-- סכום הכספים שנתרמו שנתיים לפני כן
	SUM(
		CASE 
		WHEN EXTRACT(YEAR FROM d_date) = EXTRACT(YEAR FROM CURRENT_DATE) - 2
		THEN d_amount ELSE 0
		END
        ) AS total_2_years_ago
FROM
-- מתוך תרומות למחלקות
donation NATURAL JOIN towards 
WHERE 
	EXTRACT(YEAR FROM d_date) BETWEEN EXTRACT(YEAR FROM CURRENT_DATE) - 2
	AND EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY d_name
ORDER BY total_current_year DESC; -- מיון בסדר יורד לפי סכום הכספים שנתרמו בשנה הנוכחית

-- מציגה לכל איש צוות את מספר התורמים שהביא לאירועים, כמה מהם תרמו בפועל, ואת שיעור ההצלחה באחוזים


SELECT s.s_id,  s.first_name,  s.last_name,
  Donor_stats.total_donors_brought,
  Donor_stats.donors_who_donated_at_event,
  -- אחוז התורמים שתרמו מתוך כלל התורמים שהשתתפו
  CASE 
    WHEN donor_stats.total_donors_brought = 0 THEN 0
    ELSE ROUND(100.0 * donor_stats.donors_who_donated_at_event / donor_stats.total_donors_brought, 2)
  END AS donation_participation_rate
FROM 
  StaffMember s
JOIN (
  	SELECT 
  	  s_id,
		COUNT(DISTINCT pi.donor_id) AS total_donors_brought, -- כלל התורמים שהשתתפו באירוע
		COUNT(DISTINCT CASE WHEN d.e_id IS NOT NULL THEN d.donor_id END) AS donors_who_donated_at_event -- התורמים שגם תרמו באירוע
	FROM 
		-- left join לספור את התורמים שהביא חבר הצוות לאירוע, גם אם הם לא תרמו
		Donor don NATURAL JOIN participates_in pi
		LEFT JOIN Donation d ON (d.donor_id = don.donor_id AND d.e_id IS NOT NULL GROUP BY s_id)
	) donor_stats ON s.s_id = donor_stats.s_id
ORDER BY 
  donor_stats.total_donors_brought DESC; -- ממוין לפי כמות המשתתפים
  
-- תורמים שתרמו יותר לפרויקטים מאשר למחלקות ממוין לפי גובה סכום התרומות לפרויקטים.

SELECT
	Donor_id,
	don_name,
	total_project_donations,
	total_department_donations
FROM 
	(SELECT Donor_id,
	(	 -- סכום הכספים שהוא תרם לפרויקטים
		SELECT SUM(d_amount)
		FROM donation
		WHERE donor_id = d.donor_id
		AND p_id IS NOT NULL
	) AS total_project_donations,
	( 	-- סכום הכספים שהוא תרם למחלקות
		SELECT SUM(d_amount)
		FROM donation
		WHERE donor_id = d.donor_id
		AND donation_id IN 
		(SELECT donation_id FROM towards)
	) AS total_department_donations
	FROM donation d
	GROUP BY donor_id
	) AS totals NATURAL JOIN donor
WHERE total_project_donations > total_department_donations -- רק התורמים שתרמו יותר לפרויקטים
ORDER BY total_project_donations DESC; -- ממוין לפי גובה סכום התרומות לפרויקטים

-- רשימת תורמים שתרמו יותר מ-60% מהכספים שגויסו למחלקה ספציפית.

SELECT 
	donor_id, 
	don_name, 
	d_name, -- שם המחלקה
	SUM(d_amount) AS donor_total_to_department,
	total_department_donations,
	-- חישוב אחוז סכום התרומות של התורם מתוך כלל התרומות למחלקה
	ROUND(SUM(d_amount) * 100.0 / total_department_donations,2) AS donation_percentage
FROM donor NATURAL JOIN donation NATURAL JOIN towards
		-- כלל התרומות לכל מחלקה
	NATURAL JOIN (
    	SELECT d_name, SUM(d_amount) AS total_department_donations
    	FROM donation NATURAL JOIN towards
   		GROUP BY d_name
		) AS dept_totals
GROUP BY donor_id, don_name, d_name, total_department_donations
HAVING SUM(d_amount) >= 0.6 * total_department_donations -- רק אם סכום התרומות שלו גבוה מ60%
ORDER BY donation_percentage DESC; -- לפי גובה אחוז התרומות

--   עבור כל אירוע – לאיזו מחלקה או פרויקט הוא התרים הכי הרבה.
-- סכום מקסימלי של תרומות למחלקות לפי אירוע
-- סכום מקסימלי של תרומות למחלקות לפי אירוע
SELECT
  d.e_id,
  d.d_name,
  SUM(d.d_amount) AS total_amount,
  'Department' AS target_type  -- סוג היעד מחלקה
FROM (donation NATURAL JOIN towards NATURAL JOIN department) AS d
GROUP BY d.e_id, d.d_name
HAVING SUM(d.d_amount) = (
  SELECT MAX(sum_amount)
  FROM (
    SELECT SUM(d2.d_amount) AS sum_amount
    FROM (donation NATURAL JOIN towards NATURAL JOIN department) AS d2
    WHERE d2.e_id = d.e_id
    GROUP BY d2.d_name
  ) AS subquery
)
UNION ALL
-- סכום מקסימלי של תרומות לפרויקטים לפי אירוע
SELECT
  dp.e_id,
  dp.p_name,
  SUM(dp.d_amount) AS total_amount,
  'Project' AS target_type  -- סוג היעד פרויקט
FROM (donation NATURAL JOIN project) AS dp
GROUP BY dp.e_id, dp.p_name
HAVING SUM(dp.d_amount) = (
  SELECT MAX(sum_amount)
  FROM (
    SELECT SUM(dp2.d_amount) AS sum_amount
    FROM (donation NATURAL JOIN project) AS dp2
    WHERE dp2.e_id = dp.e_id
    GROUP BY dp2.p_name
  ) AS subquery
);


-----------------------------------------------------------------------------

-- DELETE Queries

--  מחק כל חבר צוות שלא הביא תורמים, לא ארגן אירועים ואינו "מנהל"
DELETE FROM staffmember sm
WHERE 
-- לא ארגן אירועים בשנתיים האחרונות
	NOT EXISTS
		(SELECT *
		FROM organizes NATURAL JOIN fundraisingevent
		WHERE s_id = sm.s_id
		AND EXTRACT(YEAR FROM e_date) IN (2023, 2024))
	-- בשנה האחרונה הם לא אספו לפחות 2000 שקלים תרומות במשך 4 חודשים לפחות
	AND NOT EXISTS
		(SELECT s_id
		FROM
			(SELECT s_id,
				EXTRACT(YEAR FROM d_date) AS year,
				EXTRACT(MONTH FROM d_date) AS month,
				SUM(d_amount) AS monthly_sum
			FROM donor NATURAL JOIN donation
			WHERE EXTRACT(YEAR FROM d_date) IN (2024)
			GROUP BY s_id, year, month
			HAVING SUM(d_amount) >= 2000
		) AS monthly_totals
		WHERE monthly_totals.s_id = sm.s_id
GROUP BY s_id                                          	-- לקבץ אותם לפי איש צוות
HAVING COUNT(*) >= 8)                           	-- יותר או שווה ל-8 חודשים
AND LOWER(sm.position) NOT LIKE '%manager%'

-- מחק פרויקטים שבהם התרומות שהתקבלו היו פחות מ-5% מיעד הגיוס והם מסומנים כ"ongoing" אך תאריך ההתחלה חלף לפני שנה לפחות.

DELETE FROM project p
WHERE EXISTS (
	SELECT d.p_id
	FROM donation d
	WHERE d.p_id = p.p_id
	GROUP BY d.p_id
	HAVING SUM(d.d_amount) < 0.05 * p.fundraising_goal
	)
AND (
	p.status = 'ongoing'
	AND (
		EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM p.start_date) > 1
		OR (
		EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM p.start_date) = 1
		AND EXTRACT(MONTH FROM CURRENT_DATE) > EXTRACT(MONTH FROM p.start_date)
		)
		OR (
			EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM p.start_date) = 1
			AND EXTRACT(MONTH FROM CURRENT_DATE) = EXTRACT(MONTH FROM p.start_date)
			AND EXTRACT(DAY FROM CURRENT_DATE) >= EXTRACT(DAY FROM p.start_date)
		)
		)
);

-- מחק תורמים שבשנתיים האחרונות תרמו רק פעם אחת (או בכלל לא) ולא השתתפו בשום אירוע.

DELETE FROM donor don
-- התורם אינו חבר
WHERE is_member = FALSE
-- התורם לא השתתף באף אירוע
AND NOT EXISTS (
	SELECT * 
	FROM participates_in NATURAL JOIN fundraisingevent
	WHERE donor_id = don.donor_id
	AND EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM e_date) <= 2)
	AND (
		-- מספר התרומות בשנתיים האחרונות עבור תורם זה הוא 0 או 1
		SELECT COUNT(*) 
		FROM donation d 
		WHERE d.donor_id = don.donor_id
		AND EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM d.d_date) > 2
		) <= 1
		
-----------------------------------------------------------------------------

-- UPDATE Queries

--   להעלות ב-5% את שכרם של עשרת אנשי הצוות שהביאו את סכום התרומות הגבוה ביותר בחצי השנה האחרונה.
UPDATE StaffMember
SET salary = salary * 1.05
WHERE s_id IN
(SELECT s_id
 FROM Donation d NATURAL JOIN donor
 WHERE EXTRACT(YEAR FROM d.d_date) = 2024
 AND EXTRACT(MONTH FROM d.d_date) BETWEEN 7 AND 12    	-- רק במחצית השנייה של השנה
GROUP BY s_id
ORDER BY SUM(d.d_amount) DESC
LIMIT 10);

-- להפוך תורמים שתרמו לפחות 10,000 ש"ח והשתתפו לפחות ב-2 אירועים בשנה האחרונה לחברים
UPDATE Donor
SET is_member = TRUE
WHERE donor_id IN (
  SELECT don.donor_id
  FROM Donor don
  JOIN Donation d ON don.donor_id = d.donor_id
  JOIN participates_in pi ON don.donor_id = pi.donor_id
  WHERE 
    don.is_member = FALSE
    AND d.d_date >= CURRENT_DATE - INTERVAL '1 year'
    AND pi.e_id IN (
      SELECT e_id
      FROM FundraisingEvent
      WHERE e_date >= CURRENT_DATE - INTERVAL '1 year'
    )
  GROUP BY don.donor_id
  HAVING 
    SUM(d.d_amount) > 10000
    AND COUNT(DISTINCT pi.e_id) >= 2
);

-- סמן את הפרויקטים שהגיעו ליעד הגיוס שלהם כסגורים

UPDATE Project
SET status = 'closed'
WHERE p_id IN (
	SELECT p_id
	FROM Donation
	GROUP BY p_id
	HAVING SUM(d_amount) >=
		SELECT fundraising_goal
		FROM Project
		WHERE p_id = Donation.p_id
	)
);








