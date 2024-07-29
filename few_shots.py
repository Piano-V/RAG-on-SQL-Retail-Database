few_shots = [
    {
        'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        'SQLResult': "Result of the SQL query",
        'Answer': "45"
    },
    {
        'Question': "How much is the total price of the inventory for all S-size t-shirts?",
        'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
        'SQLResult': "Result of the SQL query",
        'Answer': "23115"
    },
    {
        'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue our store will generate (post discounts)?",
        'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue 
                       FROM (SELECT sum(price*stock_quantity) as total_amount, t_shirt_id 
                             FROM t_shirts 
                             WHERE brand = 'Levi'
                             GROUP BY t_shirt_id) a 
                       LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id""",
        'SQLResult': "Result of the SQL query",
        'Answer': "26347"
    },
    {
        'Question': "How many black color Levi's t-shirts do we have available whose size is bigger than small?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE color='Black' AND brand = 'Levi' AND size IN ('M','L','XL')",
        'SQLResult': "Result of the SQL query",
        'Answer': "143"
    },
    {
        'Question': "How much stock of black color Levi's t-shirts do we have available whose size is bigger than small?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE color='Black' AND brand = 'Levi' AND size IN ('M','L','XL')",
        'SQLResult': "Result of the SQL query",
        'Answer': "143"
    },
    {
        'Question': "How many white color Levi's shirt I have?",
        'SQLQuery': "SELECT stock_quantity FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
        'SQLResult': "Result of the SQL query",
        'Answer': "205"
    }
    
]
