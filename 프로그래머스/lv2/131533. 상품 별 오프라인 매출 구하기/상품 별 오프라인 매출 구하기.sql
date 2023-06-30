
SELECT p.product_code, sum(p.price*o.sales_amount) AS sales 
FROM product p
JOIN (select product_id, sales_amount FROM offline_sale) AS o
ON p.product_id = o.product_id
GROUP BY p.product_id
ORDER BY sales DESC, p.product_code