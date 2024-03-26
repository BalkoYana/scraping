const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Створюємо підключення до бази даних
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'scrapy'
});

// Підключаємось до бази даних
db.connect((err) => {
    if (err) throw err;
    console.log('Підключено до бази даних');
});
app.get('/kpi', (req, res) => {
    // Виконуємо SQL запит для отримання даних з таблиці 'items'
    const query = 'SELECT * FROM items';
    db.query(query, (err, results) => {
        if (err) throw err;
        // Відправляємо отримані дані як відповідь на GET запит
        res.json(results);
    });
});
app.post('/kpi', (req, res) => {
    // Отримуємо дані з запиту
    const data = req.body;

    // Вставляємо дані в таблицю 'items'
    const query = 'INSERT INTO items (name, department, url) VALUES (?, ?, ?)';
    db.query(query, [data.name, data.department, data.url], (err, result) => {
        if (err) throw err;
        console.log(result);
        res.send('Дані успішно збережено.');
    });
});

app.listen(3003, () => {
    console.log('Сервер запущено на порту 3003');
});
