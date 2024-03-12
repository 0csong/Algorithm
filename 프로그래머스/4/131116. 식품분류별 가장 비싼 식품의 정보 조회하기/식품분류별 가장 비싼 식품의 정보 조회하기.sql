# -- 코드를 입력하세요
# SELECT CATEGORY,MAX(PRICE) AS MAX_PRICE,PRODUCT_NAME
# FROM FOOD_PRODUCT 
# WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT 
#                 GROUP BY CATEGORY) AND CATEGORY IN ('과자', '국', '김치', '식용유')
# GROUP BY CATEGORY
# ORDER BY MAX_PRICE DESC

select CATEGORY, price as MAX_PRICE,  PRODUCT_NAME

from FOOD_PRODUCT

where PRICE in (
    select
    max(PRICE)
    from
    FOOD_PRODUCT 
    
    group by category
) and  
 CATEGORY in ('과자', '국', '김치', '식용유')

order by MAX_PRICE desc
