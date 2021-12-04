SELECT * FROM
    (SELECT 'customer',C.id AS id, C.customer_name AS name FROM customer C
    LEFT JOIN invoice I ON I.customer_id = C.id
    WHERE I.customer_id IS NULL
    UNION SELECT 'product',P.id AS id, P.product_name AS name FROM product P
    LEFT JOIN invoice_item II ON P.id = II.product_id
    WHERE II.product_id IS NULL) AS A
ORDER BY name