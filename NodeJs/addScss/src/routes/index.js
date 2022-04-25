const newsRouter = require('./news')

 function route(app) {
   app.use('/', newsRouter)
 }

 module.exports = route