const express = require('express');
const app = express();

app.get('/',(req,res)=>{
res.render('index.ejs');
});
console.log('thehien');

app.listen(3000);
