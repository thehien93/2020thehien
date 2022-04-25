const path = require('path')
const express = require('express')
const morgan = require('morgan')
const {engine} = require('express-handlebars')
const app = express()
const port = 3000; 
const route = require('./routes')




app.use(morgan('combined'))
app.engine('hbs', engine(
    {extname: '.hbs'}
))
app.set('view engine', 'hbs')
app.set('views', path.join(__dirname, ''))
route(app)
app.listen(3000)