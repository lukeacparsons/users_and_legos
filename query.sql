SELECT
	signup_week_start,
	first_order_week_start, 
	COUNT(user_id) AS "user_count",
	DATEDIFF('week',signup_week_start, first_order_week_start) AS "order_week_n_post_signup",
	ratio_to_report(user_count) over () AS "percentage_of_cohort"
FROM (
	SELECT
  		date_trunc('week',MIN(order_timestamp)) AS "first_order_week_start",
  		signup_week_start,
  		cohort_users.user_id
 	FROM (
    	SELECT
        	user_id,
    		date_trunc('week', signup_timestamp) AS "signup_week_start"
      	FROM user_signup
      	WHERE 
         	signup_timestamp BETWEEN 
	         	DATE_TRUNC('week', CAST('2019-01-01' AS datetime)) AND 
         		DATE_ADD('week',1 ,DATE_TRUNC('week',CAST('2019-01-01' AS datetime)))
  	) AS cohort_users
  LEFT OUTER JOIN user_order uo on cohort_users.user_id = uo.user_id
  WHERE 
	DATE_TRUNC('week',uo.order_timestamp) BETWEEN 
		DATE_TRUNC('week', CAST('2019-01-01' AS datetime)) AND 
		getdate() 
	OR uo.order_timestamp is NULL
  GROUP BY cohort_users.user_id, signup_week_start
) 
GROUP BY first_order_week_start, signup_week_start
ORDER BY (CASE WHEN first_order_week_start IS NULL THEN 1 ELSE 0 END) DESC, order_week_n_post_signup;


