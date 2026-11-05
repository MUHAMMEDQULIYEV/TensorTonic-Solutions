-- Returns: name, subject, score.
select name,subject, score from students
 order by score DESC NULLS last,name ASC