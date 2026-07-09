CREATE DATABASE netflix_viewer_analysis;
USE netflix_viewer_analysis;
SELECT COUNT(*) AS Total_Records
FROM netflix_cleaned;
SELECT * 
FROM netflix_cleaned
ORDER BY user_id DESC
LIMIT 5;
USE netflix_viewer_analysis;
DROP TABLE netflix_cleaned;
SELECT COUNT(*) AS Total_Records
FROM netflix_cleaned;
USE netflix_viewer_analysis;
DROP TABLE netflix_cleaned;
SELECT COUNT(*) AS Total_Records
FROM netflix_cleaned;
SELECT COUNT(*) AS Total_Users
FROM netflix_cleaned;
SELECT gender, COUNT(*) AS Total
FROM netflix_cleaned
GROUP BY gender
ORDER BY Total DESC;
SELECT age_group, COUNT(*) AS Total
FROM netflix_cleaned
GROUP BY age_group
ORDER BY age_group;
SELECT subscription_plan, COUNT(*) AS Total
FROM netflix_cleaned
GROUP BY subscription_plan
ORDER BY Total DESC;
SELECT device_type, COUNT(*) AS Total
FROM netflix_cleaned
GROUP BY device_type
ORDER BY Total DESC;
SELECT country, COUNT(*) AS Total
FROM netflix_cleaned
GROUP BY country
ORDER BY Total DESC
LIMIT 10;
SELECT content_type, COUNT(*) AS Total
FROM netflix_cleaned
GROUP BY content_type;
SELECT AVG(rating) AS Average_Rating
FROM netflix_cleaned;
SELECT AVG(avg_weekly_watch_time) AS Average_Watch_Time
FROM netflix_cleaned;
SELECT AVG(completion_percentage) AS Avg_Completion
FROM netflix_cleaned;
