SELECT user_id, name, mail
FROM Users
WHERE mail  regexp '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$';