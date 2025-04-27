-- commit and rollback

commit;

insert into donor (don_name, donor_id, address, is_member, don_email, don_phone, d_type, city, country, s_id)
  VALUES('Rachel Imenu', 9990, '1 derech avot', true, 'rachel@imenu.org', '0526676782', 'individual', 'Jerusalem', 'Israel', 1189);

SELECT *
FROM Donor
WHERE donor_id = 9990;

UPDATE donor
SET city = 'Tel Aviv'
WHERE donor_id = 9990;

SELECT *
FROM Donor
WHERE donor_id = 9990;

rollback;

SELECT *
FROM Donor
WHERE donor_id = 9990;
