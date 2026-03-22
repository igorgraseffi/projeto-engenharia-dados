-- =====================================
-- QUERY 1: Receita por estado
-- =====================================
SELECT c.customer_state, SUM(f.price) AS receita
FROM fato_vendas f
JOIN dim_cliente c ON f.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY receita DESC;

-- =====================================
-- QUERY 2: Ticket médio
-- =====================================
SELECT AVG(price) AS ticket_medio
FROM fato_vendas;

-- =====================================
-- QUERY 3: Vendas por mês
-- =====================================
SELECT DATE_TRUNC('month', order_purchase_timestamp) AS mes,
       SUM(price) AS vendas
FROM fato_vendas
GROUP BY mes
ORDER BY mes;

-- =====================================
-- QUERY 4: Frete médio por estado
-- =====================================
SELECT c.customer_state, AVG(f.freight_value) AS frete_medio
FROM fato_vendas f
JOIN dim_cliente c ON f.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY frete_medio DESC;

-- =====================================
-- QUERY 5: Clientes mais ativos
-- =====================================
SELECT LEFT(customer_id, 8) AS cliente, COUNT(*) AS compras
FROM fato_vendas
GROUP BY customer_id
ORDER BY compras DESC
LIMIT 10;