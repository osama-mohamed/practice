const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const methodOverride = require("method-override");
const port = process.env.PORT || 3000;
const app = express();


app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(methodOverride('_method'));
app.use(express.static(path.join(__dirname, "public")));


const routes = require('./routes/index');
app.use('/', routes);


app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
